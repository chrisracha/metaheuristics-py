#%%
import random

data = [ # not from the lecvid i am not insane
    [0, 13, 45, 50, 95, 15, 32, 140],
    [15, 0, 40, 44, 85, 22, 43, 122],
    [42, 35, 0, 7, 42, 55, 40, 145],
    [48, 39, 10, 0, 47, 58, 45, 155],
    [105, 90, 35, 42, 0, 98, 100, 202],
    [12, 24, 52, 55, 102, 0, 35, 148],
    [25, 42, 32, 42, 102, 33, 0, 112],
    [135, 125, 142, 150, 212, 150, 110, 0]
]


def init_tau(dimension):
    tau = []
    for k in range(dimension):
        tau.append([1] * dimension)
    return tau
#%%

size = 10
iterations = 50
beta = 2.0
alpha = 0.75
dimension = len(data[0])
best_prob = -1.0
t = 0
global_best_tour = 1000
global_best_ant = []

#initialize the pheromone levels to 1 at the start
tau = init_tau(dimension)

#choose starting city of ant
while t < iterations:
    print("Iteration : ", t)
    population = []

    #state transition rule
    #run through each ant
    for k in range(size):
        J = [i for i in range(dimension)]
        ant = []

        #randomly select starting city
        start_city = random.choice(J)

        #remove this city from J and add to ant tour
        ant.append(start_city)
        J.remove(start_city)

        last_city = start_city

        #we loop until we complete the tour, less one because we already have a starting city
        for l in range(dimension - 1):

            best_prob = -1.0
            sum = 0

            #calculate all probabilities
            for m in range(len(J)):
                sum = sum + tau[last_city][J[m]] * ((1/data[last_city][J[m]]) ** beta)
            for n in range(len(J)):
                numerator = tau[last_city][J[n]] * ((1/data[last_city][J[n]]) ** beta)
                probability = numerator / sum

                #determine the highest probability and record the city associated with it
                if probability > best_prob:
                    best_prob = probability
                    next_city = J[n]

            last_city = next_city

            #remove the city from J and add to ant tour
            ant.append(last_city)
            J.remove(last_city)

        #append the completed ant to the population
        population.append(ant)

    #calculate tour length of each ant
    L = []
    for k in range(size):
        ant = population[k]
        tour_length = 0
        for l in range(dimension - 1):
            r = ant[l]
            s = ant[l + 1]

            tour_length = tour_length + data[r][s]
        tour_length = tour_length + data[ant[-1]][ant[0]]
        L.append(tour_length)

    #fitness values of each ant
    inverted_L = [1 / L[i] for i in range(size)]

    #determine best ant in this iteration
    best_tour_now = min(L)
    best_ant_now = population[L.index(min(L))]
    print("Best tour length NOW : ", best_tour_now)
    print("Best ant NOW : ", best_ant_now)

    #compare in iterations best with global best
    if best_tour_now < global_best_tour:
        global_best_tour = best_tour_now
        global_best_ant = best_ant_now
        print("Replaced!")

    #global pheromone updating rule
    for m in range(dimension):
        for n in range(dimension):
            first_term = (1-alpha) * tau[m][n]
            second_term = 0

            #run through each ant
            for o in range(size):
                    ant
                    for p in range(dimension - 1):
                        r = ant[p]
                        s = ant[p + 1]

                        if ((m == r) and (n ==s)):
                            #get tour length of ant and reciprocate it
                            second_term = second_term + (1 / L[o])

                            #dont continue this ant if found cause it only appears once
                            break
            tau[m][n] = first_term + second_term
    t += 1

print("Best ant : ", global_best_ant)
print("Best tour length : ", global_best_tour)