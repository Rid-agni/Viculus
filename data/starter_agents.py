from agents.agent import Agent
from agents.personality import Personality

def create_starter_agents():
    agents = []
    alice = Agent("Alice", "Student",Personality(
        kindness=0.9,
        extroversion=0.8,
        ambition=0.5,
        curiosity=0.7,
        confidence=0.8
    ))
    alice.needs.belonging = 75
    alice.needs.curiosity = 30
    alice.needs.recognition = 20
    alice.needs.energy = 95
    bob = Agent("Bob", "Engineer",Personality(
        kindness=0.4,
        extroversion=0.2,
        ambition=0.9,
        curiosity=0.5,
        confidence=0.9
    ))
    bob.needs.energy = 77
    bob.needs.curiosity = 35
    bob.needs.belonging = 60
    bob.needs.recognition = 10
    charlie = Agent("Charlie", "Artist",Personality(
        kindness=0.6,
        extroversion=0.9,
        ambition=0.3,
        curiosity=1.0,
        confidence=0.6
    ))
    charlie.needs.energy = 20
    charlie.needs.curiosity = 20
    charlie.needs.belonging = 40
    charlie.needs.recognition = 25
    diana = Agent("Diana", "Researcher", Personality(
        kindness=0.8,
        extroversion=0.4,
        ambition=0.8,
        curiosity=0.8,
        confidence=0.5
    ))
    diana.needs.curiosity = 95
    diana.needs.energy = 95
    diana.needs.recognition = 15
    diana.needs.belonging = 30
    ethan = Agent("Ethan", "Traveler",Personality(
        kindness=0.5,
        extroversion=0.7,
        ambition=0.4,
        curiosity=0.95,
        confidence=0.7
    ))
    ethan.needs.belonging = 20
    ethan.needs.recognition = 85
    ethan.needs.curiosity = 40
    ethan.needs.energy = 90
    agents.extend([
        alice,
        bob,
        charlie,
        diana,
        ethan
    ])
    return agents