# Generated using @xavdid"s AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer
import re



DIGIT_MAP = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

DIGIT_PATTERNS = list(map(re.compile, DIGIT_MAP.keys()))

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1
        
    def findDigitsNumeric(self, line):
        return re.findall(r"[1-9]", line)
    
    def findDigitsNumericAndSpelled(self, line):
        matchesAtIndex = [None for _ in range(len(line))]
        for pattern in DIGIT_PATTERNS:
            matchIter = re.finditer(pattern, line)
            for m in matchIter:
                matchStartPos = m.span()[0]
                matchString = m.group(0)
                matchesAtIndex[matchStartPos] = DIGIT_MAP[matchString]
        matches = list(filter(lambda m: m != None, matchesAtIndex))
        return matches 

    def findCalibrationValues(self, lines, findDigits):
        calibrationValues = []
        for line in lines:
            digits = findDigits(line)
            calibrationValue = int(digits[0] + digits[-1])
            calibrationValues.append(calibrationValue)
        return calibrationValues
    
    @answer(54940)
    def part_1(self) -> int:
        lines = self.read_input()
        return sum(self.findCalibrationValues(lines, self.findDigitsNumeric))

    @answer(54208)
    def part_2(self) -> int:
        lines = self.read_input()
        return sum(self.findCalibrationValues(lines, self.findDigitsNumericAndSpelled))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
