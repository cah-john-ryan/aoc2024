import src.day3.mull_it_over as mull
import pytest

def test_find_multipliers():
    result = mull.find_multipliers("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

    assert len(result) == 4
    assert "mul(2,4)" in result
    assert "mul(5,5)" in result
    assert "mul(11,8)" in result
    assert "mul(8,5)" in result

@pytest.mark.parametrize("test_input,expected", [("mul(2,4)", [2, 4]), ("mul(11,8)", [11,8])])
def test_parse_numbers_to_multiply(test_input, expected):
    result = mull.parse_numbers_to_multiply(test_input)

    assert result == expected

def test_parse_multipliers():
    result = mull.parse_multipliers("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

    assert len(result) == 4
    assert result[0] == [2, 4]
    assert result[1] == [5, 5]
    assert result[2] == [11, 8]
    assert result[3] == [8, 5]

def test_add_it_up():
    result = mull.add_it_up("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

    assert result == 161

def test_add_it_up_from_file():
    result = mull.add_it_up_from_file("data_sample.txt")

    assert result == 161