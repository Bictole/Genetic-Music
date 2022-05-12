from random import sample

def generate_weighted_distribution(population, fitness_func):
    result = []

    for gene in population:
        result += [gene] * int(fitness_func(gene)+1)

    return result

def population_fitness(population, fitness_func):
    return sum([fitness_func(genome) for genome in population])


def selection_pair(population, fitness_func):
    return sample(
        population=generate_weighted_distribution(population, fitness_func),
        k=2
    )