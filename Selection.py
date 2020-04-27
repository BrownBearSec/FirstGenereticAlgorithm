import random
import Target

class Selection():

    def __init__(self, fitness):
        self.fitness = fitness
        self.target = Target.Target.getTarget()

    def selectFromPop(self):

        #ATTEMPT 1

        total = 0
        firstChoice = 0
        secondChoice = 0
        catch = 0



        # for i in range(0, len(self.fitness)):
        #     total = total + self.fitness[i][0]

        # print("Total is ")
        # print(total)
        
        # if (total == 0):
        #     total = 1
        
        
        
        # cumulative = [[0 for i in range(1)] for j in range(len(self.fitness))]
        # percentage = [[0 for i in range(1)] for j in range(len(self.fitness))]
        # for i in range(0, len(self.fitness)):
           
        #     percentage[i][0] = cumulative[i][0] + round((self.fitness[i][0]/total)*100)
        #     if (i != 0):
        #         cumulative[i][0]= cumulative[i - 1][0] + percentage[i-1][0]
        # #print("Cumulative is")
        # #print(cumulative)
        # #print("Percentage is")
        # #print(percentage)


        # maximum = max(max(x) for x in percentage)
        # #print("Max value is")
        # #print(maximum)

        # randomChoice = random.randint(0, maximum)

        # #print("random choice is ")
        # #print(randomChoice)

   
        # for i in range(0, len(percentage)):

        #     if(randomChoice <= percentage[i][0]):
        #         if (catch == 0):
        #             firstChoice = i
        #         if (catch == 1):
        #             secondChoice = i
        #         #print("Choice is")
        #         #print(choice)    
        #         if (catch == 2):
        #             break
        #         catch = catch + 1

        # return firstChoice, secondChoice
        


        # #ATTEMPT 2
    
        # fitnessValue = Target.Target.getFitnessValue()
        

        # for j in range(0, len(self.fitness)):
        #     cap = fitnessValue * len(self.target)
        #     for i in range(0, len(self.fitness)):
        #         if (self.fitness[i][0] == cap):
        #             firstChoice = i
        #             break
        #     cap = cap - fitnessValue

        # del self.fitness[firstChoice]

        # for j in range(0, len(self.fitness)):
        #     for i in range(0, len(self.fitness)):
        #         if (self.fitness[i][0] == cap):
        #             secondChoice = i 
        #             break
        #     cap = cap - fitnessValue

        # return firstChoice, secondChoice
                    
        #ATTEMPT 3

        # print("Fitness")
        # print(self.fitness)
        
        maximum = max(max(x) for x in self.fitness)
        # print("MAXIMUM IS")
        # print(maximum)

        firstChoice = self.fitness.index([maximum])
        del self.fitness[maximum]
        secondMaximum = max(max(x) for x in self.fitness)
        secondChoice = self.fitness.index([secondMaximum])

        # print("second MAXIMUM IS")
        # print(secondMaximum)


        return firstChoice, secondChoice, maximum