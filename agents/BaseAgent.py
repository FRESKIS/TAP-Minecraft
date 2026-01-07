from abc import ABC, abstractmethod
import asyncio
from support.States import state
from support.MessageBus import MessageBus


class BaseAgent(ABC):

    def __init__(self, agent_id, bus : MessageBus, mc):
        if type(self) is BaseAgent:
            raise TypeError("BaseAgent cannot be instantiated directly")
        self.agent_id = agent_id
        self.bus = bus
        self.queue = self.bus.register_agent(self)
        self.state = state.IDLE
        self.mc = mc
        self.tasks : list[dict] = []


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

    @abstractmethod
    async def response():
        pass

    
    async def run(self):
        self.state = state.RUNNING
        while self.state == state.RUNNING:        
            await self.perceive()
            if self.state not in (state.STOPPED, state.ERROR):
                await self.decide()
            if self.state not in (state.STOPPED, state.ERROR):
                await self.act()
            await asyncio.sleep(0.1)                # Small delay to prevent async tight loop

    async def answer_to_chat(self, message):
        for x in message.splitlines():
            self.mc.postToChat(f"// {x}")
