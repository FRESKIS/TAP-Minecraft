from abc import ABC, abstractmethod
import asyncio
from support.States import state


class BaseAgent(ABC):
    def __init__(self, agent_id, bus):
        self.agent_id = agent_id
        self.bus = bus
        self.state = state.IDLE

    @abstractmethod
    async def perceive(self):
        pass

    @abstractmethod
    async def decide(self):
        pass

    @abstractmethod    
    async def act(self):
        pass

    async def run(self):
        self.state = state.RUNNING
        while self.state not in {state.STOPPED, state.ERROR}:
            # Wait if the agent is paused, waiting, or idle
            if self.state in {state.PAUSED, state.WAITING, state.IDLE}:
                await asyncio.sleep(0.1)
                continue

            if self.state != state.RUNNING:         #If it changed state during perceive, skip to next loop
                continue            
            await self.perceive()
            if self.state != state.RUNNING:         #If it changed state during perceive, skip to next loop
                continue
            await self.decide()
            if self.state != state.RUNNING:         #If it changed state during decide, skip to next loop    
                continue
            await self.act()
            if self.state != state.RUNNING:
                continue
            await asyncio.sleep(0.1)                # Small delay to prevent async tight loop

