# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import StrSplitSolution, answer

import re
from collections import defaultdict

GEAR = "*"

def isSymbol(val):
    return val and bool(re.match(r"[^(0-9|\.)]", val))

def isDigit(val):
    return val and val.isnumeric()

class Schematic:
    def __init__(self, grid):
        self.grid = grid
        self.numRows = len(grid)
        self.numCols = len(grid[0])

    def isInRange(self, row, col):
        return row >= 0 and row < self.numRows and col >= 0 and col < self.numCols
    
    def getValue(self, row, col):
        if self.isInRange(row, col):
            return self.grid[row][col]
        else:
            return None
        
    def getNeighbors(self, row, col):
        neighbors = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                val = self.getValue(r, c)
                if val:
                    neighbors.append((val, r, c))
        return neighbors

    def __str__(self):
        return "\n".join(map(lambda row: row.__str__(), self.grid))
    
def makeSchematic(lines):
    grid = [list(l) for l in lines]
    return Schematic(grid)

def findNumbersToAdjacentSymbols(schematic):
    numberToAdjacentSymbols = {}
    for row in range(schematic.numRows):
        currentNumber = ""
        adjacentSymbols = set()
        for col in range(schematic.numCols):
            val = schematic.getValue(row, col)
            if isDigit(val):
                currentNumber += val
                for neighbor in schematic.getNeighbors(row, col):
                    neighborVal, _, _ = neighbor
                    if isSymbol(neighborVal):
                        adjacentSymbols.add(neighbor)    
            elif len(currentNumber):
                numberToAdjacentSymbols[(int(currentNumber), row, col)] = adjacentSymbols
                currentNumber = ""
                adjacentSymbols = set()
        if len(adjacentSymbols):
            numberToAdjacentSymbols[(int(currentNumber), row, col)] = adjacentSymbols
            currentNumber = ""
    return numberToAdjacentSymbols

def findPartNumbers(schematic):
    partNumbers = []
    for numberTuple, adjacentSymbols in findNumbersToAdjacentSymbols(schematic).items():
        if len(adjacentSymbols):
            partNumbers.append(numberTuple[0])
    return partNumbers

def findGears(schematic):
    numberToAdjacentSymbols = findNumbersToAdjacentSymbols(schematic)
    symbolsToAdjacentNumbers = defaultdict(set)
    for numTuple, adjacentSymbols in numberToAdjacentSymbols.items():
        for symbolTuple in adjacentSymbols:
            symbolsToAdjacentNumbers[symbolTuple].add(numTuple)
    
    gears = []
    for symbolTuple, adjacentNumbers in symbolsToAdjacentNumbers.items():
        if symbolTuple[0] == GEAR and len(adjacentNumbers) == 2:
            gears.append((symbolTuple, adjacentNumbers))
    return gears

def computeGearRatio(gear):
    ratio = 1
    for numTuple in gear[1]:
        ratio *= numTuple[0]
    return ratio

def findGearRatios(schematic):
    return map(computeGearRatio, findGears(schematic)) 

class Solution(StrSplitSolution):
    _year = 2023
    _day = 3
                
    @answer(514969)
    def part_1(self) -> int:
        schematic = makeSchematic(self.read_input())
        partNumbers = findPartNumbers(schematic)
        return sum(partNumbers)

    @answer(78915902)
    def part_2(self) -> int:
        schematic = makeSchematic(self.read_input())
        gearRatios = findGearRatios(schematic)
        return(sum(gearRatios))

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass