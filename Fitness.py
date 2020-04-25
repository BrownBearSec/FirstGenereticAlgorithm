import Target

class Fitness():

    def __init__(self, population):
        self.population = population
        self.target = Target.Target.getTarget()
        self.zeroList = [0]
        self.dump = []
        self.fitness = [[0 for i in range(1)] for j in range(len(self.target))]

            

    def getFitness(self):
        for i in range(0, len(self.population)):
            for j in range(0,len(self.population[0])):
                if (ord(self.population[i][j]) == ord(self.target[j])):
                    self.dump.append(2)
                # if the ascii value of the char is in +- 5 range of target
                elif (ord(self.target[j]) - 5 <= ord(self.population[i][j]) and ord(self.target[j]) + 5 >= ord(self.population[i][j])):
                    self.dump.append(1)
                else:
                    self.dump.append(0)

        #print(self.dump)
      


        for j in range(0, len(self.fitness) - 1):
            # selects each appropriate fraction of dump, starts from zero, goes to max          
            for i in range(round((len(self.dump) / len(self.population)))*j, round((len(self.dump) / len(self.population)))*(j + 1) ):
                self.fitness[j][0] = self.fitness[j][0] + self.dump[i] 
                #print(self.fitness)

        return self.fitness
    
