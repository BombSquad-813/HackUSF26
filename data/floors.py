FLOORS = {
    "1st Floor": {
        "noise": "casual",
        "noise_label": "Casual conversation",
        "zones": [
            {"id": "1-LC01", "type": "table",    "cap": 4, "charger": True,  "special": False, "zone": "Learning Commons Study Area"},
            {"id": "1-LC02", "type": "table",    "cap": 4, "charger": True,  "special": False, "zone": "Learning Commons Study Area"},
            {"id": "1-LC03", "type": "table",    "cap": 4, "charger": False, "special": False, "zone": "Learning Commons Study Area"},
            {"id": "1-CL01", "type": "computer", "cap": 1, "charger": True,  "special": True,  "zone": "Computer Lab"},
            {"id": "1-CL02", "type": "computer", "cap": 1, "charger": True,  "special": True,  "zone": "Computer Lab"},
            {"id": "1-CL03", "type": "computer", "cap": 1, "charger": True,  "special": True,  "zone": "Computer Lab"},
            {"id": "1-VL01", "type": "station",  "cap": 1, "charger": True,  "special": True,  "zone": "VizLab"},
            {"id": "1-VL02", "type": "station",  "cap": 1, "charger": True,  "special": True,  "zone": "VizLab"},
            {"id": "1-YE01", "type": "table",    "cap": 6, "charger": False, "special": False, "zone": "Youth Experiences"},
        ]
    },
    "2nd Floor": {
        "noise": "moderate",
        "noise_label": "Moderate noise",
        "zones": [
            {"id": "2-LC01", "type": "carrel",   "cap": 1, "charger": True,  "special": False, "zone": "Learning Commons (218-228)"},
            {"id": "2-LC02", "type": "carrel",   "cap": 1, "charger": False, "special": False, "zone": "Learning Commons (218-228)"},
            {"id": "2-LC03", "type": "carrel",   "cap": 1, "charger": True,  "special": False, "zone": "Learning Commons (218-228)"},
            {"id": "2-SL01", "type": "computer", "cap": 1, "charger": True,  "special": True,  "zone": "Smart Lab"},
            {"id": "2-SL02", "type": "computer", "cap": 1, "charger": True,  "special": True,  "zone": "Smart Lab"},
            {"id": "2-TH01", "type": "table",    "cap": 6, "charger": True,  "special": False, "zone": "Tutoring Hub"},
            {"id": "2-TH02", "type": "table",    "cap": 6, "charger": False, "special": False, "zone": "Tutoring Hub"},
            {"id": "2-WC01", "type": "table",    "cap": 4, "charger": False, "special": True,  "zone": "Writing Center"},
            {"id": "2-CC01", "type": "carrel",   "cap": 1, "charger": True,  "special": True,  "zone": "Career Cube"},
        ]
    },
    "3rd Floor": {
        "noise": "low-moderate",
        "noise_label": "Low-moderate noise",
        "zones": [
            {"id": "3-W305", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "West Carrels (305-331)"},
            {"id": "3-W306", "type": "carrel", "cap": 1, "charger": True,  "special": False, "zone": "West Carrels (305-331)"},
            {"id": "3-W318", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "West Carrels (305-331)"},
            {"id": "3-E335", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "East Carrels (335-358)"},
            {"id": "3-E357", "type": "carrel", "cap": 1, "charger": True,  "special": False, "zone": "East Carrels (335-358)"},
            {"id": "3-OT01", "type": "table",  "cap": 4, "charger": True,  "special": False, "zone": "Open Reading Tables"},
            {"id": "3-OT02", "type": "table",  "cap": 4, "charger": False, "special": False, "zone": "Open Reading Tables"},
        ]
    },
    "4th Floor": {
        "noise": "low-moderate",
        "noise_label": "Low-moderate noise",
        "zones": [
            {"id": "4-W440", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "West Carrels (440-464)"},
            {"id": "4-W441", "type": "carrel", "cap": 1, "charger": True,  "special": False, "zone": "West Carrels (440-464)"},
            {"id": "4-E426", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "East Carrels (426-438)"},
            {"id": "4-E437", "type": "carrel", "cap": 1, "charger": True,  "special": False, "zone": "East Carrels (426-438)"},
            {"id": "4-SC01", "type": "table",  "cap": 6, "charger": False, "special": True,  "zone": "Special Collections Reading Room"},
            {"id": "4-SC02", "type": "table",  "cap": 6, "charger": False, "special": True,  "zone": "Special Collections Reading Room"},
        ]
    },
    "5th Floor": {
        "noise": "quiet",
        "noise_label": "Quiet study only",
        "zones": [
            {"id": "5-520A", "type": "room",   "cap": 6, "charger": True,  "special": True,  "zone": "Reading Room West (520A-D)"},
            {"id": "5-520B", "type": "room",   "cap": 6, "charger": True,  "special": True,  "zone": "Reading Room West (520A-D)"},
            {"id": "5-514A", "type": "room",   "cap": 6, "charger": True,  "special": True,  "zone": "Reading Room East (514A-D)"},
            {"id": "5-514B", "type": "room",   "cap": 6, "charger": True,  "special": True,  "zone": "Reading Room East (514A-D)"},
            {"id": "5-GR01", "type": "table",  "cap": 1, "charger": True,  "special": True,  "zone": "Graduate Reading Room"},
            {"id": "5-GR02", "type": "table",  "cap": 1, "charger": True,  "special": True,  "zone": "Graduate Reading Room"},
            {"id": "5-OC01", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "Open Stacks (QH-ZA)"},
            {"id": "5-OC02", "type": "carrel", "cap": 1, "charger": False, "special": False, "zone": "Open Stacks (QH-ZA)"},
        ]
    },
    "6th Floor": {
        "noise": "moderate",
        "noise_label": "Moderate noise",
        "zones": [
            {"id": "6-BA01", "type": "table", "cap": 4,  "charger": True,  "special": False, "zone": "Bellini AI College"},
            {"id": "6-BA02", "type": "table", "cap": 4,  "charger": False, "special": False, "zone": "Bellini AI College"},
            {"id": "6-CR01", "type": "room",  "cap": 12, "charger": True,  "special": True,  "zone": "LIB 645 Conference Room"},
        ]
    },
}

HOURS = {
    "Sun": "10am-8pm",
    "Mon": "7am-2am",
    "Tue": "7am-2am",
    "Wed": "7am-2am",
    "Thu": "7am-2am",
    "Fri": "7am-8pm",
    "Sat": "10am-10pm",
}