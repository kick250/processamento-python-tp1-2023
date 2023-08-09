def is_valid_triangle(value1, value2, value3):
  if not ((value1 + value2) > value3):
    return False
  if not ((value1 + value3) > value2):
    return False
  if not ((value2 + value3) > value1):
    return False
  return True

def is_creatable_triangle(value1, value2, value3, value4):
  possibilities = (
    (value1, value2, value3),
    (value2, value3, value4),
    (value1, value3, value4),
    (value1, value2, value4),
  )

  for possibility in possibilities:
    if is_valid_triangle(possibility[0], possibility[1], possibility[2]):
      return True
  return False

def main():
  values = []
  for i in range(4):
    values.append(
      int(input(f"Qual o valor da vareta {i}? "))
    )
  if is_creatable_triangle(values[0], values[1], values[2], values[3]):
    print("S")
  else:
    print("N")


if __name__ == "__main__":
  main()