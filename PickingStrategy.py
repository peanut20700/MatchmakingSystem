from abc import ABC, abstractclassmethod


class PickingStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def pick(self, matchingResult):
        pass