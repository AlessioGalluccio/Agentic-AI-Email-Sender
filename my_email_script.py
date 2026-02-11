import os
from agentmail import AgentMail
from dotenv import load_dotenv
import markdown

load_dotenv()

def send_email(subject, body):
    # Initialize the client with your API Key
    api_key = os.getenv("AGENTMAIL_API_KEY")
    client = AgentMail(api_key=api_key)

    # Note: inbox_id is the email address you set up in the AgentMail dashboard
    inbox_id = os.getenv("AGENTMAIL_INBOX_ID") 
    recipient = os.getenv("RECEIVER_EMAIL")

    # 1. Convert Markdown to HTML
    html_content = markdown.markdown(body)

    # 2. Wrap it in a basic style for better readability
    styled_html = f"""
    <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        {html_content}
    </div>
    """

    try:
        sent_message = client.inboxes.messages.send(
            inbox_id=inbox_id,
            to=recipient,
            subject=subject,
            text=body,
            html=styled_html  # The formatted version
        )
        print(f"✅ Message sent successfully with ID: {sent_message.message_id}")
    except Exception as e:
        print(f"❌ AgentMail Error: {e}")