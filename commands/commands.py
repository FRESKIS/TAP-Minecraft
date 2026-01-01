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


class builder:
    @staticmethod
    def help():
        print("Available commands:")
        print("!builder plan list")
        print("!builder plan set < template > [ params ]")
        print("!builder bom")
        print("!builder build")
        print("!builder pause")
        print("!builder resume")

    @staticmethod
    def planlist():
        pass

class miner:
    @staticmethod
    def help():
        print("Available commands:")
        print("!miner mine < area >")
        print("!miner pause")
        print("!miner resume")

class explorer:
    @staticmethod
    def help():
        print("Available commands:")
        print("!explorer explore < area >")
        print("!explorer pause")
        print("!explorer resume")