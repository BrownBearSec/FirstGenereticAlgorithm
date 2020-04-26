#To change target change value in target and pop size must be <=

#To do list:
#Initalise population - tick
#Fitness function - tick
#Selection - tick
#Crossover - tick
#Mutation - 

import Population
import Fitness
import Selection
import Crossover
import Target

target = Target.Target.getTarget()

p = Population.Population(100)
population = p.getPopulations()

for x in range(0, 10):

    for i in range(0, len(population)):
        for j in range(0, len(target)):
            if ("".join(population[i][j]) == target):
                print("Its Done!")
                break


    f = Fitness.Fitness(population)
    fitness = f.getFitness()

    s = Selection.Selection(fitness)
    firstChoice, secondChoice = s.selectFromPop()


    c = Crossover.Crossover(population, firstChoice, secondChoice)
    population = c.crossover()

    print("Fitness is")
    print(fitness)
    print("new population is")
    print(population)
    print("first choice is")
    print(firstChoice)
    print(population[firstChoice])
    print("second choice is")
    print(secondChoice)
    print(population[secondChoice])