import random

def weighted_choice(scores):
    total = sum(scores.values())
    r = random.uniform(0, total)
    current = 0
    for item, weight in scores.items():
        current += weight
        if current >= r:
            return item