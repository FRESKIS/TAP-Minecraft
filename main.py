import asyncio
import inspect
from mcpi.minecraft import Minecraft
from mcpi import block
from buildings.constructor import constructor
from commands.commands import parse_message
from agents.BaseAgent import BaseAgent
from support import registry

discovered_agents = registry.discover_agents()

mc = Minecraft.create()
pos = mc.player.getTilePos()

builder_bot = discovered_agents["BuilderBot"]("builder", None, mc)
miner_bot = discovered_agents["MinerBot"]("miner", None, mc)
explorer_bot = discovered_agents["ExplorerBot"]("explorer", None, mc)

agents : dict[str, BaseAgent] = {
    "builder": builder_bot
    ,"miner": miner_bot
    ,"explorer": explorer_bot
}

async def dispatch_command(agent, command: str, args: list[str]):
    fn = getattr(agent, command)
    if args:
        res = fn(", ".join(args))
    else:
        res = fn()

    if inspect.isawaitable(res):
        await res
    else:
        res

async def main():
    while True:
        chatEvents = mc.events.pollChatPosts()
        if chatEvents:
            for chatEvent in chatEvents:
                if chatEvent.message.startswith("!"):
                    msg = parse_message(chatEvent.message)
                    if isinstance(msg, dict):
                        if msg["command"] in dir(agents[msg["agent"]]):
                            asyncio.create_task(dispatch_command(msg["agent"], msg["command"], msg["args"]))
                        else:
                            mc.postToChat(f"//Command '{msg['command']}' not found for agent '{msg['agent']}'")
                    else:
                        mc.postToChat("//" + str(msg))
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())