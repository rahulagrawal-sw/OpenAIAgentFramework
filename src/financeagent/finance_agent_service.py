import trace
from typing import Any
from src.financeagent.finance_agent import finance_agent
from src.financeagent.finanance_agent_response import recommendation_result
import asyncio

from agents import Runner, gen_trace_id, trace


async def run_finance_agent(input_query: str) -> recommendation_result:
    """ Runa a finance_agent for the input_query """
    input = f"Search term: {input_query}"
    print(f"input_query {input_query}")

    try:
        trace_id = gen_trace_id()
        print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
        with trace("RA Finance Agent trace", trace_id=trace_id):
            result = await Runner.run(
                finance_agent,
                input
            )
            return result.final_output
    except Exception as e:
        print(e)
        return None