from autogen_ext.models.openai import OpenAIChatCompletionClient
from src.config.constant import OPENAI_MODEL,OPENAI_API_KEY
from src.config.structure_schema import ResumeParser,JobDescriptionList,ImprovementRecommendations
class OpenAIModel:
    def __init__(self):
        self.model = OPENAI_MODEL
        self.api_key = OPENAI_API_KEY

    def get_openai_model(self):
        model = OpenAIChatCompletionClient(
            model=self.model,
            api_key=self.api_key
        )
        return model
    
    def structure_openai_output(self):
        model = OpenAIChatCompletionClient(
            model=self.model,
            api_key=self.api_key,
            response_format=ResumeParser
        )
        return model
    
    def structure_job_description(self):
        model = OpenAIChatCompletionClient(
            model=self.model,
            api_key=self.api_key,
            response_format=JobDescriptionList
        )
        return model

    def structure_improvement_recommendations(self):
        model = OpenAIChatCompletionClient(
            model=self.model,
            api_key=self.api_key,
            response_format=ImprovementRecommendations
        )
        return model