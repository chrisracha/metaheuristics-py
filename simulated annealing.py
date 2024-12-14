#%%
import random
import math
import matplotlib
import matplotlib.pyplot as plt

def griewank_generate(lb, ub):
    return lb + (ub - lb) * random.random()

def griewank(solution):
    summation = 0.0
    product = 1.0
    dimension = len(solution)
    for i in range (dimension):
        summation = summation + (solution[i] ** 2) / 4000
        product = product * math.cos(solution[i] / math.sqrt(i + 1))

    return summation - product + 1

def prob(delta_f, T):
    return math.exp(-1 * delta_f / T)

def temp_linear(T, alpha):
    return T - alpha

def temp_geometric(T, r):
    return T * r

def temp_slow_decrease(T, beta):
    return T / (1 + beta * T)
#%%

dimension = 5

# initial and final temperature
T = 10
T_final = 0.10

beta = 0.01
alpha = 0.1
L = 20 # iterations per temperature
cycles = 20 # number of cycles
r = 0.10 # reduction parameter

#generate an initial solution
solution= []
for i in range(dimension):
    solution.append(griewank_generate(-10, 10))

#list to save our function values over cycles and trials
func_values = []

for K in range(cycles):
    print("Cycle: ", K, "Temp: ", T)
    print("Obj Func Value is : ", griewank(solution))
    for k in range(L):
        #generate a new solution
        new_solution = [element + random.random() - 0.5 for element in solution]

        #calculate obj func values of two solutions
        ofv_solution = griewank(solution)
        ofv_new_solution = griewank(new_solution)

        #calculate delta F
        delta_f = ofv_new_solution - ofv_solution

        if delta_f < 0:
            solution = new_solution
        else:
            probability = prob(delta_f, T)
            z = random.random()
            if z < probability:
                solution = new_solution

        func_values.append(griewank(solution))

    # replace with desired cooling schedule
    T = temp_slow_decrease(T, beta)

#plotting the function values over cycles and trials
x = list(range(1, len(func_values) + 1))
plt.title("Objective Function Value Behaviour")
plt.xlabel("cycles x trials")
plt.ylabel("OFV")
plt.plot(x, func_values, 'r-')

#%