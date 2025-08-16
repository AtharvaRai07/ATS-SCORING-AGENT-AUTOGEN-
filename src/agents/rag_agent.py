from autogen_agentchat.agents import AssistantAgent
from src.models.openai_model import OpenAIModel
from src.config.prompt_loader import PromptLoader
from src.tools.memory_tool import MemoryTool
from src.models.groq_model import GroqModel

class RAGAgent:
    def __init__(self):
        # Load system prompt
        self.prompt_loader = PromptLoader()
        self.system_prompt = self.prompt_loader.get_prompt("RAG_AGENT")
        self.memory = MemoryTool().get_memory()

        # Initialize model client
        self.model_client = GroqModel().rag_agent_groq()

    def get_agent(self):
        rag_agent =  AssistantAgent(
            name="rag_agent",
            model_client=self.model_client,
            system_message=self.system_prompt,
            memory=[self.memory]
        )
        return rag_agent

