import re

def is_name(word):
  if len(word) == 0: return False

  for letter in word:
    if letter.isdecimal(): return False
  if word[-1].isupper(): return False

  return word[0].isupper()

def remove_empty_strings(sentences):
  def not_empty(sentence):
    return len(sentence.strip()) != 0
  return list(filter(not_empty, sentences))

def count_names(full_sentence):
  sentences = get_sentences(full_sentence)
  results = []
  for sentence in sentences:
    results.append(count_names_from_sentence(sentence))
  return results

def get_sentences(string_with_senteses):
  DELEMITERS_REGEXP = r'[.?!]'
  sentences = re.split(DELEMITERS_REGEXP, string_with_senteses)
  return remove_empty_strings(sentences)

def count_names_from_sentence(sentence):
  words = sentence.split(" ")

  return len(tuple(filter(is_name, words)))

def main():
  sentence = "Spavas li Mirno del Potro Juan martine?" # 4
  for result in count_names(sentence):
    print(result)

  sentence = "An4 voli Milovana. Ana nabra par Banana." #	1 2?
  for result in count_names(sentence):
    print(result)


if __name__ == "__main__":
  main()