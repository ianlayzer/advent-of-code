import importlib

from args import RunnerArgumentParser

if __name__=="__main__":
    args = RunnerArgumentParser()
    year, day, part, example = args.year, args.day, args.part, args.example

    day_str = str(day) if day > 9 else f"0{day}"
    solution_module = importlib.import_module(f"{year}.solutions.{day_str}")

    solution = solution_module.Solution(year, day, example)
    result = solution.solve_part(part)

    print(f"Part {part}:")
    print(result)
    

    
