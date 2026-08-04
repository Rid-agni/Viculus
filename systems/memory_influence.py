class MemoryInfluence:
    def apply(self, memory_system, agent, target, scores):
        memories = memory_system.get_memories(
            agent.name,
            target.name,
            limit=5
        )
        for memory in memories:
            text = memory[3]
            if "Complimented" in text:
                scores["compliment"] = scores.get("compliment", 0)
            if "Helped" in text:
                scores["help"] = scores.get("help", 0)
        return scores