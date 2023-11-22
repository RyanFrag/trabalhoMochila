from entities.individuo import Individuo
from entities.vetorOrdenado import OrderedVector
from entities.utils import revert_compare, compare_item

class AlgoritmoGenetico:
    @staticmethod
    def executar(itens, limite_espaco, n_populacao, n_geracao):
        populacao = OrderedVector(n_populacao, revert_compare(compare_item))
        melhores_por_geracao = []
        melhor_global = None

        for x in range(n_populacao):
            populacao.insert(Individuo(itens, limite_espaco))

        for i in range(n_geracao):
            nova_populacao = OrderedVector(n_populacao, revert_compare(compare_item))
            melhores_por_geracao.append(populacao.get(0))

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

            melhor_atual = populacao.get(0)
            if melhor_global is None or melhor_atual.preco_total > melhor_global.preco_total:
                melhor_global = melhor_atual

        return melhores_por_geracao, melhor_global
