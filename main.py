from entities.item import Item
from entities.individuo import Individuo
from entities.AlgoritimoGenetico import AlgoritmoGenetico

    
    

produtos = [
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


items = [ Item(x['nome'], x['valor'], x['volume']) for x in produtos]

AlgoritmoGenetico.executar(items, 10,  10, 50)
