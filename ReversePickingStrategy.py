from PickingStrategy import PickingStrategy

class ReversePickingStrategy(PickingStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def pick(self, matchingResult):
        bestResult = None
        bestScore = 0

        for result in matchingResult:
            if result.getMatchingScore() > bestScore:
                bestResult = result
                bestScore = result.getMatchingScore()
        
        return bestResult