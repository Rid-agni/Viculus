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