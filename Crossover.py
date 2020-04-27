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
        
        self.newPopulation.append(self.population[self.firstChoice])

        for j in range(0, len(self.population) - 1):
            temp = []
            for i in range(0, len(self.target)):
              
                switch = bool(random.getrandbits(1))
                if (switch):
                    temp.append(self.population[self.firstChoice][i])
                else:
                    temp.append(self.population[self.secondChoice][i])
               
            self.newPopulation.append(temp)

    

     
        #OLD VERSION THAT CAUSED PROGRAM RANDOM CONFUSION - BAD

        #gives values to empty array similar to first and second choices
        # for i in range(0, len(self.population)):
        #     temp = []
        #     for j in range(0, len(self.population)):

        #         selectionTemp = random.randint(ord(self.population[self.firstChoice][j]) - 3, ord(self.population[self.firstChoice][j]) + 3)
        #         if (selectionTemp >= 32 and selectionTemp <= 122):
        #             temp.append(chr(selectionTemp))
        #         else:
        #             temp.append(self.population[self.firstChoice][j])
          
        #     self.newPopulation.append(temp)
        # #print(self.newPopulation)

        
        return(self.newPopulation)