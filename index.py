try:
  valor = int(input('Insira o valor a ser sacado: ')) # 1000, 1200, 1250
  notas = [n.strip() for n in input('Insira as notas: ').split(',')] # 200, 100, 50, 20, 10, 5, 2
  
  for i in notas:
    if i.isnumeric() and int(i) <= valor:
      quantidade = int(valor / int(i))
      print(f'Total: {quantidade} notas de {i}')
except:
  print('Insira um valor válido.')
