from world.clock import Clock
#from agents.agent import Agent
from systems.need_system import NeedSystem
from systems.utility_system import DecisionSystem
from data.starter_agents import create_starter_agents
from world.society import Society
from systems.interaction_system import InteractionSystem
from systems.action_system import ActionSystem

action_system = ActionSystem()
society = Society()
interaction_system = InteractionSystem()
agents = create_starter_agents()

for agent in agents:

    society.add_agent(agent)


clock = Clock()
need_system = NeedSystem()
decision_system = DecisionSystem()

for _ in range(20):

    print(clock.current_time())

    for agent in society.agents():

        need_system.update(agent)

        decision_system.choose_goal(agent)
        if agent.current_goal.name == "Socialize":

           interaction_system.interact(
        society,
        agent
    )
        else:
           action_system.perform(agent)
        print(
            f"{agent.name:8}"
            f"| Goal: {agent.current_goal.name:18}"
            f"| Energy: {agent.needs.energy:.1f}"
            f"| Belonging: {agent.needs.belonging:.1f}"
        )
  
    print()

    print("Current Relationships")

    for a, b, data in society.graph.edges(data=True):

     print(f"{a} <-> {b}")
     print(data)
    print("-"*70)
    clock.tick()