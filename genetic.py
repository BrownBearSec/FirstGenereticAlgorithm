#To change target change value in target and pop size must be <=

#To do list:
#Initalise population - tick
#Fitness function - tick
#Selection - tick
#Crossover - tick
#Mutation

import Population
import Fitness
import Selection
import Crossover

p = Population.Population(6)
population = p.getPopulations()

f = Fitness.Fitness(population)
fitness = f.getFitness()

s = Selection.Selection(fitness)
firstChoice = s.selectFromPop()

del fitness[firstChoice]

s2 = Selection.Selection(fitness)
secondChoice = s2.selectFromPop()

c = Crossover.Crossover(population, firstChoice, secondChoice)
population = c.crossover()

print("population is")
print(population)
print("Fitness is")
print(fitness)
print("first choice is")
print(firstChoice)
print(population[firstChoice])
print("second choice is")
print(secondChoice)
print(population[secondChoice])