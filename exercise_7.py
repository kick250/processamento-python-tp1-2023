def count_names(sentences_string):
  results = []

  sentences = get_sentences(sentences_string)

  for sentence in sentences:
    results.append(
      count_names(sentence)
    )

  return results

def get_sentences(string_with_sentences):
  pass

def count_names_from_sentence(sentence):
  pass

def main():
  sentence = "Spavas li Mirno del Potro Juan martine?" # 4
  for result in count_names(sentence):
    print(result)

  sentence = "An4 voli Milovana. Ana nabra par Banana." #	1 2?
  for result in count_names(sentence):
    print(result)


if __name__ == "__main__":
  main()