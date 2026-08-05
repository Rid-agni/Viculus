from systems.interaction_type import InteractionType
from systems.interaction_effects import INTERACTION_EFFECTS
from systems.utility import Utility
from systems.reputation_system import ReputationSystem
import random

class SocialPlanner:
    def __init__(self):
        self.reputation = ReputationSystem()
    def choose(self, society, memory_system, agent):

     options = []

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

            options.append(
                Utility(
                    target,
                    interaction,
                    score
                )
            )

     if not options:
        return None

     scores = [max(0.1, o.score) for o in options]

     best = max(scores)
     weights = []
     for s in scores:
      if s < best - 4:
        weights.append(0.05)   # almost impossible
      else:
        weights.append(s)
     return random.choices(
    options,
    weights=weights,
    k=1
)[0]
    def score_interaction(self,society,memory_system,agent,target,interaction):
     p = agent.personality
     score = 5
     relationship = society.friendship(
        agent,
        target
    )
     score += relationship
     reputation = self.reputation.calculate(
    society,
    target
)
     fatigue = agent.social_fatigue
     if fatigue > 70:
       if interaction in (
        InteractionType.CONVERSATION,
        InteractionType.COMPLIMENT,
        InteractionType.HELP
    ):
        score -= 8
     elif fatigue > 40:
       if interaction in (
        InteractionType.CONVERSATION,
        InteractionType.COMPLIMENT
    ):
        score -= 4
     if (
    agent.needs.belonging < 30
    and interaction == InteractionType.CONVERSATION
):
        score += 5
     score += reputation * 3
     if interaction == InteractionType.CONVERSATION:
       score += p.extroversion * 5
       score += p.curiosity * 3
     elif interaction == InteractionType.COMPLIMENT:
       score += p.kindness * 5
       score += p.extroversion * 1
     elif interaction == InteractionType.HELP:
       score += p.kindness * 4
       score += p.confidence * 3
     elif interaction == InteractionType.IGNORE:
       score += (1 - p.extroversion) * 6
       score += p.ambition * 2
     elif interaction == InteractionType.INSULT:
       score -= p.kindness * 15
       score += (1 - p.kindness) * 6
       if relationship > 3:
         score -= 20
     needs = agent.needs
     if needs.belonging < 40:
       if interaction == InteractionType.CONVERSATION:
        score += 6
     elif interaction == InteractionType.COMPLIMENT:
        score += 3
     if needs.recognition < 40:
       if interaction == InteractionType.HELP:
        score += 5
     if needs.energy < 30:
       if interaction in (
        InteractionType.CONVERSATION,
        InteractionType.COMPLIMENT,
        InteractionType.HELP,
    ):
        score -= 4
     if relationship < 0.3:
      if interaction == InteractionType.CONVERSATION:
        score += 3
      if interaction == InteractionType.COMPLIMENT:
        score += 2
     elif relationship > 0.7:
      if interaction == InteractionType.HELP:
        score += 3
      if interaction == InteractionType.CONVERSATION:
        score += 1
     elif relationship < -3:
       if interaction == InteractionType.INSULT:
        score += 6
     elif relationship > 4:
      if interaction == InteractionType.INSULT:
        score -= 8
     memory = memory_system.memory_score(
    agent,
    target
)
     if interaction.value in ["Help", "Compliment", "Conversation"]:
      score += memory
     elif interaction.value == "Ignore":
      score -= memory * 0.5
     elif interaction.value == "Insult":
      score -= memory
     recent = memory_system.recent_interaction_count(
    agent,
    target,
    interaction
)   
     if recent == 0:
      score += 1.5
     score -= recent * 2
     score += random.uniform(-1.5, 1.5)
     return score