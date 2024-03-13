texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
vogal_encontrada = False


for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        vogal_encontrada = True

if not vogal_encontrada:
    print("Não existe vogal no texto")

    
print()