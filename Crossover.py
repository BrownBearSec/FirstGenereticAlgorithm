import Target
import random


class Crossover():

    def __init__(self, population,  firstChoice, secondChoice):
        self.firstChoice = firstChoice
        self.secondChoice = secondChoice
        self.target = Target.Target.getTarget()
        self.population = population
        self.newPopulation = []

    def crossover(self):
        #creates new population, empty
        #for i in range(0, len(self.population)):
            
            #print(self.newPopulation)
            #print(self.population)
           
            
        #gives values to empty array similar to first and second choices
        for i in range(0, len(self.population)):
            temp = []
            for j in range(0, len(self.population)):
                temp.append(chr(random.randint(ord(self.population[self.firstChoice][j]) - 5, ord(self.population[self.firstChoice][j]) + 5)))
            self.newPopulation.append(temp)
        #print(self.newPopulation)
                
        return(self.newPopulation)