class Individual:
    def __init__(self, id, gender, age, intro, habits, coord) -> None:
        self.id = id
        self.gender = gender
        self.age = age
        self.intro = intro
        self.habits = habits
        self.coord = coord
        self.matchingResult = None
    
    def getId(self):
        return self.id
    
    def getCoord(self):
        return self.coord
    
    def getHabits(self):
        return self.habits
    
    def setMatchingResult(self, matchingResult):
        self.matchingResult = matchingResult
    
    def getMatchingResult(self):
        return self.matchingResult