from google.adk.agents import LlmAgent
from tools.checkout_tools import (
    reserve_seat,
    checkout_seat,
    extend_session,
    generate_qr_token,
    verify_qr_checkout,
    auto_expire_sessions,
)

checkout_agent = LlmAgent(
    name="checkout_agent",
    model="groq/llama-3.3-70b-versatile",
    description="Handles seat reservations, session timers, extensions, and all three checkout methods.",
    instruction="""
    You are the Checkout Agent for BullSpace AI at USF Tampa Library.
    You manage the full reservation lifecycle:

    RESERVE  : Use reserve_seat(seat_id, student_id, student_name, floor)
    CHECKOUT : Use checkout_seat(seat_id, student_id)
    EXTEND   : Use extend_session(seat_id, student_id) — max 2 times
    QR       : Use generate_qr_token() to create, verify_qr_checkout() when scanned
    EXPIRE   : Use auto_expire_sessions() to release timed-out seats

    Rules:
    - Sessions last 2 hours. Max 2 extensions of 30 min each.
    - Always confirm student_id matches before checkout or extension.
    - On auto-expire notify the student their seat has been released.
    """,
    tools=[
        reserve_seat,
        checkout_seat,
        extend_session,
        generate_qr_token,
        verify_qr_checkout,
        auto_expire_sessions,
    ],
)