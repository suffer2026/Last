import numpy as np
import random
import warnings
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)

#random.seed(42)
#np.random.seed(42)

# --------------------------------
n_samples = 30  

temp = np.random.uniform(160, 180, n_samples)
flow = np.random.uniform(10, 13, n_samples)
atomizer = np.random.uniform(18000, 23000, n_samples)
concentration = np.random.uniform(20, 26, n_samples)

X = np.column_stack((temp, flow, atomizer, concentration))

# Outputs: moisture, yield
# synthetic relationships + small noise
moisture = (
    8.0
    - 0.03 * temp
    + 0.08 * flow
    - 0.00003 * atomizer
    + 0.04 * concentration
    + np.random.normal(0, 0.08, n_samples)
)

yield_ = (
    25.0
    + 0.18 * temp
    - 0.6 * flow
    + 0.0007 * atomizer
    + 0.9 * concentration
    + np.random.normal(0, 1.0, n_samples)
)

Y = np.column_stack((moisture, yield_))

# --------------------------------
# Scale input and output
x_scaler = StandardScaler()
y_scaler = StandardScaler()

X_scaled = x_scaler.fit_transform(X)
Y_scaled = y_scaler.fit_transform(Y)

# Keep at least 2 test samples
X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y_scaled, test_size=0.4, random_state=42
)

# --------------------------------
# Fitness function
def fitness(params):
    pop_size, crossover_rate, mutation_rate = params

    # keep the network very small for this tiny dataset
    hidden_size = max(2, min(4, int(pop_size / 25)))

    # use GA params for useful NN hyperparameters
    alpha_value = mutation_rate * 0.1
    max_iter_value = int(500 + crossover_rate * 1500)

    model = MLPRegressor(
        hidden_layer_sizes=(hidden_size,),
        solver='lbfgs',
        alpha=alpha_value,
        max_iter=max_iter_value,
        random_state=42
    )

    model.fit(X_train, Y_train)
    pred = model.predict(X_test)

    return mean_squared_error(Y_test, pred)

# --------------------------------
# GA functions
def create_individual():
    return [
        random.randint(20, 100),      # population size
        random.uniform(0.6, 0.9),     # crossover rate
        random.uniform(0.01, 0.1)     # mutation rate
    ]

def crossover(p1, p2):
    return [
        random.choice([p1[0], p2[0]]),
        random.choice([p1[1], p2[1]]),
        random.choice([p1[2], p2[2]])
    ]

def mutate(ind):
    if random.random() < 0.3:
        ind[0] = random.randint(20, 100)
    if random.random() < 0.3:
        ind[1] = random.uniform(0.6, 0.9)
    if random.random() < 0.3:
        ind[2] = random.uniform(0.01, 0.1)
    return ind

# --------------------------------
# GA main loop
population = [create_individual() for _ in range(10)]

for generation in range(10):
    scores = [(fitness(ind), ind) for ind in population]
    scores.sort(key=lambda x: x[0])

    print(f"Generation {generation + 1} | Best MSE: {scores[0][0]:.6f}")

    selected = [ind for (_, ind) in scores[:5]]
    new_population = [selected[0][:]]

    while len(new_population) < 10:
        p1, p2 = random.sample(selected, 2)
        child = crossover(p1, p2)
        child = mutate(child)
        new_population.append(child)

    population = new_population

# --------------------------------
# Best GA parameters
final_scores = [(fitness(ind), ind) for ind in population]
best_score, best = min(final_scores, key=lambda x: x[0])

print("\nBest Parameters Found:")
print("Population Size:", best[0])
print("Crossover Rate:", round(best[1], 4))
print("Mutation Rate:", round(best[2], 4))

# --------------------------------
# Final model using best parameters
best_hidden_size = max(2, min(4, int(best[0] / 25)))
best_alpha = best[2] * 0.1
best_max_iter = int(500 + best[1] * 1500)

final_model = MLPRegressor(
    hidden_layer_sizes=(best_hidden_size,),
    solver='lbfgs',
    alpha=best_alpha,
    max_iter=best_max_iter,
    random_state=42
)
final_model.fit(X_train, Y_train)
Y_pred = final_model.predict(X_test)

print("\nFinal Model Performance:")
print("MSE:", round(mean_squared_error(Y_test, Y_pred), 6))
print("R2 Score:", round(r2_score(Y_test, Y_pred), 6))
