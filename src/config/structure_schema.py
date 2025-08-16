from pydantic import BaseModel,Field
from typing import List,Dict,Optional,Literal

class ResumeParser(BaseModel):
    """Parse key resume fields from text"""

    file_type : Optional[str] = Field(None,description="File type of the resume.")

    name : Optional[str] = Field(None,description="Full name of the candidate.")

    contact : Optional[Dict[str,Optional[str]]] = Field(
        None,
        description="Contact information with email and phone."
    )
    skills : List[str] = Field(
        default_factory=list,
        description="List of skills mentioned in the resume.",
    )
    experience : List[str] = Field(
        default_factory=list,
        description="List of work experience mentioned in the resume.",
    )
    education : List[str] = Field(
        default_factory=list,
        description="List of education mentioned in the resume.",
    )
    certifications : List[str] = Field(
        default_factory=list,
        description="List of certifications mentioned in the resume.",
    )


class JobDescriptionData(BaseModel):
    """Schema for a single job description entry."""
    
    role: str = Field(..., description="Job title or position name.")
    
    required_skills: List[str] = Field(
        default_factory=list,
        description="List of essential skills required for this role."
    )
    
    required_experience: Optional[str] = Field(
        None,
        description="Experience required for this role (e.g., '3+ years in Python development')."
    )
    
    required_education: Optional[str] = Field(
        None,
        description="Minimum education requirement for the role."
    )
    
    keywords: List[str] = Field(
        default_factory=list,
        description="Important keywords extracted from the job description."
    )
    
    description_text: Optional[str] = Field(
        None,
        description="Full textual job description."
    )
    
    job_employment_type: Optional[
        Literal["Full-time", "Part-time", "Contract", "Internship", "Remote", "Hybrid", "Onsite"]
    ] = Field(
        None,
        description="Employment type for this role."
    )
    
    job_country: Optional[str] = Field(
        None,
        description="Country where the job is located."
    )

    job_apply_link : Optional[str] = Field(
        None,
        description="Link to apply for the job."
    )

class JobDescriptionList(BaseModel):
    """Schema for a collection of job descriptions."""
    
    jobs: List[JobDescriptionData] = Field(
        default_factory=list,
        description="List of job descriptions the candidate can apply for."
    )
    

class ImprovementRecommendations(BaseModel):
    """Schema for ATS improvement suggestions."""

    missing_keywords : List[str] = Field(default_factory=list,
    description="List of important keywords missing from the resume.")

    skill_gaps : List[str] = Field(default_factory=list,
    description="List of skills required by the job but missing from the resume.")

    format_recommendations : List[str] = Field(default_factory=list,
    description="Suggestions for improving resume formatting for ATS parsing.")

    content_optimization : List[str] = Field(default_factory=list,
    description="Suggestions for rewriting or restructuring content.")

    priority_actions: List[str] = Field(default_factory=list, description="Top 3 priority actions to improve score the most.")