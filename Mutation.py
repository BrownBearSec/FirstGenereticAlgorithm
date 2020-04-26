import Population
import random

class Mutation():

    def __init__(self, population, rate):
        self.population = population
        self.rate = rate

    def mutate(self):
        length = len(self.population)
        amount = round((length/100) * self.rate)
        if (amount == 0):
            amount = 1
        for i in range(0, amount):
            del self.population[random.randint(0, len(self.population))]
        for i in range(0, amount):
            temp = []
            for i in range(0, len(t))
            temp.append()
            # ADD THE THING THAT ADDS A NEW RANDOM ARRAY IN ARRAY
        