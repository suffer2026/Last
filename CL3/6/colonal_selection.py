import numpy as np
import random

random.seed(42)
np.random.seed(42)

# --------------------------------
# Objective function to minimize
def objective_function(x):
    return np.sum(np.array(x) ** 2)

# --------------------------------
# Create a random antibody (solution)
def create_antibody(dim, bounds):
    return [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]

# --------------------------------
# Mutation: stronger mutation for worse antibodies,
# weaker mutation for better antibodies
def mutate(antibody, mutation_rate, bounds):
    mutated = []
    for i, val in enumerate(antibody):
        new_val = val + np.random.normal(0, mutation_rate)
        new_val = max(bounds[i][0], min(bounds[i][1], new_val))
        mutated.append(new_val)
    return mutated

# --------------------------------
# Clonal Selection Algorithm
def clonal_selection_algorithm(
    objective_func,
    dim,
    bounds,
    population_size=20,
    selected_size=5,
    clone_factor=5,
    generations=50,
    base_mutation=0.5
):
    # Initial population
    population = [create_antibody(dim, bounds) for _ in range(population_size)]

    best_solution = None
    best_fitness = float("inf")

    for generation in range(generations):
        # Evaluate antibodies
        scored_population = [(objective_func(ab), ab) for ab in population]
        scored_population.sort(key=lambda x: x[0])

        # Track best
        if scored_population[0][0] < best_fitness:
            best_fitness = scored_population[0][0]
            best_solution = scored_population[0][1]

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness:.6f}")

        # Select best antibodies
        selected = scored_population[:selected_size]

        clones = []

        # Clone and mutate selected antibodies
        for rank, (fitness, antibody) in enumerate(selected):
            num_clones = clone_factor * (selected_size - rank)

            # Better antibodies get smaller mutation
            mutation_rate = base_mutation * (rank + 1) / selected_size 

            for _ in range(num_clones):
                clone = mutate(antibody, mutation_rate, bounds)
                clones.append(clone)

        # Evaluate clones
        scored_clones = [(objective_func(cl), cl) for cl in clones]
        scored_clones.sort(key=lambda x: x[0])

        # Keep best individuals from clones
        new_population = [ab for (_, ab) in scored_clones[:population_size - 2]]

        # Add a few random antibodies for diversity
        while len(new_population) < population_size:
            new_population.append(create_antibody(dim, bounds))

        population = new_population

    return best_solution, best_fitness

# --------------------------------
# Example usage
dimension = 5
bounds = [(-5, 5)] * dimension

best_sol, best_fit = clonal_selection_algorithm(
    objective_func=objective_function,
    dim=dimension,
    bounds=bounds,
    population_size=20,
    selected_size=5,
    clone_factor=5,
    generations=35,
    base_mutation=0.5
)

print("\nBest Solution Found:")
print(best_sol)
print("Best Fitness:", best_fit)
