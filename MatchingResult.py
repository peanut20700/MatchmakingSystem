class MatchingResult:
    def __init__(self, matchingResult, matchingScore) -> None:
        self.setMatchingResult(matchingResult)
        self.setMatchingScore(matchingScore)

    def setMatchingResult(self, matchingResult):
        self.matchingResult = matchingResult
    
    def getMatchingResult(self):
        return self.matchingResult

    def setMatchingScore(self, matchingScore):
        self.matchingScore = matchingScore
    
    def getMatchingScore(self):
        return self.matchingScore
    
