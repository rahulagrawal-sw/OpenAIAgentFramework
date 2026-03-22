from agno.agent import RunOutput
from agno.utils.pprint import pprint_run_response

from fastapi import APIRouter, Query
from typing import Optional
import asyncio

from src.financeagent.agno.agno_finance_agent import agno_finance_agent

run_agno_finance_agent_router = APIRouter(tags=["run_agents"])


@run_agno_finance_agent_router.get("/run/agno_finance_agent")
def run_agno_finance_agent_api(input_query: Optional[str]):

    input_query = "Analyze the NSE India top 5 stocks to suggest the investment options with top 2 stocks"

    agent_output: RunOutput = agno_finance_agent.run(input_query)
    pprint_run_response(agent_output, markdown=True)

    return {
        "status": "ok", 
        "message": "Run run_finance_agent is completed", 
        "agent_output": agent_output.model_dump()
    }
    