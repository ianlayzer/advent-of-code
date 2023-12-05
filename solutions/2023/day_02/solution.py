# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer

MAXES = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    def isGamePossible(self, gameStr):
        for setString in gameStr.split("; "):
            for subsetStr in setString.split(", "):
                numStr, color = subsetStr.split(" ")
                if int(numStr) > MAXES[color]:
                    return False
        return True
    
    def getMinimumSet(self, gameStr):
        cubesUsed = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for setString in gameStr.split("; "):
            for subsetStr in setString.split(", "):
                numStr, color = subsetStr.split(" ")
                cubesUsed[color] = max(cubesUsed[color], int(numStr))
        return cubesUsed
    
    def getPowerOfSet(self, cubeSet):
        product = 1
        for numCubes in cubeSet.values():
            product *= numCubes
        return product

    @answer(2237)
    def part_1(self) -> int:
        idSum = 0
        for line in self.read_input():
            gameNumStr, gameStr = line.split(": ")
            if self.isGamePossible(gameStr):
                idSum += int(gameNumStr[4:])
        return idSum

    @answer(66681)
    def part_2(self) -> int:
        powerSum = 0
        for line in self.read_input():
            gameStr = line.split(": ")[1]
            minimumSet = self.getMinimumSet(gameStr)
            powerSum += self.getPowerOfSet(minimumSet)
        return powerSum

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
