from agents.BaseAgent import BaseAgent 
from commands.commands import MinerCommand

class MinerBot(BaseAgent, MinerCommand):
    planlist : str = []
    bom : dict = {}

    def __init__(self, agent_id, bus, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)


    def decide(self):
        pass

    def perceive(self):
        pass

    async def act(self):
        # Implementation of the BuilderBot's actions
        pass

    async def save_context(self):
        # Implementation of context saving for BuilderBot
        pass