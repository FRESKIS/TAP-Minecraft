from agents.BaseAgent import BaseAgent 
from buildings.constructor import constructor
from commands.commands import BuilderCommand

class BuilderBot(BaseAgent, BuilderCommand):
    plan_list : dict = {}

    def __init__(self, agent_id, bus, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)

    async def perceive(self):
        pass

    async def decide(self):
        pass

    async def act(self):
        # Implementation of the BuilderBot's actions
        pass

    async def save_context(self):
        # Implementation of context saving for BuilderBot
        pass