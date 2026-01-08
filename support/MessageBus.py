import asyncio
import json

class MessageBus:
    def __init__(self):
        self.queues = {}
        self.suscribers = {}

    def register_agent(self, agent) -> asyncio.Queue:
        """Registra un agente y crea una cola para él."""
        queue = asyncio.Queue()
        self.queues[agent.__class__.__name__] = queue
        self.suscribers[agent.__class__.__name__] = agent 
        return queue

    async def send(self, agent_name: str, message: json):
        """Envía un mensaje al agente correspondiente."""
        if agent_name in self.queues:
            await self.queues[agent_name].put(message)
            await self.suscribers[agent_name].response()
        else:
            print(f"Agent {agent_name} not registered.")
