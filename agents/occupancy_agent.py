from google.adk.agents import LlmAgent
from tools.seat_tools import get_seat_status, get_available_seats

occupancy_agent = LlmAgent(
    name="occupancy_agent",
    model="groq/llama-3.3-70b-versatile",
    description="Monitors real-time seat availability across all USF library floors.",
    instruction="""
    You are the Occupancy Agent for BullSpace AI at USF Tampa Library.
    Use get_seat_status() to retrieve live seat data.
    Use get_available_seats() to filter seats by user preferences.
    Always return: seat_id, floor, zone, occupied status, charger, capacity.
    Be concise. Return structured data, not narrative.
    """,
    tools=[get_seat_status, get_available_seats],
)
