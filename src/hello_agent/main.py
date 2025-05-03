import asyncio
from agents import Agent, Runner
from dotenv import load_dotenv
import os

def my_first_agent():
    # Load environment variables from .env file
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    # Define the agent
    agent = Agent(
        name="HelloAgent",
        instructions="You are a helpful assistant that responds with 'Hello, world!'"
    )

    # Run the agent
    async def run_agent():
        result = await Runner.run(agent, "Say hello to the world!")
        print(result.final_output)

    asyncio.run(run_agent())
