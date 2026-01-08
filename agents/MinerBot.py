from agents.BaseAgent import BaseAgent
from commands.commands import MinerCommand
from support.States import state
from support.strategies import vertical, Layer
import json
from support.JSONMessageHandeler import JSONMessageHandeler

class MinerBot(BaseAgent, MinerCommand):
    context : dict = {}
    plan_list: str = []
    bom: dict = {}
    strategy = vertical

    def __init__(self, agent_id, bus : json, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)

    async def perceive(self):
        instructions = JSONMessageHandeler.to_json(self.bus)

        pass

    async def decide(self):
        if self.state == state.RUNNING:
            self._next_action = "mine"
        elif self.state == state.PAUSED:
            self._next_action = None

    async def act(self):
        if self._next_action == "mine":
            await self.mine_materials()

    async def mine_materials(self):
        
        pass

    async def save_context(self):
        # Guardar estado de la minería, si es necesario
        pass

    async def response(self):
        msg = JSONMessageHandeler.from_json(self.queue)
        if msg["type"] == "map.v1":
            pass
        if msg["type"] == "materials.requirements.v1":
            pass


