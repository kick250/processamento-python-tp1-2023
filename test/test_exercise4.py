import spec
import exercise_4


def test_create_shirt_with_size():
  def print_test():
    exercise_4.create_shirt(size = "M")

  spec.expect_print(print_test, "Camisa tamanha M\nMensagem: I ♡ Python\n")

def test_create_shirt_with_message():
  def print_test():
    exercise_4.create_shirt(message = "Bom dia")

  spec.expect_print(print_test, "Camisa tamanha G\nMensagem: Bom dia\n")

def test_create_shirt_with_size_and_message():
  def print_test():
    exercise_4.create_shirt(size="P", message = "Bom dia")

  spec.expect_print(print_test, "Camisa tamanha P\nMensagem: Bom dia\n")

