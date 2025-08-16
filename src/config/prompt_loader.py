import yaml
import os 

class PromptLoader:
    def __init__(self,prompt_path: str = "./src/config/system_messages.yaml"):
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.prompts = yaml.safe_load(f)

    def get_prompt(self,key:str):
        return self.prompts.get(key,"")