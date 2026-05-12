import random
import numpy as np
from deap import base, creator, tools, algorithms
import multiprocessing
from multiprocessing.pool import ThreadPool as Pool

DIMENSIONS = 7
BOUNDS = (-5, 5)

def fitness_function(individual):
    return (sum(x**2 for x in individual),)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("attr_float", random.uniform, BOUNDS[0], BOUNDS[1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, DIMENSIONS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fitness_function)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def evolve_island(seed, generations=5):
    random.seed(seed)

    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)
    log = []

    for gen in range(generations):
        offspring = algorithms.varAnd(pop, toolbox, cxpb=0.7, mutpb=0.2)
        fits = list(map(toolbox.evaluate, offspring))

        for ind, fit in zip(offspring, fits):
            ind.fitness.values = fit

        pop = toolbox.select(offspring, k=len(pop))
        hof.update(pop)

        best = hof[0]
        log.append((gen, best.fitness.values[0]))

    return pop, hof[0], log


def migrate(islands):
    islands = [list(i) for i in islands]

    for i in range(len(islands)):
        next_i = (i + 1) % len(islands)

        best_individual = islands[i][1]

        # Replace worst individual in next island
        worst_idx = max(
            range(len(islands[next_i][0])),
            key=lambda j: islands[next_i][0][j].fitness.values[0]
        )

        islands[next_i][0][worst_idx] = best_individual

    return islands


NUM_ISLANDS = 2
pool = Pool(processes=NUM_ISLANDS)

results = pool.map(evolve_island, range(NUM_ISLANDS))
results = [list(r) for r in results]

for i, (_, best, log) in enumerate(results):
    print(f"\nIsland {i} Log:")
    for gen, fit in log:
        print(f"Gen {gen+1} | Fitness: {fit:.4f}")

results = migrate(results)

best = min([res[1] for res in results], key=lambda ind: ind.fitness.values[0])

print("\nBest Individual:", [round(x, 4) for x in best])
print("Best Fitness:", best.fitness.values[0])
