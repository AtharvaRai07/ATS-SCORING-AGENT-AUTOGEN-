from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from src.agents.code_executor_agent import CodeExecutor
from src.agents.rag_agent import RAGAgent
from src.agents.visualization_agent import VisualizationAgent
from src.agents.ats_scoring_agent import ATS_ScoringAgent
from src.agents.job_description_agent import JobDescriptionAgent
from src.agents.text_extractor import TextExtractorAgent
from src.agents.summary_agent import SummaryAgent 
from src.agents.improvement_agent import ImprovementAgent 
from src.config.constant import TERMINATION, MAX_TURNS


class ATSAgentTeam:
    def __init__(self):
        # Initialize all agents
        self.extract_text = TextExtractorAgent().get_agent()
        self.job_description_agent = JobDescriptionAgent().get_agent()
        self.ats_scoring_agent = ATS_ScoringAgent().get_agent()
        self.rag_agent = RAGAgent().get_agent()
        self.visualization_agent = VisualizationAgent().get_agent()
        self.code_executor_agent,self.docker = CodeExecutor().get_agent()
        self.summary_agent = SummaryAgent().get_agent()
        self.improvement_agent = ImprovementAgent().get_agent()

        # Create the team
        self.team = RoundRobinGroupChat(
            participants=[
                self.extract_text,
                self.job_description_agent,
                self.ats_scoring_agent,
                self.improvement_agent,
                self.rag_agent,
                self.visualization_agent,
                self.code_executor_agent,
                self.summary_agent,
            ],
            termination_condition=TextMentionTermination(TERMINATION),
            max_turns=MAX_TURNS
        )

    def get_team(self):
        return self.team,self.docker
        
