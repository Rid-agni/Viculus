class ReputationSystem:
    def calculate(self, society, agent):
        total = 0
        count = 0
        for other in society.agents():
            if other == agent:
                continue
            if not society.has_relationship(agent, other):
                continue
            total += (
                society.friendship(other, agent) * 0.25
                + society.trust(other, agent) * 0.35
                + society.respect(other, agent) * 0.40
            )
            count += 1
        if count == 0:
            return 0
        reputation = total / count
        return max(-1.0, min(1.0, reputation))