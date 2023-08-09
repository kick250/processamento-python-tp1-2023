import exercise_9


def test_valid_triangle_when_valid():
  exercise_9.is_valid_triangle(9, 22, 15)

def test_valid_triangle_when_invalid():
  exercise_9.is_valid_triangle(14, 40, 12)

def test_is_creatable_triangle_when_valid():
  result = exercise_9.is_creatable_triangle(6, 9, 22, 15)
  assert result == True

def test_is_creatable_triangle_when_invalid():
  result = exercise_9.is_creatable_triangle(14, 40, 12, 60)
  assert result == False