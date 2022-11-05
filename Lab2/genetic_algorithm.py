import logging
from collections import namedtuple
import random
#from matplotlib import pyplot as plt


# PROBLEM_SIZE = 500
# POPULATION_SIZE = 5
# OFFSPRING_SIZE = 3
# NUM_GENERATIONS = 100


class GA:

    def __init__(self, PROBLEM_SIZE, POPULATION_SIZE, OFFSPRING_SIZE, NUM_GENERATIONS):
        self.Individual = namedtuple("Individual", ["genome", "fitness"])
        self.PROBLEM_SIZE = PROBLEM_SIZE
        self.POPULATION_SIZE = POPULATION_SIZE
        self.OFFSPRING_SIZE = OFFSPRING_SIZE
        self.NUM_GENERATIONS = NUM_GENERATIONS
        self.population = []


    def onemax(self, genome):
        return sum(genome)


    def tournament(self, tournament_size = 2):
        return max(random.choices(self.population, k = tournament_size), key = lambda i: i.fitness)


    def cross_over(self, g1, g2):
        cut = random.randint(0, self.PROBLEM_SIZE)
        return g1[:cut] + g2[cut:]


    def mutation(self, g):
        point = random.randint(0, self.PROBLEM_SIZE - 1)
        return g[:point] + (1 - g[point],) + g[point + 1 :]

    
    def populate(self):
        for genome in [tuple([random.choice([1, 0]) for _ in range(self.PROBLEM_SIZE)]) for _ in range(self.POPULATION_SIZE)]:
            self.population.append(self.Individual(genome, self.onemax(genome)))
        #logging.info(f"init: pop_size={len(self.population)}; max={max(self.population, key=lambda i: i.fitness)[1]}")


    def evolve(self):
        fitness_log = [(0, i.fitness) for i in self.population]
        for g in range(self.NUM_GENERATIONS):
            offspring = list()
            for i in range(self.OFFSPRING_SIZE):
                if random.random() < 0.3:
                    p = self.tournament()
                    o = self.mutation(p.genome)
                else:
                    p1 = self.tournament()
                    p2 = self.tournament()
                    o = self.cross_over(p1.genome, p2.genome)
                f = self.onemax(o)
                fitness_log.append((g + 1, f))
                offspring.append(self.Individual(o, f))
            self.population += offspring
            self.population = sorted(self.population, key = lambda i: i.fitness, reverse = False)

