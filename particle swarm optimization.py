#%%

import math
import random
import matplotlib.pyplot as plt

# generations random decision variable values
def griewank_generate(lb, ub):
    return lb + (ub - lb) * random.random()

# calculate fitness value based on griewank function
def griewank(solution):
    summation = 0.0
    product = 1.0
    dimension = len(solution)
    for i in range (dimension):
        summation = summation + (solution[i] * solution[i]) / 4000
        product = product * math.cos(solution[i] / math.sqrt(i + 1))

    return 1 + summation - product

# generates a population based on griewank lower and upper bounds
def generate_griewank_popn(pop_size, dimension, lb, ub):
    population = []
    for k in range(pop_size):
        solution = []
        for i in range(dimension):
            solution.append(griewank_generate(lb, ub))
        population.append(solution)

    return population

#set initial velocities to zero
def init_velocities(pop_size, dimension):
    velocity = []
    for k in range(pop_size):
        solution = []
        for i in range(dimension):
            velocity.append([0] * dimension)
    return velocity

# calculate fitness of all population
def popn_fitness(population):
    fitness = []
    dimension = len(population)
    for i in range(dimension):
        fitness_now = griewank(population[i])
        fitness.append(fitness_now)
    return fitness

# velocity update equation
def velocity_update(inertia, velocities, alpha, beta, particles, best_particle, particle_best):
    new_velocity = []
    for k in range (len(particles)):
        social_part = [alpha * random.random() * (a-b) for a, b in zip(best_particle, particles[k])]
        cognitive_part = [beta * random.random() * (a-b) for a, b in zip(particle_best[k], particles[k])]
        velocity = [inertia * a + b + c for a,b,c in zip(velocities[k], social_part, cognitive_part)]
        new_velocity.append(velocity)
    return new_velocity

# position update equation
def position_update(particles, velocities):
    new_position = []
    for k in range(len(particles)):
        position = [a + b for a, b in zip(particles[k], velocities[k])]
        new_position.append(position)
    return new_position

# clip the variable values within lower and upper bound
def within_range(solutions, lb, ub):
    size = len(solutions)
    dim = len(solutions[0])
    sols = solutions
    for k in range(size):
        particle = sols[k]
        for l in range(dim):
            if particle[l] < lb:
                particle[l] = lb
            if particle[l] > ub:
                particle[l] = ub
        sols[k] = particle
    return sols
#%%

size = 100
dim = 5
lb = -10
ub = 10
iterations = 100
alpha = 2.0
beta = 2.0
inertia = 0.5
t = 0
overall_best_fitness = []

# initalize locations
particles = generate_griewank_popn(size, dim, lb, ub)

# initialize velocities
velocities = init_velocities(size, dim)

# calculate fitness values
fitness_population = popn_fitness(particles)

# determine best particlr in the population
best_fitness = min(fitness_population)
best_particle_index = fitness_population.index(min(fitness_population))
global_best_particle = particles[best_particle_index]
overall_best_fitness.append(best_fitness)

# deterimne particle's best position, at the start it is its initial position
particle_best = particles

while t < iterations:
    # calculate new velocities
    new_velocity = velocity_update(inertia, velocities, alpha, beta, particles, global_best_particle, particle_best)

    # calculate new positions
    new_particles = position_update(new_velocity, particles)

    # clip the variable values to the bounds
    new_particles = within_range(new_particles, lb, ub)

    #update each particle's best position
    for k in range(size):
        if griewank(new_particles[k]) < griewank(particle_best[k]):
            particle_best[k] = new_particles[k]
    
    # calculate fitness values
    fitness_population = popn_fitness(new_particles)

    # determine best particle in the population
    best_fitness_now = min(fitness_population)
    best_particle_index_now = fitness_population.index(min(fitness_population))

    # update the global best
    if best_fitness_now < best_fitness:
        best_fitness = best_fitness_now
        global_best_particle = new_particles[best_particle_index_now]

    overall_best_fitness.append(best_fitness)

    # update the particles and velocities
    velocities = new_velocity
    particles = new_particles

    t += 1

last_global_best = min(overall_best_fitness)

plt.plot(overall_best_fitness)
plt.title('Global Best : ' + str(last_global_best))
plt.ylabel('Evaluation')
plt.xlabel('Generation No.')
plt.show()