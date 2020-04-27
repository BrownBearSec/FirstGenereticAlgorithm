import Population
import random
import Target

class Mutation():

    def __init__(self, population, rate):
        self.population = population
        self.rate = rate
        self.target = Target.Target.getTarget()

    def mutate(self):
        length = len(self.population)
        amount = round((length/100) * self.rate)
        if (amount == 0):
            amount = 1
        for i in range(0, amount):
            randomChromosome = random.randint(0, len(self.population) - 1)
            randomGene = random.randint(0, len(self.target)-1)
            #print(randomChromosome)
            #print(randomGene)
            self.population[randomChromosome][randomGene] = Population.Population.randomChar(self)

        # print("MUTATED GENE IS")
        # print(randomChromosome)
        # print(randomGene)
            
        return self.population