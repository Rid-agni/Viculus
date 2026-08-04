from dataclasses import dataclass

@dataclass
class Memory:
    owner: str
    other_agent: str
    description: str
    importance: float
    timestamp: int