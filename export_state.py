import json
from systems.reputation_system import ReputationSystem

reputation = ReputationSystem()

def export_state(society, memory_system, tick, events):

    agents = []
    relationships = []
   

    # ------------------------
    # Agents
    # ------------------------

    for agent in society.agents():

        memories = memory_system.database.get_memories(agent.name)

        latest_memory = ""

        if memories:
            latest_memory = memories[0][2]

        agents.append({

            "id": agent.name.lower(),

            "name": agent.name,

            "role": agent.occupation,

"goal": (
    agent.current_goal.name.replace("_", " ")
    if agent.current_goal
    else "Idle"
),
            "energy": round(agent.needs.energy),

            "belonging": round(agent.needs.belonging),

            "reputation": round(
    reputation.calculate(
        society,
        agent
    ),
    2
),

            "action": getattr(agent,"last_action",""),

            "memory": latest_memory

        })

    # ------------------------
    # Relationships
    # ------------------------

    done = set()

    for a in society.agents():

        for b in society.agents():

            if a == b:
                continue

            pair = tuple(sorted([a.name,b.name]))

            if pair in done:
                continue

            done.add(pair)

            friendship = society.friendship(a,b)
            trust = society.trust(a,b)
            respect = society.respect(a,b)

            strength = (
                friendship +
                trust +
                respect
            ) / 3

            if strength > .60:
                sentiment = "pos"

            elif strength < .30:
                sentiment = "neg"

            else:
                sentiment = "neutral"

            relationships.append({

                "a": a.name.lower(),

                "b": b.name.lower(),

                "strength": strength,

                "sentiment": sentiment

            })

    # ------------------------
    # JSON
    # ------------------------

    state = {

        "tick": tick,

        "agents": agents,

        "relationships": relationships,

        "events": events

    }

    with open("simulation_state.json","w") as f:

        json.dump(
            state,
            f,
            indent=4
        )