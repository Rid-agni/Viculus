class ActionSystem:
    def perform(self, agent):
        if agent.current_goal.name == "Rest":
            agent.needs.restore_energy(6)
            print(f"{agent.name} rested.")
        elif agent.current_goal.name == "Explore":
            agent.needs.satisfy_curiosity(4)
            print(f"{agent.name} explored.")
        elif agent.current_goal.name == "Seek Recognition":
            agent.needs.satisfy_recognition(3)
            print(f"{agent.name} achieved recognition.")