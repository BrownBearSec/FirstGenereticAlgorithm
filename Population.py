import Target
import random

class Population():

    def __init__(self, size):
        self.size = size
        self.target = Target.Target.getTarget()
        self.population = []

    def randomChar(self):
        belowAbove = random.choice([True, False])
        if (belowAbove):
            randomChar = chr(random.randint(65, 90))  
        else:
            randomChar = chr(random.randint(97,122))

        return randomChar

    def getPopulations(self):
            
        for j in range(0, self.size):
            temp = []
            for i in range(0, len(self.target)):
                temp.append(self.randomChar())
            self.population.append(temp) 
                
        print("INITIAL population is")
        print(self.population)
        return self.population

    