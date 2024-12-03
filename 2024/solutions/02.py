from utils.base_solution import BaseSolution

class Solution(BaseSolution):
    def solve_part_1(self) -> str:
        return self.find_safe_reports(allow_removal=False)
         
    def solve_part_2(self) -> str:
        return self.find_safe_reports(allow_removal=True)

    def find_safe_reports(self, allow_removal: bool) -> str:
        reports = self.get_reports_from_input()
        safe_count = 0
        for report in reports:
            if allow_removal and self.is_report_safe_with_removal(report):
                safe_count += 1
            elif not allow_removal and self.is_report_safe(report):
                safe_count += 1
        return safe_count

    def get_reports_from_input(self) -> list[list[int]]:
        reports = []
        for line in self.input:
            report = []
            for s in line.split():
                report.append(int(s))
            reports.append(report)
        return reports

    def is_report_safe_with_removal(self, report: list[int]) -> bool:
        for i in range(len(report)):
            report_with_element_i_removed = report[:i] + report[i+1:]
            if self.is_report_safe(report_with_element_i_removed):
                return True
        return False

    def is_report_safe(self, report: list[int]) -> bool:
        is_increasing = report[0] < report[1]
        for i in range(len(report) - 1):
            left, right = report[i : i + 2]
            if not self.is_acceptable_sequence(left, right, is_increasing):
                return False
        return True
    
    def is_acceptable_sequence(self, left: int, right: int, is_increasing: bool) -> bool:
        if is_increasing:
            if right < left + 1 or right > left + 3:
                return False
        elif right > left - 1 or right < left - 3:
                return False
        return True
