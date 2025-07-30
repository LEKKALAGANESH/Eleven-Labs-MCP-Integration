from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .elevenlabs_client import create_agent, make_outbound_call
from .config import AGENT_VOICE_ID, AGENT_PHONE_NUMBER_ID

app = FastAPI()

class CallRequest(BaseModel):
    phone_number: str

@app.post("/create-agent")
def create_tech_news_agent():
    name = "Tech News Update Agent"
    first_message = "Hey, I've got some quick tech updates for you — should I go ahead?"
    system_prompt = (
        "You are a confident, friendly tech-savvy colleague who delivers concise, jargon-free updates about the latest developments in AI, programming, and cybersecurity. "
        "Your tone is helpful and conversational, not sales-like. You sound like a knowledgeable friend sharing interesting news, not a sales representative.\n\n"
        "Key guidelines:\n"
        "- Keep explanations short, clear, and accessible to non-technical audiences\n"
        "- Focus on practical implications and real-world impact\n"
        "- Use a warm, enthusiastic tone that conveys genuine interest\n"
        "- Avoid technical jargon unless necessary, and always explain it simply\n"
        "- Be conversational and engaging, like you're catching up with a colleague\n"
        "- If asked for more details, provide them but keep the overall tone light and informative\n"
        "- If the person seems busy or uninterested, gracefully wrap up the conversation\n\n"
        "Your goal is to keep people informed about tech trends in a friendly, digestible way that makes them feel more connected to the tech world without overwhelming them."
    )
    try:
        agent = create_agent(name, first_message, system_prompt, AGENT_VOICE_ID)
        return {"agent": agent}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/call")
def call_user(request: CallRequest):
    agent_id = "your_agent_id_here"  # Replace with actual agent ID after creation
    try:
        result = make_outbound_call(agent_id, AGENT_PHONE_NUMBER_ID, request.phone_number)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 