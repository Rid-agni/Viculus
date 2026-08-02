from goals.rest_goal import RestGoal
from goals.socialize_goal import SocializeGoal
from goals.recognition_goal import RecognitionGoal
from goals.explore_goal import ExploreGoal

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
        agent.current_goal = best_goal