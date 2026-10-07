from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class RiskEntity(BaseModel):
    """
    Defines the exact structure required for an individual or company 
    flagged during a Vcheck corporate compliance background screening.
    """
    
    entity_name: str = Field(
        ..., 
        description="The full official name of the individual person or corporate company being screened."
    )
    
    entity_type: Literal["Individual", "Company", "Unknown"] = Field(
        ...,
        description="The classified category of the legal entity."
    )
    
    risk_category: Literal["Fraud", "Regulatory Failure", "Legal Dispute", "Sanctions Match", "None"] = Field(
        ...,
        description="The primary classification of background or compliance risk detected in the text source."
    )
    
    severity_score: int = Field(
        ...,
        ge=1,  # Minimum value allowed is 1
        le=10, # Maximum value allowed is 10
        description="The calculated severity of the risk, where 1 is minimal and 10 is catastrophic enterprise risk."
    )
    
    verdict_summary: str = Field(
        ...,
        description="A concise, 2-sentence objective technical summary justifying the assigned risk category and score."
    )
    
    source_citations: List[str] = Field(
        default_factory=list,
        description="A list containing exact direct quotes or article names used as evidence to ground this finding."
    )
