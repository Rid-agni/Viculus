class ActionSystem:
    def perform(self, agent):
        if agent.current_goal.name == "Rest":
            agent.needs.restore_energy(12)
            print(f"{agent.name} rested.")
        elif agent.current_goal.name == "Explore":
            agent.needs.satisfy_curiosity(10)
            print(f"{agent.name} explored.")
        elif agent.current_goal.name == "Seek Recognition":
            agent.needs.satisfy_recognition(8)
            print(f"{agent.name} achieved recognition.")