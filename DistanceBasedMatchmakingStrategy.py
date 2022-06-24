from Individual import Individual
from MatchmakingStrategy import MatchmakingStrategy
from MatchingResult import MatchingResult
from math import sqrt, pow

class DistanceBasedMatchmakingStrategy(MatchmakingStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def match(self, individuals):
        result = dict()
        for individual in individuals:
            result[individual] = list()
            coord1 = individual.getCoord()
            for otherIndividual in individuals:
                if individual == otherIndividual:
                    continue
                coord2 = otherIndividual.getCoord()
                score = sqrt(pow(coord1[0]-coord2[0],2) + pow(coord1[1] - coord2[1], 2))
                matchingResult = MatchingResult(otherIndividual, score)
                result[individual].append(matchingResult)

        return result

