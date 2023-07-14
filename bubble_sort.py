def bubble_sort(lista):
  """Implementação da abordagem de ordenação "bubble sort" em Python.

  Args:
    lista: Lista a ser ordenada.

  Returns:
    Uma lista ordenada.
  """
  n = len(lista)
  for i in range(n):
    for j in range(n - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]

  return lista

if __name__ == "__main__":
  lista = [5, 3, 1, 2, 4]
  print(f"Lista Original: {lista}")
  lista = bubble_sort(lista)
  print(f"Lista Ordenada: {lista}")
