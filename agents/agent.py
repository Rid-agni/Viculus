from agents.needs import Needs
from agents.personality import Personality

class Agent:
    def __init__(
        self,
        name: str,
        occupation: str,
        personality: Personality
    ):
        self.name = name
        self.occupation = occupation
        self.needs = Needs()
        self.personality = personality
        self.current_goal = None
        self.current_target = None
        self.state = "Idle"