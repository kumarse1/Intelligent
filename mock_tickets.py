python# mock_tickets.py
tickets = [
    {
        "ticket_id": "ENR-1001",
        "title": "Cannot add dependent child to policy",
        "description": "Member tried to add newborn within 30 days but system shows 'eligibility window closed' error",
        "resolution": "Backend eligibility date was not updated. Reset enrollment window in system.",
        "category": "Dependent Addition",
        "subcategory": "Child",
        "error_type": "Eligibility Window"
    },
    {
        "ticket_id": "ENR-1002", 
        "title": "Spouse enrollment failing - marriage date issue",
        "description": "Member married 2 weeks ago, trying to add spouse but gets 'qualifying event not found'",
        "resolution": "Marriage certificate date didn't match system date. Updated qualifying life event manually.",
        "category": "Dependent Addition",
        "subcategory": "Spouse",
        "error_type": "Qualifying Event"
    },
    {
        "ticket_id": "ENR-1003",
        "title": "Child over 26 showing as eligible dependent",
        "description": "System allowing enrollment of 27-year-old child, should be termed",
        "resolution": "Age-out rule not triggered. Ran batch process to term dependent.",
        "category": "Dependent Termination",
        "subcategory": "Child",
        "error_type": "Age Out"
    },
    {
        "ticket_id": "ENR-1004",
        "title": "Member details missing after open enrollment",
        "description": "Member completed open enrollment but profile shows empty, no coverage details visible",
        "resolution": "Data sync issue between enrollment portal and core system. Manually pushed data.",
        "category": "Profile Issues",
        "subcategory": "Missing Data",
        "error_type": "System Sync"
    },
    {
        "ticket_id": "ENR-1005",
        "title": "Cannot terminate ex-spouse after divorce",
        "description": "Divorce finalized 1 month ago, system won't allow dependent termination, shows 'active coverage'",
        "resolution": "Required divorce decree upload. After verification, termed coverage retroactively.",
        "category": "Dependent Termination",
        "subcategory": "Spouse",
        "error_type": "Qualifying Event"
    },
    {
        "ticket_id": "ENR-1006",
        "title": "Newborn SSN not accepting in system",
        "description": "Baby born 10 days ago, SSN issued but system rejects it as 'invalid format'",
        "resolution": "New SSN format validation was too strict. Adjusted regex pattern in enrollment module.",
        "category": "Dependent Addition",
        "subcategory": "Child",
        "error_type": "SSN Validation"
    },
    {
        "ticket_id": "ENR-1007",
        "title": "Member trying to term self instead of dependent",
        "description": "User clicked wrong button, terminated own coverage instead of child's",
        "resolution": "Reinstated member coverage, termed correct dependent. Improved UI labeling.",
        "category": "Dependent Termination",
        "subcategory": "User Error",
        "error_type": "Wrong Selection"
    },
    {
        "ticket_id": "ENR-1008",
        "title": "Stepchild enrollment rejected - relationship not recognized",
        "description": "Member trying to add stepchild but system only shows 'child' and 'spouse' options",
        "resolution": "Added 'stepchild' relationship type. Requires marriage certificate + birth certificate.",
        "category": "Dependent Addition",
        "subcategory": "Child",
        "error_type": "Relationship Type"
    },
    {
        "ticket_id": "ENR-1009",
        "title": "Member profile shows wrong plan after enrollment change",
        "description": "Changed from Gold to Silver plan but portal still displays Gold coverage details",
        "resolution": "Cache not cleared after plan change. Cleared cache and refreshed member session.",
        "category": "Profile Issues",
        "subcategory": "Incorrect Data",
        "error_type": "Cache Issue"
    },
    {
        "ticket_id": "ENR-1010",
        "title": "Cannot find dependent in system after successful enrollment",
        "description": "Added child 2 days ago, confirmation received, but child not visible in member portal",
        "resolution": "Dependent data in staging table, not promoted to production. Ran promotion script.",
        "category": "Profile Issues",
        "subcategory": "Missing Data",
        "error_type": "System Sync"
    }
]
