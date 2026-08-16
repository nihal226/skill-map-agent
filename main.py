import os
import requests

from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch


load_dotenv()

rapid_api_key = os.getenv("RAPID_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")


# ---------------- LLM ----------------

model = init_chat_model(
    model="google_genai:gemini-2.5-flash",
    api_key=gemini_api_key
)


# ---------------- TOOL 1: JOB SEARCH ----------------

@tool
def search_jobs(skill: str, location: str) -> list:
    """
    Search for jobs based on a skill and location.
    """

    url = "https://jsearch.p.rapidapi.com/search-v2"

    querystring = {
        "query": f"{skill} jobs in {location}",
        "page": "1",
        "num_pages": "1",
        "country": "in",
        "date_posted": "all",
        "employment_types": "FULLTIME,INTERN",
        "job_requirements": "no_experience"
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    response.raise_for_status()

    data = response.json()

    jobs = data.get("data", [])

    return jobs


# ---------------- TOOL 2: TAVILY ----------------

skill_demand_tool = TavilySearch(
    max_results=5,
    topic="general",
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)


# ---------------- AGENT ----------------

agent = create_agent(
    model=model,
    tools=[skill_demand_tool, search_jobs],
    system_prompt="""
    You are a helpful career assistant.

    Use search_jobs when the user asks to find jobs or internships.

    Use the web search tool when the user asks about current skills,
    technologies, industry trends, or other information requiring
    web research.
    """
)
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find developer jobs in Pune"
        }
    ]
})

print(response["messages"][-1].content)