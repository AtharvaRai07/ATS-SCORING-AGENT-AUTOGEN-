from autogen_agentchat.agents import AssistantAgent
from src.models.openai_model import OpenAIModel
from src.config.prompt_loader import PromptLoader
from src.models.groq_model import GroqModel


class TextExtractorAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("EXTRACTOR_AGENT")

        # Initialize model client
        self.model_client = GroqModel().structure_groq_output()

    def get_agent(self):
        text_extractor =  AssistantAgent(
            name="text_extractor_agent",
            model_client=self.model_client,
            system_message=self.system_prompt,
        )
        return text_extractor
