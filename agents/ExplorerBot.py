import asyncio
from agents.BaseAgent import BaseAgent 
from commands.commands import ExplorerCommand
from mcpi import block
from support.States import state
from support.JSONMessageHandeler import JSONMessageHandeler
import uuid

class ExplorerBot(BaseAgent, ExplorerCommand):
    context : dict = [{"expedition_id": "", "explored_area": [{"x": int, "z": int, "area": int}], "height_maps": [], "state": str, "progress": {"x": int, "z": int}}]
    tasks : list[dict] = []

    def __init__(self, agent_id, bus, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)
        self.stop = asyncio.Event()
        self.wait = asyncio.Event()
        self.wait.set()

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

    async def explore_area(self, x, z, area_size: int) -> list[list[dict]]:
        higth_map : list[list[dict]] = []
        i = x
        j = z
        while i < x + area_size and not self.stop.is_set():
            while j < z + area_size and not self.stop.is_set():
                await self.wait.wait()
                higth_map[i][j] = {"x": x + i, "z": j + z, "height": self.mc.getHeight(x + i, z + j)}
                self.mc.setBlock(i, higth_map[i][j]["height"], j, block.SAPLING.id)  # Place glass block at the height
                j += 1
            i += 1
        return higth_map

    
    async def safe_exploration(self, expedition, i, j):
        if self.context["expedition_id"] == expedition:
            self.context["state"] = "PAUSED"
            self.context["progress"] = {"x": i, "z": j}
        self.state = state.IDLE

    async def response(self):
        msg = JSONMessageHandeler.from_json(self.queue)
        if msg["type"] == "build.v1":
            pass
        if msg["type"] == "buildingspace.v1":
            exp_id = str(uuid.uuid4()) 
            self.tasks.append({"exploration_id":exp_id, "eplore_area":{"x":msg["payload"]["lenght"], "z":msg["payload"]["width"], "area":msg["payload"]["area"]}})
        
        
