# 🐂 BullSpace AI — USF Smart Library System

> AI-powered seat finder, reservation system, and study group matcher for USF Tampa Campus Library.

**Live Demo:** [hackusf26-h.onrender.com](https://hackusf26-h.onrender.com)  
**Built at:** HackUSF26 — University of South Florida  
**Team:** Thu · Natalia · Hana · Haneen

---

## 🎯 The Problem

50,000 USF students share one library with no real-time visibility into seat availability. Students walk up to the 3rd floor — no seats. Try the 4th — no seats. Try the 5th — no seats. There's no way to find study partners, no easy way to know when your TA is in the building, and the new 6th floor Bellini AI College confuses students who still go up looking for seats that no longer exist.

**BullSpace AI solves all of this in one place.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Live Dashboard** | Real-time occupancy across all 6 floors with color-coded bars |
| 🗺 **Interactive Seat Map** | Visual map of every seat on floors 1–5. Click to reserve |
| 🎫 **Reservation System** | 2-hour sessions with live countdown timers and up to 2 extensions |
| 📱 **QR Checkout** | Check out manually, automatically, or via QR code kiosk scan |
| 👥 **Study Group Finder** | Post and join study groups by subject, floor, and time |
| 📚 **Tutoring Hub** | 14 real TAs across 8 subjects with filterable weekly schedules |
| 💬 **AI Chat Agent** | Natural language seat recommendations powered by Google ADK |
| 🕐 **Session History** | All your past reservations saved to your browser |
| ♿ **Accessibility Mode** | Larger text and higher contrast toggle |
| 🏛 **Bellini AI College** | 6th floor correctly marked as advising-only |

---

## 🏗 Architecture

```
Student Browser (index.html)
        │
        │  HTTP / fetch
        ▼
FastAPI + Uvicorn (api.py)
        │
        │  Google ADK runner
        ▼
Google ADK 1.28.0 (agent.py)
        │
        │  litellm bridge
        ▼
Groq API — llama-3.1-8b-instant
```
<img width="3142" height="1626" alt="architecture" src="https://github.com/user-attachments/assets/07f3c48c-cdbe-4e90-9c42-a79bef8ed1c0" />

---

## 🛠 Tech Stack

- **AI Framework:** Google ADK 1.28.0
- **AI Model:** Groq llama-3.1-8b-instant (free tier)
- **Backend:** FastAPI + Uvicorn (Python)
- **Frontend:** HTML5 · CSS3 · Vanilla JavaScript
- **Deployment:** Render.com (auto-deploy on push)
- **Storage:** localStorage (session history)
- **QR Codes:** Canvas API (browser-side generation)
- **Fonts:** Space Grotesk · JetBrains Mono

---

## 📁 Project Structure

```
HackUSF26/
├── main.py           ← terminal chat entry point
├── agent.py          ← root_agent (LlmAgent, knowledge-in-prompt)
├── api.py            ← FastAPI server (/health, /chat, /)
├── index.html        ← full frontend (all 7 tabs)
├── .env              ← API keys (never committed)
├── requirements.txt  ← Python dependencies
├── agents/           ← multi-agent architecture (future use)
├── tools/            ← seat and navigation tools (future use)
└── data/
    └── floors.py     ← USF floor seat definitions
```

---

## 🚀 Run Locally

**1. Clone the repo:**
```bash
git clone https://github.com/BombSquad-813/HackUSF26.git
cd HackUSF26
```

**2. Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file:**
```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

Get a free Groq API key at [console.groq.com](https://console.groq.com)

**5. Run the web server:**
```bash
uvicorn api:app --reload
```

Open [http://localhost:8000](http://localhost:8000)

**6. Or run the terminal chat:**
```bash
python main.py
```

---

## 🌐 Deployment

Deployed on **Render.com** with auto-deploy on every GitHub push.

**Build command:** `pip install -r requirements.txt`  
**Start command:** `uvicorn api:app --host 0.0.0.0 --port $PORT`

**Environment variables on Render:**
- `GROQ_API_KEY` — your Groq API key
- `GOOGLE_GENAI_USE_VERTEXAI` — set to `FALSE`

---

## 🏛 USF Library Floors

| Floor | Noise Level | Key Zones |
|---|---|---|
| 1st Floor | Casual | Learning Commons, Computer Lab, VizLab, Starbucks |
| 2nd Floor | Moderate | Smart Lab, Tutoring Hub, Writing Center, Career Cube |
| 3rd Floor | Low-moderate | West Carrels 305–331, East Carrels 335–357, Reading Tables |
| 4th Floor | Low-moderate | West Carrels 440–455, East Carrels 426–437, Special Collections |
| 5th Floor | Quiet only | Reading Rooms 514A–D, 520A–D, Graduate Reading Room |
| 6th Floor | — | Bellini AI College (advising only — no student seats) |

**Library Hours:** Mon–Thu 7am–2am · Fri 7am–8pm · Sat 10am–10pm · Sun 10am–8pm

---

## 🤖 AI Agent

BullSpace AI uses **Google ADK 1.28.0** with a single `LlmAgent` and all USF library knowledge embedded directly in the system prompt. This knowledge-in-prompt approach proved more reliable than tool calling for a fixed dataset.

```python
from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    name="bullspace_ai",
    model="groq/llama-3.1-8b-instant",
    tools=[],
    instruction="... all USF floor data, directions, hours embedded here ..."
)
```

---

## 📚 Tutoring Hub

14 TAs across 8 subjects available in the library:

| Subject | Location |
|---|---|
| Mathematics | Tutoring Hub, 2nd Floor |
| Chemistry | Tutoring Hub, 2nd Floor |
| Physics | Tutoring Hub, 2nd Floor |
| Biology | Tutoring Hub, 2nd Floor |
| Writing | Writing Center, 2nd Floor |
| Computer Science | Smart Lab, 2nd Floor |
| Economics | Tutoring Hub, 2nd Floor |
| Statistics | Tutoring Hub, 2nd Floor |

---

## 🔮 What's Next

- **USF NetID SSO** — single sign-on for any USF student
- **IoT occupancy sensors** — $8–15/seat pressure pads for automatic real-time detection
- **Firebase Firestore** — cross-device real-time reservation sync
- **Predictive crowd modeling** — knows finals week is busy before it starts
- **Expand to USF St. Pete and Sarasota-Manatee** campuses
- **Mobile app** — React Native or Flutter

---

## ⚠️ Known Limitations

- Seat occupancy is simulated (random on login) — production would use IoT sensors
- Groq free tier has a 6,000 TPM rate limit — wait a few seconds between AI chat messages
- Sessions reset on page refresh (no persistent backend for reservations yet)

---

## 👥 Team

Built in under 24 hours at **HackUSF26** by four USF students — three of us hacking for the very first time.

| Name | Role |
|---|---|
| Haneen | AI backend, FastAPI, deployment, frontend |
| Thu | Frontend, UI design |
| Natalia | Research, data, presentation |
| Hana | Frontend, testing |

---

## 📄 License

Built for HackUSF26. All rights reserved by the BombSquad-813 team.

---

*The next time you walk into the USF library and you're not sure where to sit — open BullSpace AI. Your seat is already waiting. 🐂*
