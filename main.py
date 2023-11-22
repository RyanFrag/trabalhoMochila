from entities.item import Item
from entities.individuo import Individuo
from entities.AlgoritimoGenetico import AlgoritmoGenetico
import matplotlib.pyplot as plt
import copy

def adicionar_item(conjunto_itens, novo_item):
    novo_conjunto = copy.deepcopy(conjunto_itens)
    novo_conjunto.append(novo_item)
    return novo_conjunto

def remover_item(conjunto_itens, indice_item):
    novo_conjunto = copy.deepcopy(conjunto_itens)
    del novo_conjunto[indice_item]
    return novo_conjunto


def executar_e_analisar(items, limite_espaco, n_populacao, n_geracao):
    melhores_por_geracao, melhor_global = AlgoritmoGenetico.executar(items, limite_espaco, n_populacao, n_geracao)
    melhor_resultado = melhor_global

    print(f"Melhor resultado para {len(items)} itens:")
    print(f"Cromossomo: {melhor_resultado.cromossomo}")
    print(f"Valor total na mochila: {melhor_resultado.preco_total}")
    print(f"Volume total na mochila: {melhor_resultado.volume_total}")
    print("\n")

    plotar_grafico(melhores_por_geracao)



def criar_itens(conjunto):
    return [Item(x['nome'], x['valor'], x['volume']) for x in conjunto]

def executar_algoritmo_genetico(itens, limite_espaco, n_populacao, n_geracao):
    return AlgoritmoGenetico.executar(itens, limite_espaco, n_populacao, n_geracao)

def plotar_grafico(resultados):
    geracoes = list(range(1, len(resultados) + 1))
    valores_totais = [individuo.preco_total for individuo in resultados]

    plt.plot(geracoes, valores_totais, marker='o', linestyle='-')
    plt.title('Evolução do Preço Total na Mochila por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Preço Total na Mochila')
    plt.grid(True)
    plt.show()

produtos_original  = [
     {'nome': " Arroz " ,  'volume':  1.11 , 'valor' : 4.75 },
     {'nome': " Feijao " ,  'volume':  1.25 , 'valor' : 8.00 },
     {'nome': " Farinha de trigo " ,  'volume':  1.67  , 'valor' : 5.50 },
     {'nome': " Acucar" ,  'volume':  1.67  , 'valor' : 3.50 },
     {'nome': "Sal" ,  'volume':  1.25  , 'valor' : 1.50},
     {'nome': "Oleo de cozinha" , 'volume':  0.46  , 'valor' : 4.50},
     {'nome': "Cafe" ,  'volume':  0.9 , 'valor' : 4.50 },
     {'nome': " Leite " ,  'volume':  1.00 , 'valor' : 3.75 },
     {'nome': " Manteiga " ,  'volume':  0.54  , 'valor' : 11.50 },
     {'nome': " Pao " ,  'volume':  1.75  , 'valor' : 10.00 },
     {'nome': " Massas " ,  'volume':  1.33  , 'valor' : 7.50 },
     {'nome': " Enlatados " ,  'volume':  0.33  , 'valor' : 6.00 },
     {'nome': " Sabao " ,  'volume':  0.22  , 'valor' : 3.00 },
     {'nome': " Papel Higienico " ,  'volume':  3.24   , 'valor' : 4.50 },
]

items_original = [Item(x['nome'], x['valor'], x['volume']) for x in produtos_original]

# Adicionar Macarrão ao Conjunto
novo_item_macarrao = {'nome': "Macarrao", 'volume': 1.20, 'valor': 6.00}
produtos_com_macarrao = adicionar_item(produtos_original, novo_item_macarrao)
items_com_macarrao = [Item(x['nome'], x['valor'], x['volume']) for x in produtos_com_macarrao]

# Remover Farinha de Trigo do Conjunto
indice_remover_farinha = 2
produtos_sem_farinha = remover_item(produtos_original, indice_remover_farinha)
items_sem_farinha = [Item(x['nome'], x['valor'], x['volume']) for x in produtos_sem_farinha]

# Parâmetros para o Algoritmo Genético
limite_espaco = 10
n_populacao = 20
n_geracao = 50

# Executar e analisar para cada conjunto
executar_e_analisar(items_original, limite_espaco, n_populacao, n_geracao)
executar_e_analisar(items_com_macarrao, limite_espaco, n_populacao, n_geracao)
executar_e_analisar(items_sem_farinha, limite_espaco, n_populacao, n_geracao)