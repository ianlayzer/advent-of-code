import argparse
from datetime import datetime

class RunnerArgumentParser:  
    def __init__(self):
        today = datetime.today()
        parser = argparse.ArgumentParser()
        parser.add_argument("-y", "--year", type=int, default=today.year)
        parser.add_argument("-d", "--day", type=int, default=today.day)
        parser.add_argument("-p", "--part", type=int, default=1, choices=[1, 2])
        parser.add_argument("-e", "--example", action="store_true")
        self.args = parser.parse_args()
    
    @property
    def year(self) -> int:
        return self.args.year
    
    @property
    def day(self) -> int:
        return self.args.day
    
    @property
    def part(self) -> int:
        return self.args.part
    
    @property
    def example(self) -> bool:
        return self.args.example
