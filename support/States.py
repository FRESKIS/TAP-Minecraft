class state(enumerate):
    IDLE = "IDLE"               # Waiting for a command
    RUNNING = "RUNNING"         # Actively executing its task
    PAUSED = "PAUSED"           # Temporarily halted, with full context preserved
    WAITING = "WAITING"         # Blocked, awaiting data or resources
    STOPPED = "STOPPED"         # Terminated safely with state and data persisted
    ERROR = "ERROR"             # An unrecoverable issue occurred; the agent halts safely and notifies dependents


