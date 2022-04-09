import pytest

from . import translate_to_onp

class TestONP:
    @pytest.mark.parametrize(
        "in_data, expected_result",
        [
            ("3+2", "3 2 +"),
            ("3+2*5", "3 2 5 * +"),
            ("((2+3)*5-7)/6", "2 3 + 5 * 7 - 6 /"),
            ("2*(5+2)", "2 5 2 + *"),
            ("(7+3)*(5-2)^2", "7 3 + 5 2 - 2 ^ *"),
            ("4/(3-1)^(2*3)", "4 3 1 - 2 3 * ^ /"),
            ("(4/((3*3)-1)^(2*(3/4)))^2", "4 3 3 * 1 - 2 3 4 / * ^ / 2 ^"),
        ]
    )
    def test_should_translate_to_onp(self, in_data, expected_result):
        assert translate_to_onp(in_data) == expected_result

    @pytest.mark.parametrize(
        "in_data, expected_result",
        [
            ("3 + 2", "3 2 +"),
            ("3 + 2 * 5", "3 2 5 * +"),
            ("  ( ( 2 +3)*   5 -7 ) /   6", "2 3 + 5 * 7 - 6 /"),
        ]
    )
    def test_clean_spaces(self, in_data, expected_result):
        assert translate_to_onp(in_data) == expected_result
