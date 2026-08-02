from goals.base_goal import Goal

class RecognitionGoal(Goal):
    name = "Seek Recognition"
    def score(self, agent):
        return (
            agent.needs.recognition *
            (0.5 + agent.personality.ambition)
        )