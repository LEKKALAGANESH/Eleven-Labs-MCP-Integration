import os
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_BASE_URL = os.getenv("ELEVENLABS_BASE_URL", "https://api.elevenlabs.io/v1")
AGENT_VOICE_ID = os.getenv("AGENT_VOICE_ID", "Xb7hH8MSUJpSbSDYk0k2")  # Alice
AGENT_PHONE_NUMBER_ID = os.getenv("AGENT_PHONE_NUMBER_ID") 