#To change target change value in target and pop size must be <=

#To do list:
#Initalise population - tick
#Fitness function - tick
#Selection - tick
#Crossover - tick
#Mutation - 

import sys
import Population
import Fitness
import Selection
import Crossover
import Target
import Mutation

target = Target.Target.getTarget()
catch = 0
generations = 0

p = Population.Population(100)
population = p.getPopulations()

while(True):

    # for i in range(0, len(population)):
    #     combined = ""
    #     for j in range(0, len(target)):
    #         combined = combined.join(population[i])
    #         # print("COMBINED IS")
    #         # print(combined)
    #         if (combined == target):
    #             print("Its Done!")
    #             sys.exit()


    f = Fitness.Fitness(population)
    fitness = f.getFitness()

    s = Selection.Selection(fitness)
    firstChoice, secondChoice, maximum = s.selectFromPop()


    c = Crossover.Crossover(population, firstChoice, secondChoice)
    population = c.crossover()

    m = Mutation.Mutation(population, 10)
    population = m.mutate()

    if (catch == 1):

        print("--------------------------------------------------------------------")
        print("Program is finished!")
        print("--------------------------------------------------------------------")
        print("Final fitness: ")
        print(fitness)
        print("--------------------------------------------------------------------")
        print("Result: ")
        result = "".join(population[firstChoice])
        print(result)
        print("--------------------------------------------------------------------")
        print("It took the following amount of generations: ")
        print(generations)
        sys.exit()

    if (maximum == Target.Target.getFitnessValue()*len(target)):
        catch = 1
        

    print("new population is")
    print(population)
    print("Fitness is")
    print(fitness)
    print("first choice is")
    print(firstChoice)
    print(population[firstChoice])
    print("second choice is")
    print(secondChoice)
    print(population[secondChoice])
    generations = generations + 1