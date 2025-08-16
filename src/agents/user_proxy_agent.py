from autogen_agentchat.agents import UserProxyAgent

class UserAgent:
    def get_agent(self):
        model = UserProxyAgent(
            name="user_agent",
            input_func=input("Enter your email"),
        )
        return model
