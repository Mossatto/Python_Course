nome = "Matheus"
idade = 25
profissao = "dev"
linguagem = "python"
PI = 3.14159

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e eestou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e eestou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {nombre}. Eu tenho {age} anos de idade, trabalho como {ocupation} e eestou matriculado no curso de {language}.".format(nombre = nome,age = idade, ocupation = profissao, language = linguagem))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e eestou matriculado no curso de {linguagem}.")
print(f"O valor de PI: {PI:.2f}")
