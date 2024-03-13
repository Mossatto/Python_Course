month = int(input("Insira o numero do mês: "))

months_dict = {
    1: "january",
    2: "february",
    3: "march" ,
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december"
}

nome_do_mes = months_dict.get(month).title()
print(nome_do_mes)
