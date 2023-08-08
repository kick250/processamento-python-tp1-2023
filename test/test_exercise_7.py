import spec
import exercise_7


def test_count_names_from_sentence():
  result = exercise_7.count_names_from_sentence("Ana nabra par Banana.")
  assert result == 2

def test_get_sentences():
  sentences = exercise_7.get_sentences("An4 voli Milovana. Ana nabra par Banana.")
  assert len(sentences) == 2
  assert sentences == (
    "An4 voli Milovana",
    "Ana nabra par Banana"
  )

def test_execute_with_1_sentences():
  result = exercise_7.count_names("Ana nabra par Banana.")
  assert result == [2]

def test_execute_with_2_sentences():
  result = exercise_7.count_names("An4 voli Milovana. Ana nabra par Banana.")
  assert result == [1, 2]