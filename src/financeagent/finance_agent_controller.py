import json
from agents import agent_output
from fastapi import APIRouter, Query
from typing import Optional
import asyncio
import pydantic

from src.financeagent.finance_agent_service import run_finance_agent

run_finance_agent_router = APIRouter(tags=["run_agents"])


@run_finance_agent_router.get("/run/finance_agent")
async def run_search_agent_api(input_query: Optional[str]):
    """Run run_search_agent_router endpoint."""
    agent_output = await run_finance_agent(input_query)
    return {
        "status": "ok", 
        "message": "Run run_finance_agent is completed", 
        "agent_output": agent_output.model_dump()
    }
    