from google.adk.agents import LlmAgent
from tools.prediction_tools import get_crowd_trend

prediction_agent = LlmAgent(
    name="prediction_agent",
    model="groq/llama-3.3-70b-versatile",
    description="Predicts crowd trends and peak hours for each library floor.",
    instruction="""
    You are the Prediction Agent for BullSpace AI at USF Tampa Library.
    Use get_crowd_trend(floor) to forecast occupancy based on time of day.
    Return: predicted_load, trend level (low/medium/high), and a friendly message.
    If load > 75%: warn the student urgently.
    If load > 50%: suggest going soon.
    If load < 30%: confirm it is a good time.
    """,
    tools=[get_crowd_trend],
)