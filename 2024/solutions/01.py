from collections import Counter

from utils.base_solution import BaseSolution

class Solution(BaseSolution):
    def solve_part_1(self) -> str:
        left, right = self.make_columns(self.input)
        total_distance = 0
        for i in range(len(left)):
            total_distance += abs(left[i] - right[i])
        return str(total_distance)
    
    def solve_part_2(self) -> str:
        left, right = self.make_columns(self.input)
        counts = Counter(right)
        total_similarity = 0
        for num in left:
            total_similarity += num * counts[num]
        return total_similarity

    def make_columns(self, lines) -> list[list[int]]:
        split_lines = [l.split() for l in lines]
        columns = [[], []]
        left, right = columns
        for left_number, right_number in split_lines:
            left.append(int(left_number))
            right.append(int(right_number))
        columns = [sorted(col) for col in columns]
        return columns
    