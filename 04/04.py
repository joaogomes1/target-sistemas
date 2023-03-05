### Autor: João Ricardo de Souza Gomes

Dict = [ {"estado": "SP", "faturamento" : 67836.43},
         {"estado": "RJ", "faturamento" : 36678.66},
         {"estado": "MG", "faturamento" : 29229.88},
         {"estado": "ES", "faturamento" : 27165.48},
         {"estado": "Outros", "faturamento" : 19849.53} ]

valor_total_mensal = 0

# calcula valor total mensal
for i in range(0, len(Dict)):
    valor_total_mensal += Dict[i]["faturamento"]

# calcula e exibe os percentuais
for i in range(0, len(Dict)):
    estado = Dict[i]["estado"]
    faturamento = Dict[i]["faturamento"]
    percentual = round(faturamento/valor_total_mensal * 100, 2)
    print(estado + " " + str(percentual) + "%")
