from memory.memory import Memory
from memory.database import MemoryDatabase
import random
class MemorySystem:
   def __init__(self):

        self.database = MemoryDatabase()
   def add_memory(self,society,result,current_time):
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
    self.database.add_memory(
        owner=result.target.name,
        other=result.initiator.name,
        interaction_type=result.interaction_type,
        description=f"Had a pleasant conversation with {result.initiator.name}.",
        importance=1,
         source="SELF",
    confidence=1.0,
        timestamp=current_time
    )
   def memory_score(
    self,
    agent,
    target,
    interaction
):
     memories = self.database.get_memories_between(
    agent.name,
    target.name
)
     score = 0
     for memory in memories:
       interaction_type = memory[0]
       if interaction.value == interaction_type:
          score += 2
       if interaction_type == "Help":
          score += 1
       elif interaction_type == "Compliment":
          score += 0.5
       elif interaction_type == "Ignore":
          score -= 1
       elif interaction_type == "Insult":
          score -= 2
     return score
   def share_memory(self, speaker, listener, current_time):

    memories = self.database.get_recent_memories(
        speaker.name,
        limit=5
    )
    memories = [
        memory
        for memory in memories
        if memory[4] > 0.3      # confidence column
    ]
    if not memories:
        return

    if random.random() > 0.30:
        return

    memory = random.choice(memories)

    interaction_type, description, importance, source, confidence = memory

    self.database.add_memory(

        owner=listener.name,

        other=source,

        interaction_type=interaction_type,

        description=f"{speaker.name} told me: {description}",

        importance=importance * 0.7,

        source=speaker.name,

        confidence=confidence * 0.85,

        timestamp=current_time
    )

    print(
        f"{speaker.name} shared a memory with {listener.name}"
    )