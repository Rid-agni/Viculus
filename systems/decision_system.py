from systems.goals.rest_goal import RestGoal
from systems.goals.socialize_goal import SocializeGoal
from systems.goals.recognition_goal import RecognitionGoal
from systems.goals.explore_goal import ExploreGoal

class DecisionSystem:
    def __init__(self):
        self.goals = [
            RestGoal(),
            SocializeGoal(),
            RecognitionGoal(),
            ExploreGoal()
        ]
    def choose_goal(self, agent):
        best_goal = max(
            self.goals,
            key=lambda goal: goal.score(agent)
        )
        agent.goal = best_goal