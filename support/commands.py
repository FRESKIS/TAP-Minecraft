import asyncio

async def dispatch_command(agent, command: str, args: list[str]):
    fn = getattr(agent, command)
    if args:
        res = fn(", ".join(args))
    else:
        res = fn()
    
    if asyncio.isawaitable(res):
        await res
    else:
        res


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
