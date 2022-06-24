from MatchmakingSystem import MatchmakingSystem
from DistanceBasedMatchmakingStrategy import DistanceBasedMatchmakingStrategy
from HabitBasedMatchmakingStrategy import HabitBasedMatchmakingStrategy
from ObversePickingStrategy import ObversePickingStrategy
from ReversePickingStrategy import ReversePickingStrategy
from Gender import Gender
from Individual import Individual


if __name__ == '__main__':
    matchmakingSystem = MatchmakingSystem(HabitBasedMatchmakingStrategy(), ReversePickingStrategy())
    matchmakingSystem.addIndividual(
        Individual(
            id = 1,
            gender = Gender.MALE,
            age = 18,
            intro = "大家好我是一號",
            habits = "吃飯,睡覺,打東東",
            coord = [1,1]
        )
    )

    matchmakingSystem.addIndividual(
        Individual(
            id = 2,
            gender = Gender.FEMALE,
            age = 20,
            intro = "大家好我是二號",
            habits = "吃飯,睡覺,玩遊戲",
            coord = [10,10]
        )
    )

    matchmakingSystem.addIndividual(
        Individual(
            id = 3,
            gender = Gender.MALE,
            age = 22,
            intro = "大家好我是三號",
            habits = "吃飯,玩遊戲,散步",
            coord = [2,1]
        )
    )

    matchmakingSystem.addIndividual(
        Individual(
            id = 4,
            gender = Gender.FEMALE,
            age = 24,
            intro = "大家好我是四號",
            habits = "吃飯,睡覺,打東東",
            coord = [5,5]
        )
    )

    matchmakingSystem.match()
    matchmakingSystem.pickResultForIndividual()
    matchmakingSystem.printMatchingResultForIndivodual()
    