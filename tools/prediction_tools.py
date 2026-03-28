from datetime import datetime

def get_crowd_trend(floor: str) -> dict:
    """Predicts crowd trend for a floor based on time of day and day of week."""
    hour = datetime.now().hour
    day  = datetime.now().weekday()  # 0=Mon, 6=Sun
    is_peak    = (10 <= hour <= 14) or (18 <= hour <= 21)
    is_weekend = day >= 5

    base_load = {
        "1st Floor": 0.70,
        "2nd Floor": 0.60,
        "3rd Floor": 0.40,
        "4th Floor": 0.35,
        "5th Floor": 0.25,
        "6th Floor": 0.30,
    }

    load = base_load.get(floor, 0.5)
    load *= 1.3 if is_peak else 0.8
    load *= 0.6 if is_weekend else 1.0
    load  = min(round(load, 2), 1.0)

    if load > 0.75:
        msg   = "This area is filling up quickly — go now!"
        level = "high"
    elif load > 0.50:
        msg   = "Moderate activity — best to head there soon."
        level = "medium"
    else:
        msg   = "Low traffic right now — should stay open for a while."
        level = "low"

    return {
        "floor":          floor,
        "predicted_load": load,
        "trend":          level,
        "message":        msg,
        "is_peak_hours":  is_peak,
    }