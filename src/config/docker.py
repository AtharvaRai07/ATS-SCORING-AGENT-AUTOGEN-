from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from src.config.constant import WORK_DIR,TIMEOUT

class DockerConfig:
    @staticmethod
    def get_docker_executor():
        docker = DockerCommandLineCodeExecutor(
            image="python-with-matplotlib-and-seaborn",
            work_dir=WORK_DIR,
            timeout=TIMEOUT
        )
        return docker