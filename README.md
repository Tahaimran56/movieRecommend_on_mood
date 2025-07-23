 Movie Recommendation Agent using Gemini API & OpenAI Agents SDK
This project demonstrates how to build a smart movie recommendation system using OpenAI’s Agent SDK with a Google Gemini-compatible API. It takes a user's mood (like sad, happy, bored) and returns a structured list of movie suggestions with titles, genres, ratings, and release years.
🧩 Features
🧠 Agentic AI using OpenAI Agents SDK

🔗 Connects to Google Gemini (via OpenAI-compatible endpoint)

🎯 Structured JSON output using Pydantic

🎥 Returns a list of movies with rating, genre, and release year

🚀 Asynchronous, production-ready setup

⚙️ Requirements
Python 3.8+

openai-agents

pydantic

python-dotenv

📦 Installation
# Install required packages
pip install openai-agents pydantic python-dotenv
🔐 Environment Setup
Create a .env file in your root directory and add your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key_here
🚀 Run the Agent

python check.py
🧠 How It Works
Loads your Gemini API key

Initializes a Gemini-compatible client with AsyncOpenAI

Defines an Agent that responds based on mood

Returns a structured list of movie suggestions in a MovieRecommend schema

📤 Example Output
Mood: sad

Recommended Movies:
🎥 The Pursuit of Happyness (2006) | Genre: Drama | ⭐ 8.0/10
🎥 Inside Out (2015)               | Genre: Animation | ⭐ 8.2/10
🎥 Amélie (2001)                   | Genre: Comedy | ⭐ 8.3/10
🧠 Schema Design
class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: float

class MovieRecommend(BaseModel):
    mood: str
    movies: List[Movie]
✅ Future Improvements
📽 Add trailer links and posters

🌐 Integrate with TMDb or IMDb API for live results

💻 Display in Streamlit app

🎭 Include mood detection from voice or chat



