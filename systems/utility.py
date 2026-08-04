from dataclasses import dataclass

@dataclass
class Utility:
    target: object
    interaction_type: object
    score: float