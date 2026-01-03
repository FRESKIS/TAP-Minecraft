from abc import ABC
from textwrap import dedent
from support.States import state
from buildings.constructor import constructor


def parse_message(msg: str) -> dict | str:
    msg: str = msg.strip()

    parts = msg[1:].split()   # quitamos el !
    if not parts:
        return "Nai"

    agent = parts[0].lower()
    if agent not in ["builder", "miner", "explorer"]:
        return "Agent not found"
    if len(parts) < 2:
        return "No command provided"
    command = parts[1]
    args = parts[2:]

    return {
        "agent": agent,
        "command": command,
        "args": args
    }


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
        """)
        await self.answer_to_chat(msg)

    async def planlist(self):
        await self.answer_to_chat(f"Current plan list:\n" + "\n".join(f"- {plan['name']}" for plan in self.plan_list))

    async def planset(self, template: str):
        plans = constructor.load(template)  # Verify that the template exists
        params = { "name": template, "Nblocks": plans["Nblocks"], "materials": plans["materials"], "lenght": plans["dimensions"]["length"], "height": plans["dimensions"]["height"], "width": plans["dimensions"]["width"] }  # Default empty params
        self.plan_list.append(params)
        await self.answer_to_chat(f"Plan '{template}' added to the plan list.")

    async def start(self):
        if self.state is not state.IDLE:
            await self.run()

class MinerCommand(ABC):
    async def help(self):
        msg = f"""Available commands:
        !miner dig < area >
        !miner pause
        """
        await self.answer_to_chat(msg)

class ExplorerCommand(ABC):
    async def help(self):
        msg = f"""Available commands:
        !explorer explore < area >
        !explorer pause
        """
        await self.answer_to_chat(msg)

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