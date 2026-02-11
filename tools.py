from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool # Modern decorator
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

# Initialize search globally
search = DuckDuckGoSearchRun()

@tool
def save_tool(data: str):
    """Saves the lead information and outreach messages to a local text file."""
    filename = "leads_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Leads Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

def scrape_website(url: str) -> str:
    """Internal helper to scrape HTML."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        return re.sub(r'\s+', ' ', text)[:5000]
    except Exception as e:
        return f"Error scraping website: {e}"

@tool
def scrape_tool(company_name: str):
    """
    Finds IT-related information for a specific company by searching and 
    scraping relevant web results.
    """
    queries = [f"{company_name} IT Services", f"{company_name} contact info"]
    results = []

    for query in queries:
        search_results = search.run(query)
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', search_results)
        if urls:
            results.append(scrape_website(urls[0]))

    return " ".join(results)

@tool
def search_tool(query: str):
    """Search the web for general information, companies, or local businesses."""
    return search.run(query)