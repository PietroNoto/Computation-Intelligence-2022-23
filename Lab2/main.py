import random
import logging
from itertools import combinations
from genetic_algorithm import GA


class Problem:

    def __init__(self, N, seed):
        input_data = self.problem(N, seed)
        self.seed = seed
        self.input = self.makeAsDict(self.removeDuplicates(input_data))
        self.N = N
        self.size = len(self.input)
        self.min_number_of_el = self.size
        self.best_sol = None
        self.total_steps = 0


    def problem(self, N, seed = None):
        random.seed(seed)
        return [
            list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
            for n in range(random.randint(N, N * 5))
        ]


    def removeDuplicates(self, raw_data):
        list_of_tuples = [tuple(l) for l in raw_data]
        return set(list_of_tuples)


    def makeAsDict(self, data):
        return {i : l for i, l in enumerate(data)}


    def solve(self):
        for n in range(1, 6):
            possible_solutions = combinations(range(self.size), n)
            for ps in possible_solutions:
                self.total_steps += 1
                number_of_elements = self.getNumberOfElements(ps)
                if number_of_elements < self.min_number_of_el and self.isSolution(ps):
                    self.min_number_of_el = number_of_elements
                    self.best_sol = ps
                    if self.min_number_of_el == self.N:
                        return   #I found the best solution
                    
    
    def solve_GA(self, PROBLEM_SIZE, POPULATION_SIZE, OFFSPRING_SIZE, NUM_GENERATIONS):
        EPOCHS = 1
        num_of_el = 0
        #iterate over epochs to produce several populations in order to maximize the chances
        #to get more suitable individuals that lead to more optimal solutions
        for e in range(EPOCHS):
            #generate a population
            genomes = GA(PROBLEM_SIZE = PROBLEM_SIZE, POPULATION_SIZE = POPULATION_SIZE, OFFSPRING_SIZE = OFFSPRING_SIZE, NUM_GENERATIONS = NUM_GENERATIONS)
            genomes.populate()
            genomes.evolve()
            #once I got the population I'm gonna inspect each individual and search for a potential solution.
            genomes.population = self.removeDuplicates([t[0] for t in genomes.population])
            for individual in sorted(genomes.population, key = lambda t: sum(t)):
                self.total_steps += 1
                num_of_el = self.getNumberOfElementsBitmap(individual)
                #take into consideration only tuples that potentially improve the best so far
                #which, of course, have also to cover the set
                if num_of_el < self.min_number_of_el and self.isSolutionBitmap(individual):
                    self.best_sol = individual
                    self.min_number_of_el = num_of_el
        return


    def isSolution(self, tuple):
        s = set()
        for index in tuple:
            s.update(self.input[index])
        return len(s) == self.N


    def isSolutionBitmap(self, tuple):
        s = set()
        for index, val in enumerate(tuple):
            if val == 1:
                s.update(self.input[index])
        return len(s) == self.N


    def getNumberOfElements(self, tuple):
        return sum([len(self.input[index]) for index in tuple])

    
    def getNumberOfElementsBitmap(self, tuple):
        return sum([len(self.input[index]) for index, val in enumerate(tuple) if val == 1])


if __name__ == '__main__':
    problems = {}
    seed = 42
    POPULATION_SIZE = 10**6
    OFFSPRING_SIZE = 10
    NUM_GENERATIONS = 100

    for n in [25]:
        problem = Problem(n, seed)
        logging.getLogger().setLevel(logging.INFO)
        logging.info(f"Computing solution for N = {n}...")
        problem.solve_GA(PROBLEM_SIZE = problem.size, POPULATION_SIZE = POPULATION_SIZE, OFFSPRING_SIZE = OFFSPRING_SIZE, NUM_GENERATIONS = NUM_GENERATIONS)
        problems[n] = problem
        logging.info(f"N = {n}, best solution: {problem.best_sol}, elements: {problem.min_number_of_el}, visited nodes: {problem.total_steps}")
