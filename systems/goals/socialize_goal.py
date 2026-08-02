from systems.goals.base_goal import Goal

class SocializeGoal(Goal):
    name = "Socialize"
    def score(self, agent):
        return agent.needs.belonging