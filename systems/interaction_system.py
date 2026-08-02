import random

class InteractionSystem:
    def choose_target(self, society, agent):
        candidates = []
        for other in society.agents():
            if other != agent:
                candidates.append(other)
        if not candidates:
            return None
        return random.choice(candidates)
    def interact(self, society, agent):
        target = self.choose_target(society, agent)
        if target is None:
            return
        agent.current_target = target
        society.increase_friendship(agent, target, 5)
        society.increase_trust(agent, target, 2)
        society.increase_respect(agent, target, 1)
        agent.needs.satisfy_belonging(8)
        print(
            f"{agent.name} talked with {target.name}"
        )