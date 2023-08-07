import spec
import exercise_1

def test_print_message():
  expected_message = "O melhor curso do mundo!!!\n"
  spec.expect_print(exercise_1.print_message, expected_message)
