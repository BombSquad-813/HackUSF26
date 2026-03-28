DIRECTIONS = {
    "1st Floor": [
        "Enter through the main library entrance on Leroy Collins Blvd.",
        "Learning Commons Study Area is straight ahead.",
        "Computer Lab is along the east wall.",
        "VizLab is on the far left past the Service Desk.",
    ],
    "2nd Floor": [
        "Enter the main library entrance.",
        "Take elevators or stairs to Floor 2.",
        "Smart Lab is on the right — look for the computer workstations.",
        "Tutoring Hub and Writing Center are on the left.",
        "Numbered carrels (218-228) line the west wall.",
    ],
    "3rd Floor": [
        "Take elevators to Floor 3.",
        "West carrels (305-331) are along the left wall.",
        "East carrels (335-358) are along the right wall.",
        "Open reading tables are in the center.",
    ],
    "4th Floor": [
        "Take elevators to Floor 4.",
        "West carrels (440-464) are along the left wall.",
        "Special Collections Reading Room is at the north center.",
        "Bring your USF ID for Special Collections access.",
    ],
    "5th Floor": [
        "Take elevators to Floor 5 — quiet study floor.",
        "No talking permitted anywhere on this floor.",
        "Reading Rooms 520A-D are on the west side.",
        "Reading Rooms 514A-D are on the east side.",
        "Graduate Reading Room is in the center.",
    ],
    "6th Floor": [
        "Take elevators to Floor 6.",
        "Bellini AI College seating is past the info desk.",
        "LIB 645 Conference Room requires advance booking.",
    ],
}

def get_directions(floor: str, zone: str = None) -> dict:
    """Returns step-by-step directions to a floor and optional zone."""
    steps = DIRECTIONS.get(floor, ["Take elevators to " + floor + "."])
    if zone:
        steps = steps + [f"Look for '{zone}' signage once you exit the elevator."]
    return {
        "floor": floor,
        "zone":  zone,
        "steps": steps,
        "tip":   "Elevators are in the center of the building on every floor.",
    }