from agents.BaseAgent import BaseAgent 
from commands.commands import explorer

class ExplorerBot(BaseAgent, explorer):
    planlist : str = []
    bom : dict = {}

    def __init__(self, agent_id, bus):
        BaseAgent.__init__(self, agent_id, bus)


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