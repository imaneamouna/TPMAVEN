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

# Example usage:
n = 10  # Number of stocks
capacity = 8
values, weights = Tp1.generate_random_stock(n)
knapsack_instance = Tp1(weights, values, capacity)
# knapsack_instance = Tp1(weights, values, capacity)
solution, total_weight = knapsack_instance.solve()


print("Values of stocks:", values)
print("Weights of stocks:", weights)
print("C array (1 for included, 0 for not included):\n", solution)
print("Total weight of included stocks:", total_weight)
total_value = knapsack_instance.fit(solution)
print("Total value of included stocks:", total_value)
