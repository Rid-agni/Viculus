from dataclasses import dataclass

@dataclass
class InteractionResult:
    initiator: object
    target: object
    interaction_type: str
    friendship_change: float
    trust_change: float
    respect_change: float
    belonging_change: float
    recognition_change: float
    memory_text: str