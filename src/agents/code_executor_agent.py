from autogen_agentchat.agents import CodeExecutorAgent
from src.config.docker import DockerConfig


class CodeExecutor:
    def __init__(self):
        self.docker_executor = DockerConfig().get_docker_executor()

    def get_agent(self):

        code_executor_agent = CodeExecutorAgent(
            name="Code_Executor_Agent",
            code_executor=self.docker_executor
        )
        return code_executor_agent,self.docker_executor
