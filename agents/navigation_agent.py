from google.adk.agents import LlmAgent
from tools.navigation_tools import get_directions

navigation_agent = LlmAgent(
    name="navigation_agent",
    model="groq/llama-3.3-70b-versatile",
    description="Provides step-by-step directions to any floor or zone in the USF library.",
    instruction="""
    You are the Navigation Agent for BullSpace AI at USF Tampa Library.
    Use get_directions(floor, zone) to generate step-by-step directions.
    Always start from the main library entrance on Leroy Collins Blvd.
    Keep directions human-friendly — no jargon or call numbers.
    Add a helpful tip at the end.
    """,
    tools=[get_directions],
)