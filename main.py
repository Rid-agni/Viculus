from world.clock import Clock
from agents.agent import Agent
from systems.need_system import NeedSystem

clock = Clock()
alice = Agent(
    name="Alice",
    occupation="Farmer"
)
needs = NeedSystem()
for _ in range(10):
    print(clock.current_time())
    print(
        f"Hunger: {alice.needs.hunger:.1f} | "
        f"Energy: {alice.needs.energy:.1f} | "
        f"Social: {alice.needs.social:.1f}"
    )
    print("-" * 40)
    needs.update(alice)
    clock.tick()