from entities.individuo import Individuo

def revert_compare(callback):
    return lambda i1, i2: callback(i1, i2) * -1

def compare_item(item1: "Individuo", item2: "Individuo") -> int:
    if item1.score == item2.score:
        return 0
    
    return 1 if item1.score > item2.score else -1