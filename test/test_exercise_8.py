import exercise_8

def test_get_phonetic_part_from_verse():
  verse = "It seems though"
  phonetic_part = exercise_8.get_phonetic_part_from_verse(verse)

  assert phonetic_part == "ugh"

  verse = "I say to you boo"
  phonetic_part = exercise_8.get_phonetic_part_from_verse(verse)
  assert phonetic_part == "o"

  verse = "but summer is not"
  phonetic_part = exercise_8.get_phonetic_part_from_verse(verse)
  assert phonetic_part == "ot"

def test_perfect_poem():
  poem = (
    "I say to you boo",
    "You say boohoo",
    "I cry too",
    "It is too much foo"
  )

  assert exercise_8.get_poem_type(poem) == exercise_8.PERFECT

def test_pair_poem():
  poem = (
    "It seems though",
    "that without some dough",
    "creating such a bash",
    "is a weighty in terms of cash"
  )

  assert exercise_8.get_poem_type(poem) == exercise_8.PAIR


def test_crusade_poem():
  poem = (
    "One plus one is small",
    "one hundred plus one is not",
    "you might be very tall",
    "but summer is not"
  )

  assert exercise_8.get_poem_type(poem) == exercise_8.CRUSADE


def test_shell_poem():
  poem = (
    "Your teacher has to mark",
    "and mark and mark and teach",
    "To do well on this contest you have to reach",
    "for everything with a lark"
  )

  assert exercise_8.get_poem_type(poem) == exercise_8.SHELL


def test_free_poem():
  poem = (
    "But how I see",
    "the problem so fair",
    "is to write subtle verse",
    "with hardly a rhyme"
  )

  assert exercise_8.get_poem_type(poem) == exercise_8.FREE
