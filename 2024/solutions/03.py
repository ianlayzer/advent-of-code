from utils.base_solution import BaseSolution
import re

INSTRUCTION_PATTERN = r"(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))"

class Solution(BaseSolution):
    def solve_part_1(self) -> str:
        return self.solve(allow_disable_muls=False)
         
    def solve_part_2(self) -> str:
        return self.solve(allow_disable_muls=True)
    
    def solve(self, allow_disable_muls: bool) -> str:
        memory = ''.join(self.input)
        instructions = re.findall(INSTRUCTION_PATTERN, memory)

        muls_enabled = True
        result = 0
        for instruction in instructions:
            mul, do, dont = instruction
            if mul and muls_enabled:
                result += self.evaluate_mul(mul)
            elif not allow_disable_muls:
                continue
            elif do:
                muls_enabled = True
            elif dont:
                muls_enabled = False
        return result
        
    def evaluate_mul(self, mul_str: str) -> int:
        stripped = mul_str[4:-1]
        x_1, x_2 = stripped.split(",")
        return int(x_1) * int(x_2)