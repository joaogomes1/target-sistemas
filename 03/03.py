### Autor: João Ricardo de Souza Gomes

import os
import json
 
# setar caminhos
this_path = os.path.abspath(__file__)
json_path = os.path.dirname(this_path) + "\\dados.json"

# abrir arquivo json
with open(json_path) as json_arq:
    dados = json.load(json_arq)
    valores = list() # para cálculos gerais
    valores_nao_nulos = list() # para cálculo da média
    media = 0
    dias_faturamento_superior_media = 0
 
    # popular listas
    for i in range(0, len(dados)):
        val = dados[i]["valor"]

        if ( val != 0 ):
            valores_nao_nulos.append(val) # para cálculo da média

        valores.append(val) # para cálculos gerais


    ### Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
    
    # média
    media = sum(valores_nao_nulos) / len(valores_nao_nulos)
    for i in range(0, len(valores_nao_nulos)):
        if valores_nao_nulos[i] > media:
            dias_faturamento_superior_media += 1


    ### saídas
    print("menor valor:", min(valores))
    print("menor valor não-nulo:", min(valores_nao_nulos))
    print("maior valor:", max(valores))
    print("número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", dias_faturamento_superior_media)
