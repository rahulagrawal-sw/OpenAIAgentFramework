from fastapi import APIRouter, Query
from typing import Optional
import asyncio
from agents import Runner, trace, gen_trace_id
from ..research.search_agent import search_agent

router = APIRouter(prefix="/run", tags=["run"])
run_search_agent_router = APIRouter(tags=["run_agents"])


@router.get("/")
def run():
    """Run endpoint."""
    return {"status": "ok", "message": "Run completed"}


@run_search_agent_router.get("/run/search_agent")
async def run_search_agent_api(input_query: Optional[str] = Query(
        None, 
        min_length=3, 
        max_length=100, 
        regex="^[a-zA-Z0-9 ]*$",  # Only alphanumeric and spaces
        description="Search query string"
    )):
    # Method body starts below
    """Run run_search_agent_router endpoint."""
    agent_output = await run_search_agent(input_query)
    return {"status": "ok", "message": "Run run_search_agent is completed", "agent_output": agent_output}
    

async def run_search_agent(input_query: str):
    """ Perform a search for the query """
    input = f"Search term: {input_query}"
    try:
        trace_id = gen_trace_id()
        print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
        with trace("RA Search Agent trace", trace_id=trace_id):
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
    except Exception:
        return None