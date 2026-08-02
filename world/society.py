import networkx as nx

class Society:
    def __init__(self):

        self.graph = nx.Graph()
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
        self.graph[a.name][b.name]["friendship"] = min(
        100,
        self.graph[a.name][b.name]["friendship"] + amount
    )


    def increase_trust(self, a, b, amount):
        self.ensure_relationship(a, b)
        self.graph[a.name][b.name]["trust"] = min(
        100,
        self.graph[a.name][b.name]["trust"] + amount
    )
    def increase_respect(self, a, b, amount):
        self.ensure_relationship(a, b)
        self.graph[a.name][b.name]["respect"] = min(
        100,
        self.graph[a.name][b.name]["respect"] + amount
    )
    def decrease_friendship(self, a, b, amount):
      self.ensure_relationship(a, b)

      self.graph[a.name][b.name]["friendship"] = max(
        0,
        self.graph[a.name][b.name]["friendship"] - amount
    )
    def decrease_trust(self, a, b, amount):
      self.ensure_relationship(a, b)

      self.graph[a.name][b.name]["trust"] = max(
        0,
        self.graph[a.name][b.name]["trust"] - amount
    )
    def decrease_respect(self, a, b, amount):
      self.ensure_relationship(a, b)

      self.graph[a.name][b.name]["respect"] = max(
        0,
        self.graph[a.name][b.name]["respect"] - amount
    )
    def has_relationship(self, a, b):
       return self.graph.has_edge(a.name, b.name)