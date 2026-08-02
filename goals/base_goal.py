from abc import ABC, abstractmethod
from agents.agent import Agent

class Goal(ABC):
    name = "Goal"
    @abstractmethod
    def score(self, agent: Agent) -> float:
        pass