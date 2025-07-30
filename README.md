# ElevenLabs MCP Integration - Tech News Update Agent

A FastAPI backend to create an ElevenLabs agent that makes outbound calls to deliver friendly, jargon-free tech news updates. This project demonstrates the integration of ElevenLabs MCP (Model Context Protocol) for creating conversational AI agents with voice capabilities.

## 🚀 Features

- **Conversational AI Agent**: Creates a confident, friendly tech-savvy colleague
- **Voice Integration**: Uses ElevenLabs Alice voice for natural-sounding calls
- **Tech News Delivery**: Provides updates about AI, programming, and cybersecurity
- **Simple API**: Easy-to-use endpoints for agent creation and call management
- **MCP Integration**: Leverages ElevenLabs MCP for seamless agent management

## 📁 Project Structure

```
ElevenLabs/
├── app/
│   ├── main.py              # FastAPI application with endpoints
│   ├── elevenlabs_client.py # ElevenLabs API client functions
│   └── config.py            # Configuration and environment variables
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## 🛠️ Setup

### Prerequisites

- Python 3.8+
- ElevenLabs API key
- ElevenLabs phone number (for outbound calls)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LEKKALAGANESH/Eleven-Labs-MCP-Integration.git
   cd Eleven-abs-MCP-Integration
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_BASE_URL=https://api.elevenlabs.io/v1
AGENT_VOICE_ID=Xb7hH8MSUJpSbSDYk0k2
AGENT_PHONE_NUMBER_ID=your_phone_number_id
```

## 📡 API Endpoints

### 1. Create Agent
**POST** `/create-agent`

Creates a new Tech News Update Agent with predefined personality and voice.

**Response:**
```json
{
  "agent": {
    "agent_id": "agent_5701k1capwtse9fske3xgefspyra",
    "name": "Tech News Update Agent",
    "voice_id": "Xb7hH8MSUJpSbSDYk0k2"
  }
}
```

### 2. Make Outbound Call
**POST** `/call`

Initiates an outbound call to the specified phone number.

**Request Body:**
```json
{
  "phone_number": "+1234567890"
}
```

**Response:**
```json
{
  "result": {
    "conversation_id": "conv_3401k1casackffe9emj08wgf9zsd",
    "call_sid": "CA12265951d92ca816f1f15693d7efd6a2",
    "status": "success"
  }
}
```

## 🎯 Usage Examples

### Using curl

1. **Create the agent:**
   ```bash
   curl -X POST "http://localhost:8000/create-agent"
   ```

2. **Make a call:**
   ```bash
   curl -X POST "http://localhost:8000/call" \
        -H "Content-Type: application/json" \
        -d '{"phone_number": "+1234567890"}'
   ```

### Using Python requests

```python
import requests

# Create agent
response = requests.post("http://localhost:8000/create-agent")
agent_data = response.json()
agent_id = agent_data["agent"]["agent_id"]

# Make call
call_data = {"phone_number": "+1234567890"}
response = requests.post("http://localhost:8000/call", json=call_data)
print(response.json())
```

## 🤖 Agent Personality

The Tech News Update Agent is configured with:

- **Tone**: Confident, friendly, and conversational
- **Voice**: Alice (female voice) for natural communication
- **Expertise**: AI, programming, and cybersecurity updates
- **Style**: Jargon-free explanations with practical implications
- **Approach**: Like a knowledgeable colleague sharing interesting news

## ⚠️ Important Notes

- **Phone Verification**: You must have a verified or paid ElevenLabs/Twilio account to call unverified numbers
- **Agent ID**: After creating the agent, update the `agent_id` in `main.py` with the returned ID
- **API Limits**: Be aware of ElevenLabs API rate limits and usage quotas
- **Environment Variables**: Never commit your actual API keys to version control

## 🔗 Related Links

- [ElevenLabs API Documentation](https://docs.elevenlabs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

**Built with ❤️ using ElevenLabs MCP Integration** 
