from mcpi.minecraft import Minecraft
from mcpi import block
from buildings.constructor import constructor
from commands import commands
from commands.commands import parse_message, builder
from agents.BaseAgent import BaseAgent
from support import registry

discovered_agents = registry.discover_agents()

mc = Minecraft.create()
pos = mc.player.getTilePos()

builder_bot = discovered_agents["BuilderBot"]("builder", None)
miner_bot = discovered_agents["MinerBot"]("miner", None)
explorer_bot = discovered_agents["ExplorerBot"]("explorer", None)

agents : dict[str, BaseAgent] = {
    "builder": builder_bot
    ,"miner": miner_bot
    ,"explorer": explorer_bot
}

while True:
    chatEvents = mc.events.pollChatPosts()
    if chatEvents:
        for chatEvent in chatEvents:
            if chatEvent.message.startswith("!"):
                msg = parse_message(chatEvent.message)
                if type(msg) != str and msg["command"] in dir(agents[msg["agent"]]):
                    if not msg["args"]:
                        getattr(agents[msg["agent"]], msg["command"])()
                    else:
                        getattr(agents[msg["agent"]], msg["command"])(", ".join(msg["args"]))
                else:
                    print(msg)