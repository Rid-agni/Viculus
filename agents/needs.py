from dataclasses import dataclass

@dataclass
class Needs:
    energy: float = 100.0
    belonging: float = 40.0
    recognition: float = 30.0
    curiosity: float = 50.0
    def update(self):
        self.energy = max(0, self.energy - 0.2)
        self.belonging = min(100, self.belonging + 0.15)
        self.recognition = min(100, self.recognition + 0.08)
        self.curiosity = min(100, self.curiosity + 0.05)
    def restore_energy(self, amount):
        self.energy = min(100, self.energy + amount)
    def satisfy_belonging(self, amount):
        self.belonging = max(0, self.belonging - amount)
    def satisfy_recognition(self, amount):
        self.recognition = max(0, self.recognition - amount)
    def satisfy_curiosity(self, amount):
        self.curiosity = max(0, self.curiosity - amount)