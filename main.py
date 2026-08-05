from world.clock import Clock
#from agents.agent import Agent
from systems.need_system import NeedSystem
from systems.utility_system import DecisionSystem
from data.starter_agents import create_starter_agents
from world.society import Society
from systems.interaction_system import InteractionSystem
from systems.action_system import ActionSystem
from systems.memory_system import MemorySystem
from export_state import export_state
import server
import time
memory_system = MemorySystem()
action_system = ActionSystem()
society = Society()
interaction_system = InteractionSystem()
agents = create_starter_agents()

for agent in agents:

    society.add_agent(agent)


clock = Clock()
need_system = NeedSystem()
decision_system = DecisionSystem()
events=[]
for _ in range(100):

    print(clock.current_time())
    for agent in society.agents():
        agent.has_interacted = False
    for agent in society.agents():

        need_system.update(agent)
        agent.update_cooldowns()
        decision_system.choose_goal(agent)
        if agent.current_goal.name == "Socialize":
           result = interaction_system.interact(
        society,
        agent,
        clock.current_time()
    )
           if result:
            memory_system.add_memory(
            society,
            result,
            clock.minute
        )
            events.append(result.memory_text)
           else:
       
            action = action_system.perform(agent)

            if action:
             events.append(f"{action}.")
        else:
         action = action_system.perform(agent)
         if action:
          events.append(f"{action}.")
        print(
            f"{agent.name:8}"
            f"| Goal: {agent.current_goal.name:18}"
            f"| Energy: {agent.needs.energy:5.1f}"
            f"| Social: {agent.social_fatigue:5.1f}"
            f"| Belonging: {agent.needs.belonging:5.1f}"
        )
  
    print()

    print("Current Relationships")

    for a, b, data in society.graph.edges(data=True):

     print(f"{a} <-> {b}")
     print(data)
    print("\nReputation")
    for agent in agents:
      rep = interaction_system.reputation.calculate(
        society,
        agent
    )
      print(

        f"{agent.name}: {rep:.2f}"

    )
      for agent in society.agents():
       agent.recover_social_energy()
    print("-"*70)
    print("\nAlice's Memories")
    for memory in memory_system.database.get_memories("Alice"):
     print(memory)
    print("-" * 70)
    society.decay_relationships()
    clock.tick()
    export_state(
    society,
    memory_system,
    clock.current_time(),
    events
)
    time.sleep(1)   # wait 1 second before next tick