from systems.goals.base_goal import Goal

class RestGoal(Goal):
    name = "Rest"
    def score(self, agent):
        return 100 - agent.needs.energy