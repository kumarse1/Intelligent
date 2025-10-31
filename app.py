python# app.py
import streamlit as st
from mock_tickets import tickets

st.set_page_config(page_title="Healthcare Enrollment Assistant", page_icon="🏥")

st.title("🏥 Smart Enrollment Support Assistant")
st.markdown("### Get help with member enrollment issues")

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.query = ""
    st.session_state.category = ""
    st.session_state.subcategory = ""

# --- STEP 1: Initial Query ---
if st.session_state.step == 1:
    st.markdown("#### What issue are you experiencing?")
    
    user_query = st.text_input("Describe your issue:", placeholder="e.g., can't add my kid, spouse won't enroll")
    
    if st.button("Search", type="primary"):
        if user_query:
            st.session_state.query = user_query
            st.session_state.step = 2
            st.rerun()

# --- STEP 2: Clarifying Questions ---
elif st.session_state.step == 2:
    st.markdown(f"**Your search:** _{st.session_state.query}_")
    st.markdown("---")
    
    # Show comparison
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ❌ Without Clarification")
        st.warning("Would show ALL 10 tickets (mixed issues)")
        for ticket in tickets[:5]:
            st.text(f"• {ticket['ticket_id']}: {ticket['title']}")
        st.text("... and 5 more")
    
    with col2:
        st.markdown("### ✅ With Clarification")
        st.info("Let me ask 2 quick questions first...")
    
    st.markdown("---")
    st.markdown("#### 🔍 Question 1: What type of issue?")
    
    category = st.radio(
        "Select category:",
        ["Adding a dependent (spouse/child)", 
         "Removing/terminating a dependent", 
         "Member profile/data issues"],
        key="category_radio"
    )
    
    if category:
        st.session_state.category = category
        
        st.markdown("#### 🔍 Question 2: More details")
        
        if "Adding" in category:
            subcategory = st.radio(
                "Who are you trying to add?",
                ["Newborn/Child", "Spouse", "Stepchild"],
                key="sub_radio"
            )
        elif "Removing" in category:
            subcategory = st.radio(
                "Who are you trying to remove?",
                ["Child (age out)", "Ex-spouse (divorce)", "Other dependent"],
                key="sub_radio"
            )
        else:
            subcategory = st.radio(
                "What's wrong with the profile?",
                ["Can't find member/dependent info", "Wrong information showing", "Data missing after enrollment"],
                key="sub_radio"
            )
        
        if subcategory:
            st.session_state.subcategory = subcategory
            
            if st.button("Show Results", type="primary"):
                st.session_state.step = 3
                st.rerun()

# --- STEP 3: Results ---
elif st.session_state.step == 3:
    st.markdown(f"**Original search:** _{st.session_state.query}_")
    st.markdown(f"**Refined to:** {st.session_state.category} → {st.session_state.subcategory}")
    st.markdown("---")
    
    # Simple filtering logic
    filtered_tickets = []
    
    if "Adding" in st.session_state.category:
        if "Newborn" in st.session_state.subcategory or "Child" in st.session_state.subcategory:
            filtered_tickets = [t for t in tickets if t['category'] == 'Dependent Addition' and t['subcategory'] == 'Child']
        elif "Spouse" in st.session_state.subcategory:
            filtered_tickets = [t for t in tickets if t['category'] == 'Dependent Addition' and t['subcategory'] == 'Spouse']
        elif "Stepchild" in st.session_state.subcategory:
            filtered_tickets = [t for t in tickets if 'step' in t['title'].lower()]
    
    elif "Removing" in st.session_state.category:
        filtered_tickets = [t for t in tickets if t['category'] == 'Dependent Termination']
        
        if "age" in st.session_state.subcategory.lower():
            filtered_tickets = [t for t in filtered_tickets if 'age' in t['title'].lower() or t['error_type'] == 'Age Out']
        elif "spouse" in st.session_state.subcategory.lower():
            filtered_tickets = [t for t in filtered_tickets if t['subcategory'] == 'Spouse']
    
    else:  # Profile issues
        filtered_tickets = [t for t in tickets if t['category'] == 'Profile Issues']
    
    # Display results
    if filtered_tickets:
        st.success(f"✅ Found {len(filtered_tickets)} highly relevant ticket(s):")
        
        for ticket in filtered_tickets:
            with st.expander(f"🎫 {ticket['ticket_id']}: {ticket['title']}"):
                st.markdown(f"**Problem:** {ticket['description']}")
                st.markdown(f"**Resolution:** {ticket['resolution']}")
                st.markdown(f"**Category:** {ticket['category']} - {ticket['subcategory']}")
                st.markdown(f"**Error Type:** {ticket['error_type']}")
    else:
        st.warning("⚠️ No exact matches found.")
        st.info("💡 **SOP Generation Mode:** Based on similar issues in your cluster, here's a suggested resolution process...")
        st.markdown("""
        **Suggested Steps:**
        1. Verify qualifying life event documentation
        2. Check system eligibility window settings
        3. Validate dependent relationship type in system
        4. Review data sync status between portal and core system
        """)
    
    # Metrics comparison
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Search Attempts", "1", delta="-2", delta_color="inverse")
    with col2:
        st.metric("Relevant Results", len(filtered_tickets), delta="+3")
    with col3:
        st.metric("Time Saved", "~5 min", delta="+5 min")
    
    if st.button("Start New Search"):
        st.session_state.step = 1
        st.session_state.query = ""
        st.session_state.category = ""
        st.session_state.subcategory = ""
        st.rerun()
