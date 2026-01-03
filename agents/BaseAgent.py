from abc import ABC, abstractmethod
import asyncio
from support.States import state


class BaseAgent(ABC):

    def __init__(self, agent_id, bus, mc):
        self.agent_id = agent_id
        self.bus = bus
        self.state = state.IDLE
        self.mc = mc


    @abstractmethod
    async def perceive(self):
        pass

    @abstractmethod
    async def decide(self):
        pass

    @abstractmethod    
    async def act(self):
        pass

    @abstractmethod
    async def save_context(self):
        pass

    async def run(self):
        self.state = state.RUNNING
         
        await self.perceive()

        await self.decide()

        await self.act()

        await asyncio.sleep(0.1)                # Small delay to prevent async tight loop

    async def answer_to_chat(self, message):
        for x in message.splitlines():
            self.mc.postToChat(f"// {x}")
