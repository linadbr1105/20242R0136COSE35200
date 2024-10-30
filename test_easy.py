import calculator as cal


def test_add():
  assert cal.add(3, 5) == 8

def test_multiply():
  assert cal.multiply(8, 8) == 64

def test_abs_diff():
  assert cal.abs_diff(8, 4) == 4
