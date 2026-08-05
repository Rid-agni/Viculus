from systems.target_scoring import TargetScorer
from systems.interaction_result import InteractionResult
from systems.social_planner import SocialPlanner
from systems.memory_system import MemorySystem
from systems.interaction_effects import INTERACTION_EFFECTS
from systems.reputation_system import ReputationSystem
from systems.interaction_type import InteractionType
class InteractionSystem:

    def __init__(self):
        self.planner = SocialPlanner()
        self.scorer = TargetScorer()
        self.memory_system = MemorySystem()
        self.reputation = ReputationSystem()

    def choose_target(self, society, agent):
        candidates = []
        for npc in society.agents():
            if npc == agent:
                continue
            if npc.has_interacted:
                continue
            if not agent.can_talk_to(npc):
                continue
            candidates.append(npc)
        if not candidates:
            return None
        best_target = max(
            candidates,
            key=lambda npc: self.scorer.score(
                society,
                agent,
                npc
            )
        )
        for npc in candidates:
            print(
                f"{npc.name} : "
                f"{self.scorer.score(society, agent, npc):.2f}"
            )
        print("Chosen:", best_target.name)
        return best_target
    def interact(self, society, agent,current_time):
        
        choice = self.planner.choose(
    society,
    self.memory_system,
    agent
)
        if choice:
         self.memory_system.print_strongest_memory(
        agent,
        choice.target
    )
        if choice is None:
          return

        target = choice.target
        interaction_type = choice.interaction_type
        effect = INTERACTION_EFFECTS[interaction_type]
        agent.current_target = target
        result = InteractionResult(
    initiator=agent,
    target=target,
    interaction_type=interaction_type.value,
    friendship_change=effect["friendship"],
    trust_change=effect["trust"],
    respect_change=effect["respect"],
    belonging_change=effect["belonging"],
    recognition_change=effect["recognition"],
    memory_text=effect["memory"].format(
        target=target.name
    )
)
        if result.friendship_change >= 0:

         society.increase_friendship(
        result.initiator,
        result.target,
        result.friendship_change
    )

        else:

         society.decrease_friendship(
        result.initiator,
        result.target,
        abs(result.friendship_change)
    )

        if result.trust_change >= 0:

         society.increase_trust(
        result.initiator,
        result.target,
        result.trust_change
    )

        else:

         society.decrease_trust(
        result.initiator,
        result.target,
        abs(result.trust_change)
    )

        if result.respect_change >= 0:

         society.increase_respect(
        result.initiator,
        result.target,
        result.respect_change
    )

        else:

          society.decrease_respect(
        result.initiator,
        result.target,
        abs(result.respect_change)
    )
        if result.belonging_change >= 0:
           result.initiator.needs.satisfy_belonging(
        result.belonging_change
    )

        else:
          result.initiator.needs.belonging = max(
        0,
        result.initiator.needs.belonging + result.belonging_change
    )
        result.initiator.has_interacted = True
        result.target.has_interacted = True
        result.initiator.start_cooldown(result.target)
        result.target.start_cooldown(result.initiator)
       
        fatigue_gain = 0
        if interaction_type == InteractionType.CONVERSATION:
          fatigue_gain = 4
        elif interaction_type == InteractionType.COMPLIMENT:
          fatigue_gain = 3
        elif interaction_type == InteractionType.HELP:
          fatigue_gain = 5
        elif interaction_type == InteractionType.IGNORE:
          fatigue_gain = 1
        elif interaction_type == InteractionType.INSULT:
          fatigue_gain = 7
        fatigue_gain *= (
    1.3
    - (0.6 * result.initiator.personality.extroversion)
)
        result.initiator.social_fatigue = min(
    100,
    result.initiator.social_fatigue + fatigue_gain
)       
        verb = interaction_type.value.lower()
        if verb == "conversation":
          verb = "had a conversation with"
        elif verb == "ignore":
         verb = "ignored"
        elif verb == "help":
         verb = "helped"
        elif verb == "compliment":
         verb = "complimented"
        elif verb == "insult":
         verb = "insulted"
        print(f"{result.initiator.name} {verb} {result.target.name}")
        result.initiator.last_action = result.memory_text
        self.memory_system.share_memory(
    result.initiator,
    result.target,
    current_time
)    
        result.initiator.last_action = result.memory_text
        result.target.last_action = f"Interacted with {result.initiator.name}"
        return result
    