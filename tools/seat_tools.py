import random
from data.floors import FLOORS


def get_seat_status(floor: str = "all") -> dict:
    """Returns real-time seat availability.
    Args:
        floor: Floor name like '1st Floor' or 'all' for all floors
    """
    result = {}
    for floor_name, floor_data in FLOORS.items():
        if floor != "all" and floor_name != floor:
            continue
        for seat in floor_data["zones"]:
            sid = seat["id"]
            result[sid] = {
                **seat,
                "floor": floor_name,
                "noise": floor_data["noise"],
                "noise_label": floor_data["noise_label"],
                "occupied": random.choice([True, False, False]),
            }
    return result


def get_available_seats(
    noise_pref: str = "any",
    needs_charger: str = "no",
    group_size: str = "1",
    seat_type: str = "any",
    floor: str = "all",
) -> list:
    """Returns available seats matching student preferences.
    Args:
        noise_pref: 'quiet', 'moderate', 'casual', 'low-moderate', or 'any'
        needs_charger: 'yes' or 'no'
        group_size: number of people as a string like '1', '2', '4'
        seat_type: 'carrel', 'table', 'computer', 'station', 'room', or 'any'
        floor: Floor name like '1st Floor' or 'all'
    """
    all_seats = get_seat_status(floor)
    results = []
    size = int(group_size) if group_size.isdigit() else 1

    for seat_id, seat in all_seats.items():
        if seat["occupied"]:
            continue
        if noise_pref != "any" and seat["noise"] != noise_pref:
            continue
        if needs_charger == "yes" and not seat["charger"]:
            continue
        if seat["cap"] < size:
            continue
        if seat_type != "any" and seat["type"] != seat_type:
            continue
        results.append({"seat_id": seat_id, **seat})

    results.sort(key=lambda s: s["floor"])
    return results