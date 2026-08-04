class TargetScorer:
    def score(self, society, agent, target):
        return (
            self.relationship_score(society, agent, target)
            + self.novelty_score(society, agent, target)
            + self.compatibility_score(agent, target)
        )
    def relationship_score(self, society, agent, target):
      if not society.has_relationship(agent, target):
        return 0
      return (
        society.friendship(agent, target) * 0.5
        + society.trust(agent, target) * 0.3
        + society.respect(agent, target) * 0.2
    )
    def novelty_score(self, society, agent, target):
      if society.has_relationship(agent, target):
        return 0
      return (
        agent.needs.curiosity * 0.2
        + agent.personality.curiosity * 10
    )
    def compatibility_score(self, agent, target):
     kindness = 1 - abs(
        agent.personality.kindness
        - target.personality.kindness
    )
     curiosity = 1 - abs(
        agent.personality.curiosity
        - target.personality.curiosity
    )
     confidence = 1 - abs(
        agent.personality.confidence
        - target.personality.confidence
    )
     return (
        kindness
       + curiosity
        + confidence
    ) * 3