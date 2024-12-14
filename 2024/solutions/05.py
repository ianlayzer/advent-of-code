from utils.base_solution import BaseSolution
from collections import defaultdict
from functools import cmp_to_key

class Solution(BaseSolution):
    def solve_part_1(self) -> str:
        must_come_before, updates = self.parse_input()

        result = 0
        for update in updates:
            if self.is_update_correct_ordered(update, must_come_before):
                middle_num = update[len(update) // 2]
                result += middle_num
        return result

    def solve_part_2(self) -> str:
        must_come_before, updates = self.parse_input()

        def compare(x, y):
            if x in must_come_before[y]:
                return -1
            elif y in must_come_before[x]:
                return 1
            else:
                return 0
            
        result = 0
        for update in updates:
            sorted_update = sorted(update, key=cmp_to_key(compare))
            if str(update) != str(sorted_update):
                middle_num = sorted_update[len(update) // 2]
                result += middle_num
        return result

    def is_update_correct_ordered(self, update: list[int], must_come_before: defaultdict[list[int]]) -> bool:
        bad_numbers = set()
        for num in update:
            if num in bad_numbers:
                return False
            else:
                for new_bad in must_come_before[num]:
                    bad_numbers.add(new_bad)
        return True
                

    def parse_input(self) -> tuple[list[int], list[int]]:
        def map_int(strings: list[str]) -> list[int]:
            return list(map(lambda s: int(s), strings))
        
        rules, updates = [], []
        parsing_rules = True
        for line in self.input:
            if line == '':
                parsing_rules = False
            elif parsing_rules:
                rules.append(map_int(line.split("|")))
            else:
                updates.append(map_int(line.split(",")))

        must_come_before = defaultdict(list[int])
        for left, right in rules:
            must_come_before[right].append(left)

        return must_come_before, updates
                
