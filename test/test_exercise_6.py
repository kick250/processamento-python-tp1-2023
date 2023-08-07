from exercise_6 import f


def test_function_f():
  v = [1]*5 + [2]*3 + [3]*4
  assert f(v, 2) == 3