from MatchmakingStrategy import MatchmakingStrategy
from MatchingResult import MatchingResult
from StringToSet import StringToSet
from StringToSet import StringToSet

class HabitBasedMatchmakingStrategy(MatchmakingStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def match(self, individuals):
        result = dict()
        for individual in individuals:
            result[individual] = list()
            habits1 = individual.getHabits()
            set1 = StringToSet.stringToSet(habits1)

            for otherIndividual in individuals:
                if individual == otherIndividual:
                    continue
                habits2 = otherIndividual.getHabits()
                set2 = StringToSet.stringToSet(habits2)
                score = len(set1.intersection(set2))
                matchingResult = MatchingResult(otherIndividual, score)
                result[individual].append(matchingResult)

        return result