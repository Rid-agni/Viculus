from agents.needs import Needs
from agents.personality import Personality

class Agent:
    def __init__(self, name: str, occupation: str):
        self.name = name
        self.occupation = occupation
        self.needs = Needs()
        self.personality = Personality(
            kindness=0.8,
            extroversion=0.7,
            ambition=0.5,
            curiosity=0.6
        )
        self.goal = None
        self.state = "Idle"