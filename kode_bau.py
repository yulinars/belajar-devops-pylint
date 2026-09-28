def calculate_value(a, b, c, numbers, value):
    """Melakukan perhitungan sederhana."""
    base_value = 10
    increment = 1
    offset = 0

    if a and not b and c is None:
        try:
            result = numbers[0] + value + increment + offset
            print(result)
            return base_value + result
        except (IndexError, TypeError):
            return None

    return None


calculate_value(True, False, None, [2], 3)