from abc import ABC
import json
import uuid
from support.JSONMessageHandeler import JSONMessageHandeler
from textwrap import dedent
from support.States import state
from buildings.constructor import constructor


class BuilderCommand(ABC):
    async def help(self):
        msg = dedent("""\
        Available commands:
        !builder plan list
        !builder plan set <template> [params]
        !builder bom
        !builder build
        !builder pause
        !builder resume
        !builder stop
        """)
        await self.answer_to_chat(msg)

    async def planlist(self):
        await self.answer_to_chat(f"Current plan list:\n" + "\n".join(f"- {plan['name']}" for plan in self.plan_list))

    async def planset(self, template: str):
        plans = constructor.load(template)  # Verify that the template exists
        params = { "name": template, "Nblocks": plans["Nblocks"], "materials": plans["materials"], "lenght": plans["dimensions"]["length"], "height": plans["dimensions"]["height"], "width": plans["dimensions"]["width"] }  # Default empty params
        self.plan_list.append(params)
        await self.answer_to_chat(f"Plan '{template}' added to the plan list.")

    async def build(self, template=None):
        if self.state == state.IDLE:
            await self.run()
        elif template != None:
            self.tasks.clear()
            self.contecxt = {}
            self.tasks.append(template)
            await self.run()
        else:
            await self.amswer_to_chat(f"Builder is already running, task stored")




class MinerCommand(ABC):
    async def help(self):
        msg = f"""Available commands:
        !miner start [ x = < int > z = < int > y = < int >]
        !miner set strategy < vertical | grid | vein >
        !miner fulfill
        !miner pause
        !miner resume
        !miner status
        !miner stop
        """
        await self.answer_to_chat(msg)

    async def start(self, x, z, range, workflow=None):
        if workflow != None:
            self.tasks.append({})
        else: 
            if self.state == state.IDLE:
                await self.run()
            elif not self.bom:
                self.tasks.clear()
                self.contecxt = {}
                self.tasks.append({})
            else:
                await self.amswer_to_chat(f"Explorer is already running, task stored")

class ExplorerCommand(ABC):
    async def help(self):
        msg = f"""Available commands:
        !explorer start x =< int > z = < int > [ range = < int >]
        !explorer stop
        !explorer set range <int >
        !explorer status
        !explorer pause
        !explorer resume
        """
        await self.answer_to_chat(msg)

    async def start(self, x, z, range, workflow=None):
        exp_id = str(uuid.uuid4)
        self.tasks.append({"": exp_id, "explored_area": [{"x": x, "z": z, "area": range}], "height_maps": [], "progress": {"x": 0, "z": 0}})
        if self.state == state.IDLE:
            await self.run()
        elif workflow != None:
            self.tasks.clear()
            self.contecxt = {}
            self.tasks.append({"expedition_id": exp_id, "explored_area": [{"x": x, "z": z, "area": range}], "height_maps": [], "progress": {"x": 0, "z": 0}})
        else:
            await self.amswer_to_chat(f"Explorer is already running, task stored")

    async def stop(self):
        self.stop.set()
        await self.answer_to_chat("Exploration stopped.")

    async def wait(self):
        if self.wait.is_set():
            self.wait.clear()
            await self.answer_to_chat("Exploration resumed.")
        else:
            self.wait.set()
            await self.answer_to_chat("Exploration paused.")


class Workflow():
    def __init__(self, builder, explorer, miner):
        self.builder = builder
        self.explorer = explorer
        self.miner = miner 

    async def run(self, lenght, width, range, template, strategy, minerx, minery, minerz):
        self.explorer.start(lenght, width, range, 1)
        self.builder.build(template)
        self.miner.strategy = strategy
        self.miner.start()
