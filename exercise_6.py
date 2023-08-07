def f(a, b):
  """
  Remove o paramento b enviado do array enviado como primeiro parametro, retornando quantos foram removidos.
  a => Array que sera removido o elemento
  b => elemento que sera removido
  """
  r = 0
  while b in a:
    a.remove(b)
    r += 1
  return r


if __name__ == "__main__":
  v = [1]*5 + [2]*3 + [3]*4
  f(v, 2)

  help(f)