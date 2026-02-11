# 🤖 Daily Agentic AI Physical AI Email Recap
An automated AI agent that scours the web for the latest breakthroughs in Physical AI (Robotics, Embodied AI, and Sim-to-Real), summarizes them, and delivers a recap directly to your inbox.

# 🌟 Features
- **Autonomous Research**: Uses a LangChain ReAct agent to perform real-time searches via DuckDuckGo.
- **Smart Summarization**: Powered by Google Gemini (3 Flash) to distill complex technical papers into digestible recaps.
- **Agent-First Delivery**: Integrated with AgentMail for seamless, SMTP-free email delivery.
- **Fully Automated**: Runs every morning via GitHub Actions—no local server required.

# 🛠️ Architecture
The system follows a simple but effective pipeline:
- **Trigger**: GitHub Actions wakes up the script on a cron schedule.
- **Search**: The agent uses DuckDuckGoSearchRun to find articles from the last 24 hours.
- **Process**: Gemini analyzes the findings and formats a report.
- **Send**: The recap is dispatched via the AgentMail SDK to the configured recipient.

# 🚀 Setup & Installation
**1. Clone the repo**
```
git clone https://github.com/AlessioGalluccio/Agentic-AI-Email-Sender.git
cd Agentic-AI-Email-Sender
```
**2. Install Dependencies**
```
pip install -r requirements.txt
```
**3. Environment Variables**
Create a .env file for local testing:
```
GEMINI_API_KEY=your_gemini_key
AGENTMAIL_API_KEY=your_agentmail_key
AGENTMAIL_INBOX_ID=your_inbox_address
RECEIVER_EMAIL=your_email@example.com
```
**4. GitHub Secrets**
For the automation to work, add the variables above to your GitHub Repository under Settings > Secrets and variables > Actions.

# **📅 Automation Schedule**
The bot is currently configured to run daily at 10:00 UTC. You can modify the frequency in .github/workflows/main.yml.

# **🧰 Tech Stack**
- **LLM: Google Gemini 3 Flash**
- **Orchestration: LangChain**
- **Email: AgentMail**
- **Automation: GitHub Actions**
