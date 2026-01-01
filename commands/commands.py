def parse_message(msg: str):
    msg: str = msg.strip()

    # solo comandos que empiecen por !
    if not msg.startswith("!"):
        return None

    parts = msg[1:].split()   # quitamos el !
    if not parts:
        return None

    agent = parts[0].lower()
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