
from  entities.individuo import Individuo
from entities.vetorOrdenado import OrderedVector
from entities.utils import revert_compare, compare_item

class AlgoritmoGenetico:
    @staticmethod
    def executar(itens, limite_espaco, n_populacao, n_geracao):
        populacao = OrderedVector(n_populacao, revert_compare(compare_item))
        melhores = []

        for x in range(n_populacao):
            populacao.insert(Individuo(itens, limite_espaco))

        for i in range(1, n_geracao):
            nova_populacao = OrderedVector(n_populacao, revert_compare(compare_item))
            melhores.append(populacao.get(0))

            metade = n_populacao // 2

            for index in range(metade):
                index_order = index
                index_pre_order = metade - index - 1

                individuo1 = populacao.get(index_order)
                individuo2 = populacao.get(index_pre_order)

                filho1, filho2 = individuo1.crossover(individuo2)

                nova_populacao.insert(filho1)
                nova_populacao.insert(filho2)

            populacao = nova_populacao

        melhores.append(populacao.get(0))
        return melhores
