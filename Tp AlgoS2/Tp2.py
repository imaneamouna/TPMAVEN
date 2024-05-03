import random

class Tp1:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity

    def generate_random_stock(n):
        values = [random.randint(1, 10) for _ in range(n)]
        weights = [random.randint(1, 10) for _ in range(n)]
        return values, weights

    def calcule_ri(self):
        ri = [v / w for v, w in zip(self.values, self.weights)]
        sorted_indices = [idx + 1 for idx in sorted(range(len(ri)), key=lambda k: ri[k], reverse=True)]
        sorted_ri = sorted(ri, reverse=True)
        return sorted_ri, sorted_indices

    def solve(self):
        sorted_ri, sorted_indices = self.calcule_ri()
        total_weight = 0
        c = [0] * len(self.weights)

        for idx in sorted_indices:
            item_index = idx - 1
            item_weight = self.weights[item_index]
            if total_weight + item_weight <= self.capacity:
                c[item_index] = 1
                total_weight += item_weight

        return c, total_weight
    def fit(self, x):
        return sum(x[i] * self.values[i] for i in range(len(x)))

    def swap(self, i, j, c):
        
        c[i], c[j] = c[j], c[i]
        return c
    # recherche local
    def graspe(self):
        best_solution = None
        best_value = self.fit(self.solve())
        c = self.solve()
        n = len(self.solve())
        
        for i in range(1, 10):
                for j in range(i + 1, 10):
                    if c[i] != c[j]:
                        s_prime = self.swap(i, j, c)
                        value_s_prime = self.fit(s_prime)

                        new_total_weight = sum(w * s_prime[idx] for idx, w in enumerate(self.weights))
                        if new_total_weight <= self.capacity and value_s_prime > best_value:
                            best_solution = s_prime
                            best_value = value_s_prime

        return best_solution, best_value
    # ************************** local_search_iteration ******************************************************
def local_search_iteration(self, initial_solution, iterations):
    current_solution = initial_solution
    best_solution = initial_solution
    best_value = self.fit(initial_solution)

    for _ in range(iterations):
        for i in range(1, n):
            for j in range(i + 1, n):
                if current_solution[i] != current_solution[j]:
                    neighbor_solution = self.swap(i, j, current_solution)
                    neighbor_value = self.fit(neighbor_solution)

                    new_total_weight = sum(w * neighbor_solution[idx] for idx, w in enumerate(self.weights))
                    if new_total_weight <= self.capacity and neighbor_value > best_value:
                        best_solution = neighbor_solution
                        best_value = neighbor_value

        current_solution = best_solution

    total_value = self.fit(best_solution)  # Calculate fitness (total value)

    return best_solution, total_value






# Example usage:
n = 10  # Number of stocks
capacity = 8
values, weights = Tp1.generate_random_stock(n)
knapsack_instance = Tp1(weights, values, capacity)
# knapsack_instance = Tp1(weights, values, capacity)
solution, total_weight = knapsack_instance.solve()
GRASPE_solution, GRASPE_total_value = knapsack_instance.graspe()

print("Values of stocks:", values)
print("Weights of stocks:", weights)
print("C array (1 for included, 0 for not included):\n", solution)
print("Total weight of included stocks:", total_weight)
total_value = knapsack_instance.fit(solution)
print("Total value of included stocks:", total_value)
print("***************************************************************************")
print("GRASPE solution (1 for included, 0 for not included):\n", GRASPE_solution)
print("Total value of best solution:", GRASPE_total_value)

# Call the function
local_search_itere_solution, local_search_itere_total_value = knapsack_instance.local_search_iteration(initial_solution=solution, iterations=1000)

# Print results
print("Total value of included stocks:", GRASPE_total_value)
print("***************************************************************************")
print("GRASPE solution (1 for included, 0 for not included):\n", GRASPE_solution)
print("Total value of best solution:", GRASPE_total_value)