import random

random_zero_or_one = lambda _x: random.choice([0,1])
random_0_100 = lambda _x: random.randint(0, 100)

class Individuo () :
    def __init__ ( self , itens ,limite_de_espacos , geracao=0, cromossomos=None) :
        self.itens = itens
        self.limite_de_espacos = limite_de_espacos
        self.geracao = geracao
        self.cromossomo = cromossomos if cromossomos else self.criar_cromossomo(len(itens))
        self.score, self.volume_total, self.preco_total  = self.get_info(self.cromossomo, itens, limite_de_espacos)



    def criar_cromossomo(self, tamanho):
        lista_cromossomo = []
        for i in range(0, tamanho):
             lista_cromossomo.append(random_zero_or_one(0))
        return lista_cromossomo
    
    def get_info(self, cromossomos, itens, limite_espaco):
        volume_total = 0
        valor_total  = 0
        for index, i in enumerate(itens):
            if cromossomos[index] == 1: 
               volume_total += i.volume
               valor_total += i.valor
        if volume_total > limite_espaco:
            return 1, volume_total, valor_total
        
        return valor_total, volume_total, valor_total
    def crossover(self, individuo: "Individuo"):
        index = random.randint(0, len(self.cromossomo))
        filho1 = self.cromossomo[:index] + individuo.cromossomo[index:]
        filho2 = individuo.cromossomo[:index] + self.cromossomo[index:]

        return (
            Individuo(
                self.itens,
                self.limite_de_espacos,
                self.geracao + 1,
                self.mutacao()  # Remova o argumento aqui
            ),
            Individuo(
                self.itens,
                self.limite_de_espacos,
                self.geracao + 1,
                self.mutacao() 
            ),
        )
    
    def mutacao(self):
        mutacao_taxa = 80
        novo_cromossomo = []
        for i in self.cromossomo:
            x = i
            if mutacao_taxa >= random_0_100(0):
                x = 1 if x == 0 else 0  

            novo_cromossomo.append(x)

        return novo_cromossomo

    def __str__(self) -> str:
        return self.cromossomo.__str__()