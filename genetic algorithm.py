#%%

import random
import numpy as np
import matplotlib.pyplot as plt

def f(w,x,y,z):
    return w**3 + x**2 - y**2 - z**2 + 2*y*z - 3*w*x + w* z - x * y + 2

def bin_to_dec(list_bin):
    # convert the number into list of bits

    decimal = 0
    for i in range(len(list_bin)):
        #returns the rightmost bit in the binary string
        digit = list_bin.pop()
        if digit == '1':
            decimal += pow(2, i)
    return decimal

def evaluation(solution):
    w = bin_to_dec(solution[0:4])
    x = bin_to_dec(solution[4:8])
    y = bin_to_dec(solution[8:12])
    z = bin_to_dec(solution[12:16])
    return f(w,x,y,z)

def generate_pop(n):
    population= []
    for i in range(n):
        solution = []
        # generate for w
        w = []
        for i in range(4):
            if random.random() < 0.5:
                w.append('1')
            else:
                w.append('0')

        # generate for x
        x = []
        for i in range(4):
            if random.random() < 0.5:
                x.append('1')
            else:
                x.append('0')

        # generate for y
        y = []
        for i in range(4):
            if random.random() < 0.5:
                y.append('1')
            else:
                y.append('0')

        # generate for z
        z = []
        for i in range(4):
            if random.random() < 0.5:
                z.append('1')
            else:
                z.append('0')

        solution = w + x + y + z
        population.append(solution)
    return population

def averaging(added, fitness):
    increased = [x + added for x in fitness]
    average = sum(increased) / len(increased)
    averaging = [x / average for x in increased]
    return averaging

def substring_swap(solution1, solution2):
    dimension = len(solution1)
    index1 = random.randint(0, dimension - 1)
    index2 = random.randint(0, dimension - 1)
    #the positions should not be the same
    while index1 == index2:
        index2 = random.randint(0, dimension - 1)

    if index1 < index2:
        left = index1
        right = index2
    else:
        left = index2
        right = index1

    baby1 = solution1[0:left] + solution2[left:right + 1] + solution1[right + 1:dimension]
    baby2 = solution2[0:left] + solution1[left:right + 1] + solution2[right + 1:dimension] 

    return baby1, baby2

def mutation(solution):
    dimension = len(solution)
    index1 = random.randint(0, dimension - 1)
    new_sol = solution
    if new_sol[index1] == '1':
        new_sol[index1] = '0'
    else:
        new_sol[index1] = '1'
    return new_sol

#generates percentage range based on percentage strength of each solution
def generate_wheel(percentages):
    wheel = []
    pair = []
    dimension = len(percentages)
    start = 0.0
    end = percentages[0]
    pair.append(start)
    pair.append(end)
    wheel.append(pair)
    for i in range(dimension):
        pair = []
        if i != 0:
            start = end
            end = end + percentages[i]
            pair.append(start)
            pair.append(end)
            wheel.append(pair)
    return wheel

#choose index of parent based on random number generated and the range in the r wheel
def select_parent(random_number, wheel):
    dimension = len(wheel)
    for i in range(dimension):
        if random_number > wheel[i][0]:
            if random_number < wheel[i][1]:
                return i + 1
            else:
                continue
#%%

n = 16
added = 2000
mutation_rate = 0.75
generations = 30

# generate population

popn = generate_pop(n)
print("The solutions")
for i in range(n):
    print(popn[i])

# calculate fitness

fitness_value = []
for i in range(n):
    fit = evaluation(popn[i])
    fitness_value.append(fit)
print(" ")
print("The Evaluation")
print(fitness_value)

# keep track of the best solution

all_fitness = []
index_best = np.argmax(fitness_value)
super_best_solution = popn[index_best] # a vector of 16 bits
super_best_fitness = max(fitness_value) #scalar value
print(" ")
print("Best Solution : ", super_best_solution)
print("Best Fitness : ", super_best_fitness)
all_fitness.append(super_best_fitness) # keep track of the best solution

for j in range(generations):
    print(" ")
    print("Generation : ", j)

    # calculate the strength of each solution
    ave = averaging(added, fitness_value)

    #convert the averaging into percentages
    percentages = [x/sum(ave) for x in ave]
    print(" ")
    print("The Strength")

    # generate the roulette wheel ranges
    wheel = generate_wheel(percentages)
    print(" ")
    print("The Wheel")
    print(wheel)

    # recombination
    new_popn = []
    for i in range(int(n/2)):

        # select two parents
        parent1 = select_parent(random.random(), wheel)
        parent2 = select_parent(random.random(), wheel)
        print(" ")
        print("Parents", parent1, " and ", parent2)

        # Ensure valid parents are selected
        if parent1 is None or parent2 is None:
            print("Error: Invalid parent selection")
            continue

        print(" ")
        print("Recombination : ", i)
        print("Before Swapping")
        print("Parent1", popn[parent1 - 1])
        print("Parent2", popn[parent2 - 1])
        print("Fitness Parent 1 : ", evaluation(popn[parent1 - 1]))
        print("Fitness Parent 2 : ", evaluation(popn[parent2 - 1]))
        babe1, babe2 = substring_swap(popn[parent1 - 1], popn[parent2 - 1])
        print("After Swapping")
        print("Baby1", babe1)
        print("Baby2", babe2)
        print("Fitness Baby 1 : ", evaluation(babe1))
        print("Fitness Baby 2 : ", evaluation(babe2))
        new_popn.append(babe1)
        new_popn.append(babe2)

    print("The New Solutions")
    for i in range(n):
        print(new_popn[i])

    # calculate fitness
    fitness_value = []
    for i in range(n):
        fit = evaluation(new_popn[i])
        fitness_value.append(fit)
    print(" ")
    print("The Evaluation")
    print(fitness_value)

    # mutation
    for i in range(n):
        random_number = random.random()
        if random_number < mutation_rate:
            mutated = mutation(new_popn[i])
            new_popn[i] = mutated

    # new population becomes the current population
    popn = new_popn

    print("The Mutated Solutions")
    for i in range(n):
        print(popn[i])

    # calculate fitness
    fitness_value = []
    for i in range(n):
        fit = evaluation(new_popn[i])
        fitness_value.append(fit)
    print(" ")
    print("The Evaluation")
    print(fitness_value)

    # determine best in this generation
    index_best = np.argmax(fitness_value)
    best_solution_this_gen = popn[index_best]
    best_fitness_this_gen = max(fitness_value)

    # compare with overall best
    if best_fitness_this_gen > super_best_fitness:
        super_best_solution = best_solution_this_gen
        super_best_fitness = best_fitness_this_gen

    print(" ")
    print("Best Solution : ", super_best_solution)
    print("Best Fitness : ", super_best_fitness)

    all_fitness.append(super_best_fitness)

print(all_fitness)
plt.plot(all_fitness)
plt.ylabel('Evaluation')
plt.xlabel('Generation No.')
plt.show()