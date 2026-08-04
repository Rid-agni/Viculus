from systems.interaction_type import InteractionType

INTERACTION_EFFECTS = {
    InteractionType.CONVERSATION: {
        "friendship": 0.05,
        "trust": 0.03,
        "respect": 0.02,
        "belonging": 3,
        "recognition": 0,
        "memory": "Had a pleasant conversation with {target}."
    },
    InteractionType.HELP: {
        "friendship": 0.04,
        "trust": 0.08,
        "respect": 0.10,
        "belonging": 2,
        "recognition": 2,
        "memory": "Helped {target}."
    },
    InteractionType.COMPLIMENT: {
        "friendship": 0.08,
        "trust": 0.04,
        "respect": 0.05,
        "belonging": 3,
        "recognition": 1,
        "memory": "Complimented {target}."
    },
    InteractionType.IGNORE: {
        "friendship": -0.04,
        "trust": -0.02,
        "respect": -0.01,
        "belonging": -2,
        "recognition": 0,
        "memory": "Ignored {target}."
    },
    InteractionType.INSULT: {
        "friendship": -0.10,
        "trust": -0.08,
        "respect": -0.05,
        "belonging": -3,
        "recognition": 0,
        "memory": "Insulted {target}."
    }
}