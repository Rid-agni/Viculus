from world.clock import Clock
from agents.agent import Agent
from systems.need_system import NeedSystem
from systems.decision_system import DecisionSystem

clock = Clock()
alice = Agent(
    name="Alice",
    occupation="Student"
)
need_system = NeedSystem()
decision_system = DecisionSystem()
for _ in range(20):
    print(clock.current_time())
    print(
        f"Energy: {alice.needs.energy:.1f} | "
        f"Belonging: {alice.needs.belonging:.1f} | "
        f"Recognition: {alice.needs.recognition:.1f} | "
        f"Curiosity: {alice.needs.curiosity:.1f}"
    )
    need_system.update(alice)
    decision_system.choose_goal(alice)
    print(f"Current Goal: {alice.goal.name}")
    print("-" * 50)
    clock.tick()