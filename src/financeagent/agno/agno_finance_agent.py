from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.webtools import WebTools
from agno.models.openai import OpenAIChat
from agno.knowledge.knowledge import Knowledge

from src.financeagent.agno.agno_const import agno_finance_agent_instructions
from src.constants import GPT_MODEL

# Initialize the AI investment analyst agent with comprehensive tools and instructions
agno_finance_agent = Agent(
    name="Personal Accountant",
    description=(
        "You are an investment analyst that researches stock prices, "
        "analyst recommendations, and stock fundamentals."
    ),
    instructions=agno_finance_agent_instructions,
    model=OpenAIChat(id=GPT_MODEL),
    db=SqliteDb(db_file="personal_accountant.db"),
    add_history_to_context=True,
    enable_agentic_memory=True,
    tools=[
        ReasoningTools(
            add_instructions=True,
            enable_think=True,
            enable_analyze=True,
        ),
        YFinanceTools(
            cache_dir="./yfinance_cache",
            cache_results=True,
        ),
        WebTools(),
    ],
    add_datetime_to_context=True,
    timezone_identifier="Asia/Kolkata",
    cache_session=True,
    markdown=True,
    telemetry=True
)