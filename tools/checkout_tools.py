import time
import hashlib

SESSION_STORE: dict = {}
SESSION_DURATION = 7200  # 2 hours
EXTEND_DURATION  = 1800  # 30 minutes


def reserve_seat(seat_id: str, student_id: str,
                 student_name: str, floor: str) -> dict:
    """Check a student into a seat and start their session."""
    if seat_id in SESSION_STORE:
        return {"success": False,
                "message": f"Seat {seat_id} is already reserved."}
    now = time.time()
    SESSION_STORE[seat_id] = {
        "student_id":    student_id,
        "student_name":  student_name,
        "floor":         floor,
        "checked_in_at": now,
        "expires_at":    now + SESSION_DURATION,
        "extensions":    0,
    }
    return {
        "success":    True,
        "seat_id":    seat_id,
        "student_id": student_id,
        "message":    f"Seat {seat_id} reserved for {student_name}. Session expires in 2 hours.",
    }


def checkout_seat(seat_id: str, student_id: str) -> dict:
    """Manually release a seat."""
    session = SESSION_STORE.get(seat_id)
    if not session:
        return {"success": False,
                "message": f"No active reservation for seat {seat_id}."}
    if session["student_id"] != student_id:
        return {"success": False, "message": "Student ID does not match."}
    del SESSION_STORE[seat_id]
    return {"success": True, "seat_id": seat_id,
            "message": f"Checked out of {seat_id}. Seat is now available."}


def extend_session(seat_id: str, student_id: str) -> dict:
    """Extend a session by 30 minutes. Max 2 extensions."""
    session = SESSION_STORE.get(seat_id)
    if not session:
        return {"success": False, "message": "No active reservation found."}
    if session["student_id"] != student_id:
        return {"success": False, "message": "Student ID does not match."}
    if session["extensions"] >= 2:
        return {"success": False,
                "message": "Maximum 2 extensions already used."}
    session["expires_at"]  += EXTEND_DURATION
    session["extensions"]  += 1
    remaining = 2 - session["extensions"]
    return {
        "success":         True,
        "extensions_used": session["extensions"],
        "message":         f"Session extended by 30 min. {remaining} extensions remaining.",
    }


def auto_expire_sessions() -> list:
    """Release all sessions past their expiry time."""
    now     = time.time()
    expired = [sid for sid, s in SESSION_STORE.items()
               if now >= s["expires_at"]]
    for sid in expired:
        del SESSION_STORE[sid]
    return expired


def generate_qr_token(seat_id: str, student_id: str) -> dict:
    """Generate a QR checkout token."""
    raw   = f"BULLSPACE|{seat_id}|{student_id}|CHECKOUT"
    token = hashlib.sha256(raw.encode()).hexdigest()[:12].upper()
    return {
        "qr_data":    raw,
        "token":      token,
        "seat_id":    seat_id,
        "student_id": student_id,
        "message":    f"Show token {token} at any library kiosk to check out.",
    }


def verify_qr_checkout(qr_data: str) -> dict:
    """Verify and process a QR scan from a kiosk."""
    parts = qr_data.split("|")
    if len(parts) != 4 or parts[0] != "BULLSPACE" or parts[3] != "CHECKOUT":
        return {"success": False, "message": "Invalid QR code."}
    return checkout_seat(parts[1], parts[2])