from autogen_agentchat.agents import AssistantAgent
from src.config.prompt_loader import PromptLoader
from src.models.openai_model import OpenAIModel
from src.models.groq_model import GroqModel


class ImprovementAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("IMPROVEMENT_AGENT")

        # Initialize model client
        self.model_client = GroqModel().get_groq_model()

    def get_agent(self):
        improvement_agent =  AssistantAgent(
            name="improvement_agent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return improvement_agent



























from autogen_agentchat.agents import AssistantAgent
from src.config.prompt_loader import PromptLoader
from src.models.openai_model import OpenAIModel
from src.models.groq_model import GroqModel

class JobDescriptionAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("JOB_DESCRIPTION_AGENT")

        # Initialize model client
        self.model_client = GroqModel().structure_job_description()

    def get_agent(self):
        job_description_agent =  AssistantAgent(
            name="job_description_agent",
            model_client=self.model_client,
            system_message=self.system_prompt
        )
        return job_description_agent

