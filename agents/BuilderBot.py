from agents.BaseAgent import BaseAgent 
from buildings.constructor import constructor
from commands.commands import BuilderCommand

class BuilderBot(BaseAgent, BuilderCommand):
    context : dict = {}
    plan_list : list = []

    def __init__(self, agent_id, bus, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)

    async def perceive(self):
        pass

    async def decide(self):
        pass

    async def act(self):
        if not self.plan_list:
            await self.answer_to_chat("No plans to build.")
            return
        else:    
            constructor.build(self.mc, self.mc.player.getTilePos(), self.plan_list[0]["name"])
            self.plan_list.pop(0)
            # Implementation of the BuilderBot's actions
            pass

    async def save_context(self):
        # Implementation of context saving for BuilderBot
        pass

    async def response(self):
        pass