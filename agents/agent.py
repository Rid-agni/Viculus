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
        self.has_interacted = False
        self.social_cooldowns = {}
    def can_talk_to(self, target):
      return self.social_cooldowns.get(target.name, 0) == 0 
    def start_cooldown(self, target):
      self.social_cooldowns[target.name] = 5
    def update_cooldowns(self):

      for person in list(self.social_cooldowns):

        if self.social_cooldowns[person] > 0:

            self.social_cooldowns[person] -= 1
    