from mcpi.minecraft import Minecraft
from mcpi import block
from buildings.constructor import constructor
from commands import commands
from commands.commands import parse_message, builder
from agents.BuilderBot import BuilderBot 
from agents.MinerBot import MinerBot    
from agents.ExplorerBot import ExplorerBot
from agents.BaseAgent import BaseAgent


mc = Minecraft.create()
pos = mc.player.getTilePos()

builder_bot = BuilderBot("builder", None)
miner_bot = MinerBot("miner", None)
explorer_bot = ExplorerBot("explorer", None)

agents : dict[str, BaseAgent] = {
    "builder": builder_bot
    ,"miner": miner_bot
    ,"explorer": explorer_bot
}

while True:
    chatEvents = mc.events.pollChatPosts()
    if chatEvents:
        print("New chat message")
        for chatEvent in chatEvents:
            msg = parse_message(chatEvent.message)
            if msg != None and msg["command"] in dir(agents[msg["agent"]]):
                print(1)
                if not msg["args"]:
                    getattr(agents[msg["agent"]], msg["command"])()
                else:
                    getattr(agents[msg["agent"]], msg["command"])(", ".join(msg["args"]))
            elif msg == None:
                print("comando invalido")