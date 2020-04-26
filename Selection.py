import random

class Selection():

    def __init__(self, fitness):
        self.fitness = fitness

    def selectFromPop(self):
        total = 0
        firstChoice = 0
        secondChoice = 0
        catch = 0

        for i in range(0, len(self.fitness)):
            total = total + self.fitness[i][0]
        
        if (total == 0):
            total = 1
        
        
        
        cumulative = [[0 for i in range(1)] for j in range(len(self.fitness))]
        percentage = [[0 for i in range(1)] for j in range(len(self.fitness))]
        for i in range(0, len(self.fitness)):
           
            percentage[i][0] = cumulative[i][0] + round((self.fitness[i][0]/total)*100)
            if (i != 0):
                cumulative[i][0]= cumulative[i - 1][0] + percentage[i-1][0]
        #print("Cumulative is")
        #print(cumulative)
        #print("Percentage is")
        #print(percentage)


        maximum = max(max(x) for x in percentage)
        #print("Max value is")
        #print(maximum)

        randomChoice = random.randint(0, maximum)

        #print("random choice is ")
        #print(randomChoice)

   
        for i in range(0, len(percentage)):

            if(randomChoice <= percentage[i][0]):
                if (catch == 0):
                    firstChoice = i
                if (catch == 1):
                    secondChoice = i
                #print("Choice is")
                #print(choice)    
                if (catch == 2):
                    break
                catch = catch + 1

        return firstChoice, secondChoice
        
                    
             
        
                    
            
                
