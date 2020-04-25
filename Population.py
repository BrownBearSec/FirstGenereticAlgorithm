import random

class Population():

    def __init__(self, size):
        self.size = size

    def randomChar(self):
        belowAbove = random.choice([True, False])
        if (belowAbove):
            randomChar = chr(random.randint(65, 90))  
        else:
            randomChar = chr(random.randint(97,122))

        return randomChar

    def getPopulations(self):
        population = []
        for i in range(0, self.size):
            population.append([])
            
        for j in range(0, self.size):
            for i in range(0, self.size):
                population[j].append(self.randomChar()) 
        return population

    