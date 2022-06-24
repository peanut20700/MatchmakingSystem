from unicodedata import name


class MatchmakingSystem:
    def __init__(self, matchmakingStrategy, pickingStrategy) -> None:
        self.individuals = list()
        self.matchmakingStrategy = None
        self.pickingStrategy = None
        self.matchingResult = dict()

        self.setMatchmakingStrategy(matchmakingStrategy)
        self.setPickingStrategy(pickingStrategy)
    
    def addIndividual(self, individual):
        self.individuals.append(individual)
    
    def getIndividuals(self):
        return self.individuals
    
    def setMatchmakingStrategy(self, matchmakingStrategy):
        self.matchmakingStrategy = matchmakingStrategy
    
    def setPickingStrategy(self, pickingStrategy):
        self.pickingStrategy = pickingStrategy

    def match(self):
        self.matchingResult = self.matchmakingStrategy.match(self.getIndividuals())

    def printMatchingResult(self):
        for individual in self.matchingResult.keys():
            print("Result for individual no " + str(individual.getId()))
            matchingResult = self.matchingResult[individual]
            for result in matchingResult:
                print("score with no " + str(result.getMatchingResult().getId()) + " : " + str(result.getMatchingScore()))
    
    def printMatchingResultForIndivodual(self):
        for individual in self.individuals:
            print("Result for individual no " + str(individual.getId()) + " : no " + str(individual.getMatchingResult().getMatchingResult().getId()))
            print("score: " + str(individual.getMatchingResult().getMatchingScore()) + "\n")

    def pickResultForIndividual(self):
        for individual in self.individuals:
            matchingResult = self.pickingStrategy.pick(self.matchingResult[individual])
            individual.setMatchingResult(matchingResult)