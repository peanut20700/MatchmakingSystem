from abc import ABC, abstractclassmethod

class MatchmakingStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def match(self, individuals):
        pass