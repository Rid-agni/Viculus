from memory.memory import Memory
from memory.database import MemoryDatabase
import random
from systems.interaction_effects import INTERACTION_EFFECTS
from systems.interaction_type import InteractionType
class MemorySystem:
   def __init__(self):

        self.database = MemoryDatabase()
   def add_memory(self,society,result,current_time):
    TARGET_MEMORY = {
    "Conversation": "{target} had a pleasant conversation with me.",
    "Help": "{target} helped me.",
    "Compliment": "{target} complimented me.",
    "Ignore": "{target} ignored me.",
    "Insult": "{target} insulted me."
}
    self.database.add_memory(
        owner=result.initiator.name,
        other=result.target.name,
        interaction_type=result.interaction_type,
        description=result.memory_text,
        importance=1,
         source="SELF",
    confidence=1.0,
        timestamp=current_time
    )
    interaction = InteractionType(result.interaction_type)
    effects = INTERACTION_EFFECTS[interaction]    
    self.database.add_memory(
        owner=result.target.name,
        other=result.initiator.name,
        interaction_type=result.interaction_type,
       description = TARGET_MEMORY[
    result.interaction_type
].format(
        target=result.initiator.name
    ),
        importance=1,
         source="SELF",
    confidence=1.0,
        timestamp=current_time
    )
   def memory_score(self, agent, target):
    memories = self.database.get_memories_between(
        agent.name,
        target.name
    )

    opinion = 0

    for memory in memories:
        interaction = memory[0]
        importance = memory[2]

        if interaction == "Help":
            opinion += 2 * importance

        elif interaction == "Compliment":
            opinion += 1.5 * importance

        elif interaction == "Conversation":
            opinion += 1 * importance

        elif interaction == "Ignore":
            opinion -= 1.5 * importance

        elif interaction == "Insult":
            opinion -= 3 * importance

    return opinion
   def share_memory(self, speaker, listener, current_time):
    memories = self.database.get_recent_memories(
        speaker.name,
        limit=5
    )
    memories = [
        m
        for m in memories
        if m[5] > 0.3
    ]
    if not memories:
        return
    if random.random() > 0.12:
        return
    memory = random.choice(memories)
    other_agent, interaction_type, description, importance, source, confidence = memory
    self.database.add_memory(
        owner=listener.name,
        other=other_agent,
        interaction_type=interaction_type,
        description=f"{speaker.name} said: {description}",
        importance=importance * 0.7,
        source=speaker.name,
        confidence=confidence * 0.85,
        timestamp=current_time
    )
    print(
        f"{speaker.name} shared gossip with {listener.name}"
    )
   def recent_interaction_count(
    self,
    owner,
    other,
    interaction
):
     memories = self.database.get_memories(owner.name)
     count = 0
     for memory in memories:
        if (
            memory[2] == other.name
            and memory[3] == interaction.value
        ):
            count += 1
     return count
   def print_strongest_memory(self, agent, target):
     memories = self.database.get_memories_between(
        agent.name,
        target.name
    )
     if not memories:
        return
     strongest = memories[0]
     if strongest[2] >= 2:
        print(f"{agent.name} remembers: {strongest[1]}")