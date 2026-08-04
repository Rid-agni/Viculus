from enum import Enum

class InteractionType(Enum):
    CONVERSATION = "Conversation"
    HELP = "Help"
    COMPLIMENT = "Compliment"
    IGNORE = "Ignore"
    INSULT = "Insult"