from goals.base_goal import Goal

class RestGoal(Goal):
    name = "Rest"
    def score(self, agent):
        tiredness = 100 - agent.needs.energy
        return tiredness