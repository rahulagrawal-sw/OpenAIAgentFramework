import json
from agents import Agent
from agents.tool import WebSearchTool
import asyncio
from src.constants import GPT_MODEL
from src.financeagent.finanance_agent_response import recommendation_result

FINANCE_AGENT_INSTRUCTIONS = """
    You are a Finance Analyst
    Your job is to do a market research and present ONLY top 2-3 companies for investments
    Just provide clear and concsie summary for each stock in 2 sentences
    DO NOT SEARCH MORE THAN 3 COMPANIES
"""

finance_agent = Agent(
    name = "RA Finance Agent",
    model = GPT_MODEL,
    instructions=FINANCE_AGENT_INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    output_type=recommendation_result
)