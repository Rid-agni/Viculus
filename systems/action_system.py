class ActionSystem:
    def perform(self, agent):
        if agent.current_goal.name == "Rest":
            agent.social_fatigue = max(
    0,
    agent.social_fatigue - 10
)
            agent.needs.restore_energy(2)
            agent.last_action = "Resting"
            print(f"{agent.name} rested.")
            return f"{agent.name} rested."
        elif agent.current_goal.name == "Explore":
            agent.needs.satisfy_curiosity(4)
            agent.last_action = "Exploring"
            print(f"{agent.name} explored.")
            return f"{agent.name} explored the town."
        elif agent.current_goal.name == "Seek Recognition":
            agent.needs.satisfy_recognition(3)
            agent.last_action = "Seeking Recognition"
            print(f"{agent.name} achieved recognition.")
            return f"{agent.name} worked toward recognition."
        return None