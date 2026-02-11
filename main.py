from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from my_email_script import send_email
from datetime import datetime

load_dotenv()

# Define tools
search_tool = DuckDuckGoSearchRun()
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# Create the agent
app = create_agent(model, tools=[search_tool])

today_str = datetime.now().strftime("%Y-%m-%d")

# Run the agent once and collect the readable AI text
final_answer = ""

inputs = {"messages": [("user", f"Find 3 interesting technical articles in Physical AI from today (which is {today_str}). Recap them in a few sentences, include links to the article.")]}

for output in app.stream(inputs):
    # Only print AI text messages
    if "model" in output and "messages" in output["model"]:
        for msg in output["model"]["messages"]:
            if msg.content:
                for c in msg.content:
                    if "text" in c:
                        text = c["text"]
                        print(text)
                        final_answer += text + "\n\n"  # accumulate for email


# Send email if we got any text
if final_answer:
    send_email(
        subject=f"Daily Physical AI Recap - {today_str}",
        body=final_answer
    )
