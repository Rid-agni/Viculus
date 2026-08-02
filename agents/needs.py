from dataclasses import dataclass

@dataclass
class Needs:
    hunger: float = 20
    energy: float = 100
    social: float = 80
    money: float = 20
    def update(self):

        self.hunger = min(100, self.hunger + 0.5)

        self.energy = max(0, self.energy - 0.3)

        self.social = max(0, self.social - 0.1)