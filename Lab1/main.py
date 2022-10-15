import random
import logging
from itertools import combinations


class Problem:

    def __init__(self, N, seed):
        input_data = self.problem(N, seed)
        self.seed = seed
        self.input = self.makeAsDict(input_data)
        self.N = N
        self.size = len(self.input)
        self.min_number_of_el = self.size
        self.best_sol = None
        self.total_steps = 0
        self.visited_nodes = 0


    def problem(self, N, seed = None):
        random.seed(seed)
        return [
            list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
            for n in range(random.randint(N, N * 5))
        ]


    def makeAsDict(self, data):
        return {i : l for i, l in enumerate(data)}


    def solve(self):
        for n in range(3, 6):
            possible_solutions = combinations(range(self.size), n)
            for ps in possible_solutions:
                self.total_steps += 1
                number_of_elements = self.getNumberOfElements(ps)
                if number_of_elements < self.min_number_of_el and self.isSolution(ps):
                    self.min_number_of_el = number_of_elements
                    self.best_sol = ps
                    self.visited_nodes += 1
                    if self.min_number_of_el == self.N:
                        return   #I found the best solution
                    
    
    def isSolution(self, tuple):
        s = set()
        for index in tuple:
            s.update(self.input[index])
        return len(s) == self.N


    def getNumberOfElements(self, tuple):
        return sum([len(self.input[index]) for index in tuple])


if __name__ == '__main__':
    problems = {}
    seed = 42
    for n in [5, 10, 20, 100, 500, 1000]:
        problem = Problem(n, seed)
        problem.solve()
        problems[n] = problem
        logging.getLogger().setLevel(logging.INFO)
        logging.info(f"N = {n}, best solution: {problem.best_sol}, elements: {problem.min_number_of_el}, total steps: {problem.total_steps}")
