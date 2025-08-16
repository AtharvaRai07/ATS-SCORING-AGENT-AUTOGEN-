from autogen_agentchat.agents import AssistantAgent
from src.models.openai_model import OpenAIModel
from src.config.prompt_loader import PromptLoader
from src.models.groq_model import GroqModel

class ATS_ScoringAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("ATS_SCORING_AGENT")

        # Initialize model client
        self.model_client = GroqModel().get_groq_model()

    def get_agent(self):
        ats_scoring =  AssistantAgent(
            name="ats_scoring_agent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return ats_scoring

















