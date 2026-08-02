from agents.needs import Needs
from agents.personality import Personality

class Agent:

    def __init__(self, name: str, occupation: str):

        self.name = name
        self.occupation = occupation

        self.needs = Needs()

        self.personality = Personality(
            kindness=0.8,
            greed=0.2,
            curiosity=0.6
        )