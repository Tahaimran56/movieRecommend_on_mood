import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from typing import List
# 1. Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# 2. Set up Gemini-compatible OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 3. Define the model to use
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # adjust if your model name is different
    openai_client=external_client
)

# 4. Set up the runner config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)





class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: float

class MovieRecommend(BaseModel):
    mood: str
    movies:List[Movie]

agent = Agent(
    name="MovieRecommendationAgent",
    instructions="Recommend movies based on user's mood using the MovieRecommend schema.",
    output_type=MovieRecommend,
    model=model
)

async def main():
    query = "I’m feeling a bit demotivated. Can you suggest some uplifting movies?"
    result = await Runner.run(agent, query, run_config=config)

    print(f"\nMood: {result.final_output.mood}")
    print("\nRecommended Movies:")
    for movie in result.final_output.movies:
        print(f"🎥 {movie.title} ({movie.year}) | Genre: {movie.genre} | ⭐ {movie.rating}/10")

asyncio.run(main())