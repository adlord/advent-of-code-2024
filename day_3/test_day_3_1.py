from main_day_3_1 import get_multiply


def test_calculate_safe_count(tmp_path):
    input_file = tmp_path / "input.txt"
    input_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)
    +mul(32,64]then(mul(11,8)mul(8,5))"""
    input_file.write_text(input_data)

    result = get_multiply(str(input_file))
    print(result)
    assert result == 161