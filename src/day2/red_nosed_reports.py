from enum import Enum

from src.utilities.file_processing import read_lines_from_file

def get_count_of_safe_reports(input_data):
    count_of_safe_reports = 0
    for input_line in input_data:
        if is_report_safe(input_line):
            count_of_safe_reports += 1
    return count_of_safe_reports

class ReportDirection(Enum):
    INCREASING = 0
    DECREASING = 1

def is_report_safe(input_line):
    report_levels = [int(x) for x in input_line.split(' ')]
    direction = ReportDirection.DECREASING if report_levels[0] > report_levels[-1] else ReportDirection.INCREASING
    previous_level = report_levels[0]
    for report_level in report_levels[1:]:
        if abs(previous_level - report_level) < 1 or 3 < abs(previous_level - report_level):
            return False
        if direction == ReportDirection.INCREASING and previous_level > report_level:
            return False
        elif direction == ReportDirection.DECREASING and previous_level < report_level:
            return False
        previous_level = report_level
    return True

def get_count_of_safe_reports_from_file(file_name):
    input_data = read_lines_from_file(file_name)
    return get_count_of_safe_reports(input_data)

if __name__ == '__main__':
    part1_result = get_count_of_safe_reports_from_file('data.txt')
    print(f"day2 part 1 result: {part1_result}")