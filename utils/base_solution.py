from abc import ABCMeta, abstractmethod

class BaseSolution(object, metaclass=ABCMeta):
    @abstractmethod
    def solve_part_1(self) -> str:
        pass
        
    @abstractmethod
    def solve_part_2(self) -> str:
        pass

    def __init__(self, year: int, day: int, example: bool):
        self.year = year
        self.day = day
        self.input = self.get_input(example)


    def get_input(self, example: bool) -> list[str]:
        year_str = str(self.year)
        day_str = str(self.day) if self.day > 9 else f"0{str(self.day)}"
        file_str = "example.txt" if example else "input.txt"

        path = f"{year_str}/inputs/{day_str}/{file_str}"
        with open(path) as f:
            return [l.strip() for l in f.readlines()]
        
    def solve_part(self, part: int) -> str:
        if part == 1:
            return self.solve_part_1()
        elif part == 2:
            return self.solve_part_2()
