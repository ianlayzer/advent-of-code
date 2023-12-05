# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import StrSplitSolution, answer
import math

class Card:
    def __init__(self, num, winningNumbers, myNumbers):
        self.num = num
        self.winningNumbers = winningNumbers
        self.myNumbers = myNumbers
        self.matches = list(set(myNumbers).intersection(winningNumbers))
        self.cardsWon = [self.num + i for i in range(1, len(self.matches) + 1)]

def getNumbers(cardString):
    return list(filter(lambda c: c, cardString.split(" ")))

def makeCard(cardStr):
    cardNumStr, numbersStrs = cardStr.split(": ")
    cardNum = int(cardNumStr[4:])
    winningNumbersStr, myNumbersStr = numbersStrs.split(" | ")
    return Card(cardNum, getNumbers(winningNumbersStr), getNumbers(myNumbersStr))

def makeCards(lines):
    return list(map(makeCard, lines))

def getScore(card):
    numMatches = len(card.matches)
    return int(math.pow(2, numMatches - 1)) if numMatches > 0 else 0

class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(33950)
    def part_1(self) -> int:
        return sum(list(map(getScore, makeCards(self.read_input()))))
    
    @answer(14814534)
    def part_2(self) -> int:
        cards = makeCards(self.read_input())
        cardMap = {}
        for card in cards:
            cardMap[card.num] = card

        numCards = 0
        stack = list(cardMap.keys())
        while len(stack):
            currCardNum = stack.pop()
            stack += cardMap[currCardNum].cardsWon
            numCards += 1
        return numCards

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
