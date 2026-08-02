from world.clock import Clock
from agents.agent import Agent
from systems.need_system import NeedSystem
from systems.utility_system import DecisionSystem
from data.starter_agents import create_starter_agents

agents = create_starter_agents()
clock = Clock()
need_system = NeedSystem()
decision_system = DecisionSystem()

for _ in range(20):

    print(clock.current_time())

    for agent in agents:

        need_system.update(agent)

        decision_system.choose_goal(agent)

        print(
            f"{agent.name:8}"
            f"| Goal: {agent.current_goal.name:18}"
            f"| Energy: {agent.needs.energy:.1f}"
            f"| Belonging: {agent.needs.belonging:.1f}"
        )

    print("-"*70)

    clock.tick()