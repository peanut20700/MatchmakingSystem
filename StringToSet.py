class StringToSet:
    @staticmethod
    def stringToSet(string):
        li = string.split(',')
        retSet = set()
        for element in li:
            retSet.add(element)
        return retSet