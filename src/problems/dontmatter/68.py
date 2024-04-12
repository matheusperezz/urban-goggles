def eh_ordenada(palavra):
  for i in range(len(palavra) - 1):
    if palavra[i] > palavra[i + 1]:
      return False
  return True

numero_palavras = int(input())

for _ in range(numero_palavras):
  palavra = input()
  resultado = "O" if eh_ordenada(palavra) else "N"
  print(f"{palavra}: {resultado}")
