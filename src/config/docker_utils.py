from src.config.docker import DockerConfig
class DockerUtils:
    def __init__(self,docker):
        self.docker = docker
    
    async def start_docker_container(self):
        print("Starting Docker Container")
        await self.docker.start()
        print("Docker Container Started")

    async def stop_docker_container(self):
        print("Stopping Docker Container")
        await self.docker.stop()
        print("Docker Container Stopped")