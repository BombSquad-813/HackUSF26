from dotenv import load_dotenv
load_dotenv()

import asyncio
import time
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agent import root_agent


async def main():
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="bullspace_ai",
        session_service=session_service,
    )

    session = await session_service.create_session(
        app_name="bullspace_ai",
        user_id="U12345678",
    )

    print("=" * 60)
    print("  BullSpace AI — USF Smart Library System")
    print("  Type your request below. Type 'exit' to quit.")
    print("=" * 60)

    while True:
        user_input = input("\nStudent: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye! Go Bulls!")
            break

        message = Content(parts=[Part(text=user_input)])

        async for event in runner.run_async(
            user_id="U12345678",
            session_id=session.id,
            new_message=message,
        ):
            if event.is_final_response():
                print(f"\nBullSpace AI: {event.content.parts[0].text}\n")

        time.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())