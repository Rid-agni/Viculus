from goals.base_goal import Goal

class ExploreGoal(Goal):
    name = "Explore"
    def score(self, agent):
        return (
            agent.needs.curiosity *
            (0.2 + agent.personality.curiosity)
        )