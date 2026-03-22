from pydantic import BaseModel


class company_fundamentals(BaseModel):
    """
        This is a Structured response of company information like company_name, why it's selected by agent, 
        and fundamentals like valuations, P&L, etc.
    """
    company_name: str
    key_findings: list[str]
    sources: list[str]


class recommendation_result(BaseModel):
    recommendations: list[company_fundamentals]