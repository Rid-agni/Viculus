from goals.base_goal import Goal

class SocializeGoal(Goal):
    name = "Socialize"
    def score(self, agent):
     need = agent.needs.belonging / 100
     extroversion = agent.personality.extroversion
     confidence = agent.personality.confidence
     return (
        need ** 2
    ) * 100 * (0.5 + extroversion * 0.5) * (0.7 + confidence * 0.3)