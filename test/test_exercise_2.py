import spec
import exercise_2

def print_test():
  exercise_2.favorite_book("Padrões de Projeto")

def test_favorite_book():
  expected_message = "Um dos meus livros favoritos é Padrões de Projeto\n"
  spec.expect_print(print_test, expected_message)
