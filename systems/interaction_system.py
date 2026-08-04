from systems.target_scoring import TargetScorer
from systems.interaction_result import InteractionResult
from systems.social_planner import SocialPlanner
from systems.memory_system import MemorySystem
from systems.interaction_effects import INTERACTION_EFFECTS
class InteractionSystem:

    def __init__(self):
        self.planner = SocialPlanner()
        self.scorer = TargetScorer()
        self.memory_system = MemorySystem()
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
        self.memory_system.share_memory(
       result.initiator,
    result.target,
    current_time
)
        print(
           f"{result.initiator.name} "
           f"{interaction_type.value.lower()}ed "
           f"{result.target.name}"
)
        print(
            f"{result.initiator.name} talked with {result.target.name}"
        )
        return result
    