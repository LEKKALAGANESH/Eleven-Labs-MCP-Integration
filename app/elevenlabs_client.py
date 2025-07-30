import requests
from .config import ELEVENLABS_API_KEY, ELEVENLABS_BASE_URL

HEADERS = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}

def create_agent(name, first_message, system_prompt, voice_id):
    url = f"{ELEVENLABS_BASE_URL}/agents"
    payload = {
        "name": name,
        "first_message": first_message,
        "system_prompt": system_prompt,
        "voice_id": voice_id,
        "language": "en",
        "temperature": 0.7,
        "asr_quality": "high",
        "model_id": "eleven_turbo_v2",
        "optimize_streaming_latency": 3,
        "stability": 0.6,
        "similarity_boost": 0.8,
        "turn_timeout": 10,
        "max_duration_seconds": 300,
        "record_voice": True,
        "retention_days": 30
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

def make_outbound_call(agent_id, agent_phone_number_id, to_number):
    url = f"{ELEVENLABS_BASE_URL}/calls/outbound"
    payload = {
        "agent_id": agent_id,
        "agent_phone_number_id": agent_phone_number_id,
        "to_number": to_number
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json() 