from goals.base_goal import Goal

class SocializeGoal(Goal):
    name = "Socialize"
    def score(self, agent):
        need = agent.needs.belonging
        extroversion = agent.personality.extroversion
        confidence = agent.personality.confidence
        return need * (0.2 + extroversion) * (0.5 + confidence)