numeros = set([1,2,3,1,3,4])
print(numeros)

fruta = set("abacaxi")
print(fruta)

carros = set(("palio","corsa","palio","gol"))
print(carros)

#conjuntos não aceitam indexação nem fatiamento, precisa converter para lista

carros_list = list(carros)

print(carros_list[0])
