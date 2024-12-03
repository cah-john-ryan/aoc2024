from src.day2.red_nosed_reports import get_count_of_safe_reports, get_count_of_safe_reports_from_file

def test_part1_sample_data():
    sample_data = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]

    result = get_count_of_safe_reports(sample_data)

    assert result == 2

def test_part1_sample_data_from_file():
    result = get_count_of_safe_reports_from_file("data_sample.txt")

    assert result == 2