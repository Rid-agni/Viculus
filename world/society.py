import networkx as nx

class Society:
    def __init__(self):

        self.graph = nx.Graph()
    def _bounded_increase(self, current, amount):
     return min(
        1.0,
        current + amount * (1 - current)
    )

    def _bounded_decrease(self, current, amount):
     return max(
        0.0,
        current - amount * current
    )
    def add_agent(self, agent):
        self.graph.add_node(
            agent.name,
            agent=agent
        )
    def get_agent(self, name):

        return self.graph.nodes[name]["agent"]
    def agents(self):
        return [
            data["agent"]
            for _, data in self.graph.nodes(data=True)
        ]
    def ensure_relationship(self, a, b):

     if not self.graph.has_edge(a.name, b.name):

        self.graph.add_edge(
            a.name,
            b.name,
            friendship=0,
            trust=0,
            respect=0
        )

         
    
    def friendship(self, a, b):
        self.ensure_relationship(a, b)
        return self.graph[a.name][b.name]["friendship"]

    def trust(self, a, b):
        self.ensure_relationship(a, b)
        return self.graph[a.name][b.name]["trust"]

    def respect(self, a, b):
        self.ensure_relationship(a, b)
        return self.graph[a.name][b.name]["respect"]

    def increase_friendship(self, a, b, amount):
     self.ensure_relationship(a, b)
     current = self.graph[a.name][b.name]["friendship"]
     self.graph[a.name][b.name]["friendship"] = (
        self._bounded_increase(current, amount)
    )
    
    def increase_trust(self, a, b, amount):
      self.ensure_relationship(a, b)
      current = self.graph[a.name][b.name]["trust"]
      self.graph[a.name][b.name]["trust"] = (
        self._bounded_increase(current, amount)
    )
    def increase_respect(self, a, b, amount):
     self.ensure_relationship(a, b)
     current = self.graph[a.name][b.name]["respect"]
     self.graph[a.name][b.name]["respect"] = (
        self._bounded_increase(current, amount)
    )
    def decrease_friendship(self, a, b, amount):
     self.ensure_relationship(a, b)
     current = self.graph[a.name][b.name]["friendship"]
     self.graph[a.name][b.name]["friendship"] = (
        self._bounded_decrease(current, amount)
    )
    def decrease_trust(self, a, b, amount):
     self.ensure_relationship(a, b)
     current = self.graph[a.name][b.name]["trust"]
     self.graph[a.name][b.name]["trust"] = (
        self._bounded_decrease(current, amount)
    )
    def decrease_respect(self, a, b, amount):
     self.ensure_relationship(a, b)
     current = self.graph[a.name][b.name]["respect"]
     self.graph[a.name][b.name]["respect"] = (
        self._bounded_decrease(current, amount)
    )
    def has_relationship(self, a, b):
       return self.graph.has_edge(a.name, b.name)
    def decay_relationships(self):
      for _, _, data in self.graph.edges(data=True):
        data["friendship"] = self._bounded_decrease(
        data["friendship"],
    0.02
)
        data["trust"] = self._bounded_decrease(
    data["trust"],
    0.01
)
        data["respect"] = self._bounded_decrease(
    data["respect"],
    0.005
)
    def neighbors(self, agent):

     return [
        self.get_agent(name)
        for name in self.graph.neighbors(agent.name)
    ]
    def strangers(self, agent):
       known = set(self.graph.neighbors(agent.name))
       return [
        other
        for other in self.agents()
        if other.name != agent.name
        and other.name not in known
    ]