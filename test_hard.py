import calculator as cal


def test_add_list():
  assert cal.add(3, 5, 9, 10, 38) == 65

def test_multiply_negative():
  assert cal.multiply(8, -8) == -64

def test_abs_diff_negative():
  assert cal.abs_diff(8, -4) == 12
