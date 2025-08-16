from autogen_agentchat.agents import AssistantAgent
from src.config.prompt_loader import PromptLoader
from src.models.openai_model import OpenAIModel
from src.models.groq_model import GroqModel
from src.tools.JSearch import JSearch
from autogen_core.tools import FunctionTool


class JobDescriptionAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("JOB_DESCRIPTION_AGENT")
        self.jsearch = FunctionTool(
        func=JSearch().JSearchAPI,
        name="JSearch_API",
        description="The tool searches for job based on the query"
    )

        # Initialize model client
        self.model_client = OpenAIModel().get_openai_model()

    def get_agent(self):
        job_description_agent =  AssistantAgent(
            name="job_description_agent",
            model_client=self.model_client,
            system_message=self.system_prompt,
            tools=[self.jsearch],
            reflect_on_tool_use=True
        )
        return job_description_agent
























