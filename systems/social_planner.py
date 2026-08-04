from systems.interaction_type import InteractionType
from systems.interaction_effects import INTERACTION_EFFECTS
from systems.utility import Utility

class SocialPlanner:
    def choose(self, society, memory_system, agent):
        best = None
        for target in society.agents():
            if target == agent:
                continue
            if target.has_interacted:
                continue
            if not agent.can_talk_to(target):
                continue
            for interaction in INTERACTION_EFFECTS.keys():
                score = self.score_interaction(
                    society,
                    memory_system,
                    agent,
                    target,
                    interaction
                )
                utility = Utility(
                    target,
                    interaction,
                    score
                )
                if best is None or utility.score > best.score:
                    best = utility
        return best
    def score_interaction(self,society,memory_system,agent,target,interaction):
     p = agent.personality
     score = 5
     relationship = society.friendship(
        agent,
        target
    )
     score += relationship
     if interaction == InteractionType.CONVERSATION:
        score += p.curiosity * 5
     elif interaction == InteractionType.COMPLIMENT:
        score += p.kindness * 6
        score += p.confidence * 2
     elif interaction == InteractionType.HELP:
        score += p.kindness * 5
     elif interaction == InteractionType.IGNORE:
        score += (1 - p.confidence) * 2
     elif interaction == InteractionType.INSULT:
        score += (1 - p.kindness) * 5
     score += memory_system.memory_score(
        agent,
        target,
        interaction
    )
     return score