from autogen_agentchat.agents import AssistantAgent
from src.models.openai_model import OpenAIModel
from src.config.prompt_loader import PromptLoader
from src.models.groq_model import GroqModel


class VisualizationAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("VISUALIZATION_AGENT")

        # Initialize model client
        self.model_client = GroqModel().get_groq_model()

    def get_agent(self):
        visualization_agent =  AssistantAgent(
            name="visualization_agent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return visualization_agent
