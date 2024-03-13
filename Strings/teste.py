N = int(input("Insira a quantidade de casos de teste: "))
contador = 0


while(N > contador):
    a = str(input(f"Insira o valor de A para o caso {contador + 1}(até 1000 digitos): "))
    b = str(input(f"Insira o valor de B para o caso {contador + 1}(até 1000 digitos): "))

    if int(a) <= 0 or int(b) <=0:
        print("insira um número maior que 0")
        continue
    if len(a) > 1000  or len(b) > 1000:
        print("Por favor insira um número válido")
        continue

    len_b = int(len(b))
   
    ultimos_caracteres_a = a[-(len_b):]
    

    if ultimos_caracteres_a == b:
        print("encaixa")
    else:
        print("não encaixa")

    contador += 1

