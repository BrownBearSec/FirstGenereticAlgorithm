import random

class Selection():

    def __init__(self, fitness):
        self.fitness = fitness

    def selectFromPop(self):
        total = 0
        choice = 0
        catch = 0

        for i in range(0, len(self.fitness)):
            total = total + self.fitness[i][0]
        
        
        
        
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
                choice = i
                #print("Choice is")
                #print(choice)    
                break

        return choice     
        
                    
             
        
                    
            
                
