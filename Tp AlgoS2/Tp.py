import random


class Tp:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity

    @staticmethod
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
        help = c[i]
        c[i] = c[j]
        c[j] = help
        return c


    def graspe(self, iterations=1000):
      best_solution = None
      best_value = float('-inf')
      c = self.solve()[0]
  
      for _ in range(iterations):
          for i in range(1, len(c)):
              for j in range(i + 1, len(c)):
                  if c[i] != c[j]:
                      s_prime = self.swap(i, j, c)
                      value_s_prime = self.fit(s_prime)
  
                      new_total_weight = sum(w * s_prime[idx] for idx, w in enumerate(self.weights))
                      if new_total_weight <= self.capacity and value_s_prime > best_value:
                          best_solution = s_prime.copy()  # Make a copy to preserve the best solution
                          best_value = value_s_prime

      return best_solution, best_value
    def print_results_table(self, solution, total_weight, total_value):
        headers = ["Stock", "Value", "Weight", "Included"]
        data = list(zip(headers, *zip(range(1, len(self.values) + 1), self.values, self.weights, solution)))
        max_len = max(len(header) for header, *_ in data)
        for header, *items in data:
            print(f"{header:<{max_len}}: {' '.join(str(item) for item in items)}")
        print("Total weight of included stocks:", total_weight)
        print("Total value of included stocks:", total_value)
# Example usage:
n = 10  # Number of stocks
capacity = 8
values, weights = Tp.generate_random_stock(n)
knapsack_instance = Tp(weights, values, capacity)
solution, total_weight = knapsack_instance.solve()
total_value = knapsack_instance.fit(solution)

print("Original Solution:")
knapsack_instance.print_results_table(solution, total_weight, total_value)

GRASPE_solution, GRASPE_total_value = knapsack_instance.graspe()

print("\nGRASPE Solution:******************************")
# print("*************************************************************")
knapsack_instance.print_results_table(GRASPE_solution, total_weight, GRASPE_total_value)
# print("GRASPE solution (1 for included, 0 for not included):\n", GRASPE_solution)
# print("Total value of best solution:", GRASPE_total_value)