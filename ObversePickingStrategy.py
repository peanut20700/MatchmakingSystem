from PickingStrategy import PickingStrategy
from MatchingResult import MatchingResult

class ObversePickingStrategy(PickingStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def pick(self, matchingResult):
        bestResult = None
        bestScore = float('inf')

        for result in matchingResult:
            if result.getMatchingScore() < bestScore:
                bestResult = result
                bestScore = result.getMatchingScore()
        
        return bestResult