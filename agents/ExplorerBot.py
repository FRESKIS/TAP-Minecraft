import asyncio
from agents.BaseAgent import BaseAgent 
from commands.commands import ExplorerCommand
from mcpi import block
from support.States import state
import uuid

class ExplorerBot(BaseAgent, ExplorerCommand):
    context : list[dict] = [{"expedition_id": "", "explored_area": [{"x": int, "z": int, "area": int}], "height_maps": [], "state": str, "progress": {"x": int, "z": int}}]

    def __init__(self, agent_id, bus, mc):
        BaseAgent.__init__(self, agent_id, bus, mc)
        self.stop = asyncio.Event()
        self.wait = asyncio.Event().set()

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
        expedition_id = str(uuid.uuid4())
        i = x
        j = z
        while i < x + area_size and not self.stop.is_set():
            while j < z + area_size and not self.stop.is_set():
                self.wait.wait()
                await higth_map[i][j] = {"x": x + i, "z": j + z, "height": self.mc.getHeight(x + i, z + j)}
                await self.mc.setBlock(i, higth_map[i][j]["height"], j, block.SAPLING.id)  # Place glass block at the height
                j += 1
            i += 1
        if not self.stop.is_set():
            await self.context.append({"expedition_id": expedition_id, "explored_area": [{"x": x, "z": z, "area": area_size}], "height_maps": higth_map, "state": "COMPLETED"})
            return higth_map
        else:
            await self.safe_exploration(expedition_id, i, j)
    
    async def safe_exploration(self, expedition, i, j):
        for k in self.context:
            if k["expedition_id"] == expedition:
                k["state"] = "PAUSED"
                k["progress"] = {"x": i, "z": j}
        self.state = state.IDLE

        
        
