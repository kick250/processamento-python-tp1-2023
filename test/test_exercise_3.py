import spec
import exercise_3

def print_test():
  exercise_3.create_shirt("M", "Padrões de Projeto")

def test_create_shirt():
  spec.expect_print(print_test, "Camisa tamanha M\nMensagem: Padrões de Projeto\n")




