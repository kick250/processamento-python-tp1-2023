import re


VOWEL_REGEXP = r'[aeiouAEIOU]'
PERFECT = "perfeita"
PAIR = "par"
CRUSADE = "cruzada"
SHELL = "concha"
FREE = "livre"

class InvalidPoemLength(Exception):
  @property
  def message():
    return "Tamanho de poema invalido."

def is_vowel(letter):
  return re.match(VOWEL_REGEXP, letter)

def get_phonetic_part_from_verse(verse):
  verse = verse.strip()
  last_index = len(verse) - 1
  for index in range(last_index, 0, -1):
    letter = verse[index]
    if is_vowel(letter):
      return verse[index:len(verse)]
    if letter.isspace():
      return verse[index:len(verse)].strip()
  return verse.strip()

def get_poem_type(poem):
  if len(poem) != 4: raise InvalidPoemLength()
  phonetic_part_1 = get_phonetic_part_from_verse(poem[0])
  phonetic_part_2 = get_phonetic_part_from_verse(poem[1])
  phonetic_part_3 = get_phonetic_part_from_verse(poem[2])
  phonetic_part_4 = get_phonetic_part_from_verse(poem[3])

  if phonetic_part_1 == phonetic_part_2 and phonetic_part_3 == phonetic_part_4 and phonetic_part_2 == phonetic_part_3:
    return PERFECT
  elif phonetic_part_1 == phonetic_part_2 and phonetic_part_3 == phonetic_part_4 and phonetic_part_2 != phonetic_part_3:
    return PAIR
  elif phonetic_part_1 == phonetic_part_3 and phonetic_part_2 == phonetic_part_4 and phonetic_part_2 != phonetic_part_3:
    return CRUSADE
  elif phonetic_part_1 == phonetic_part_4 and phonetic_part_2 == phonetic_part_3 and phonetic_part_2 != phonetic_part_4:
    return SHELL
  else:
    return FREE

def main():
  try:
    lines = []
    for i in range(1, (4 + 1)):
      lines.append(
        input(f"Qual a {i} linha? ")
      )
  except InvalidPoemLength as e:
    print(e.message)

  poem = tuple(lines)
  poem_type = get_poem_type(poem)
  print(f"O tipo de rima é {poem_type}.")


if __name__ == "__main__":
  main()