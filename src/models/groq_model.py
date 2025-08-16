from autogen_ext.models.openai import OpenAIChatCompletionClient
from src.config.constant import GROQ_MODEL,GROQ_API_KEY
from src.config.structure_schema import ResumeParser,JobDescriptionList,ImprovementRecommendations

class GroqModel:
    def __init__(self):
        self.model = GROQ_MODEL
        self.api_key = GROQ_API_KEY
    
    def get_groq_model(self):
        model = OpenAIChatCompletionClient(
            base_url="https://api.groq.com/openai/v1", 
            model=self.model, 
            api_key=self.api_key, 
            model_info={
                "family": "groq",
                "vision": False, 
                "function_calling": True,
                "json_output": False,
                "multiple_system_messages":True
            }
        ) 
        return model
    
    def structure_groq_output(self):
        model = OpenAIChatCompletionClient(
    base_url="https://api.groq.com/openai/v1", 
    model=self.model, 
    api_key=self.api_key, 
    model_info={
        "family": "groq",
        "vision": False, 
        "function_calling": True,
        "json_output": False,
        "structured_output": ResumeParser
        }
     ) 
        return model
    
    def structure_job_description(self):
        model = OpenAIChatCompletionClient(
    base_url="https://api.groq.com/openai/v1", 
    model=self.model, 
    api_key=self.api_key, 
    model_info={
        "family": "groq",
        "vision": False, 
        "function_calling": True,
        "json_output": False,
        "structured_output": JobDescriptionList
        }
     ) 
        return model

    def structure_improvement_recommendations(self):
        model = OpenAIChatCompletionClient(
    base_url="https://api.groq.com/openai/v1", 
    model=self.model, 
    api_key=self.api_key, 
    model_info={
        "family": "groq",
        "vision": False, 
        "function_calling": True,
        "json_output": False,
        "structured_output": ImprovementRecommendations
        }
     ) 
        return model

    def rag_agent_groq(self):
        model = OpenAIChatCompletionClient(
    base_url="https://api.groq.com/openai/v1", 
    model=self.model, 
    api_key=self.api_key, 
    model_info={
        "family": "groq",
        "vision": False, 
        "function_calling": True,
        "json_output": False,
        "multiple_system_messages":True
        }
     ) 
        return model