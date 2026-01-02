from abc import ABC
from textwrap import dedent


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
        await self.answer_to_chat(f"Current plan list:\n" + "\n".join(f"- {x}" for x in self.plan_list))

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