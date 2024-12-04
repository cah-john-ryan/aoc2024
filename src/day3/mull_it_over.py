import re

from src.utilities.file_processing import read_lines_from_file


def find_multipliers(input_string: str) -> list[str]:
    match = re.findall(r"mul[(][0-9]{1,3}[,][0-9]{1,3}[)]", input_string)
    return match

def parse_numbers_to_multiply(multiplier_as_string: str) -> list[int]:
    return [int(x) for x in multiplier_as_string[4:-1].split(",")]

def parse_multipliers(input_string: str) -> list[list[int]]:
    multipliers = find_multipliers(input_string)
    results = []
    for multiplier in multipliers:
        results.append(parse_numbers_to_multiply(multiplier))
    return results

def add_it_up(input_string: str) -> int:
    multipliers = parse_multipliers(input_string)
    result = 0
    for multiplier in multipliers:
        result += multiplier[0] * multiplier[1]
    return result

def add_it_up_from_file(file_name: str) -> int:
    input_data = read_lines_from_file(file_name)
    total_value = 0
    for input_line in input_data:
        total_value += add_it_up(input_line)
    return total_value

if __name__ == "__main__":
    part_1_result = add_it_up_from_file("data.txt")
    print(f"Part 1 result: {part_1_result}")