from autogen_agentchat.agents import AssistantAgent
from src.models.openai_model import OpenAIModel
from src.config.prompt_loader import PromptLoader
from src.models.groq_model import GroqModel


class SummaryAgent:
    def __init__(self):
        self.model_client = GroqModel().get_groq_model()
        self.system_prompt = PromptLoader().get_prompt("SUMMARY_AGENT")

    def get_agent(self):
        summary_agent = AssistantAgent(
            name="summary_agent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return summary_agent
