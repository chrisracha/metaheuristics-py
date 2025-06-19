# Metaheuristics Algorithms Collection

This repository contains implementations of various metaheuristic optimization algorithms in Python. These algorithms are designed to solve complex optimization problems where traditional methods may not be effective.

## 📁 File Structure

```
metaheuristics-py/
├── README.md                           # This file
├── antsystem.py                        # Ant Colony Optimization (ACO)
├── simulated annealing.py              # Simulated Annealing (SA)
├── neural networks.py                  # Neural Network Implementation
├── particle swarm optimization.py      # Particle Swarm Optimization (PSO)
└── genetic algorithm.py                # Genetic Algorithm (GA)
```

## 🚀 Algorithms Overview

### 1. Ant Colony Optimization (ACO) - `antsystem.py`
**Problem**: Traveling Salesman Problem (TSP)
- **Description**: Implements the Ant System algorithm for solving TSP using pheromone trails and heuristic information
- **Key Features**:
  - Pheromone initialization and updating
  - State transition rule with probability calculations
  - Global pheromone updating rule
  - Configurable parameters (alpha, beta, population size, iterations)
- **Usage**: Run the script to solve a predefined 8-city TSP instance

### 2. Simulated Annealing (SA) - `simulated annealing.py`
**Problem**: Global optimization using Griewank function
- **Description**: Implements simulated annealing with multiple cooling schedules
- **Key Features**:
  - Linear, geometric, and slow decrease temperature schedules
  - Griewank function as objective function
  - Probability-based acceptance criterion
  - Visualization of convergence using matplotlib
- **Usage**: Run the script to optimize the Griewank function with configurable parameters

### 3. Neural Networks - `neural networks.py`
**Problem**: Pattern recognition and classification
- **Description**: Educational implementation of feedforward neural networks with backpropagation
- **Key Features**:
  - Sigmoid activation function
  - Mean Squared Error loss function
  - Backpropagation training algorithm
  - Configurable network architecture
- **Usage**: Includes example dataset for training and testing

### 4. Particle Swarm Optimization (PSO) - `particle swarm optimization.py`
**Problem**: Global optimization using Griewank function
- **Description**: Implements PSO with velocity and position update equations
- **Key Features**:
  - Velocity update with cognitive and social components
  - Position update with boundary constraints
  - Griewank function optimization
  - Convergence visualization
- **Usage**: Run the script to optimize the Griewank function with swarm intelligence

### 5. Genetic Algorithm (GA) - `genetic algorithm.py`
**Problem**: Binary optimization with mathematical function
- **Description**: Implements GA with binary encoding and various genetic operators
- **Key Features**:
  - Binary chromosome representation
  - Roulette wheel selection
  - Substring crossover (uniform crossover)
  - Bit-flip mutation
  - Fitness scaling and averaging
- **Usage**: Run the script to optimize a 4-variable mathematical function

## 🛠️ Requirements

The following Python packages are required:
```bash
pip install numpy matplotlib
```

## 📊 Key Parameters

### Ant Colony Optimization
- `size`: Number of ants (default: 10)
- `iterations`: Number of iterations (default: 50)
- `alpha`: Pheromone evaporation rate (default: 0.75)
- `beta`: Heuristic importance factor (default: 2.0)

### Simulated Annealing
- `T`: Initial temperature (default: 10)
- `T_final`: Final temperature (default: 0.10)
- `L`: Iterations per temperature (default: 20)
- `cycles`: Number of cycles (default: 20)

### Particle Swarm Optimization
- `size`: Population size (default: 100)
- `dim`: Problem dimension (default: 5)
- `iterations`: Number of iterations (default: 100)
- `alpha`: Social learning factor (default: 2.0)
- `beta`: Cognitive learning factor (default: 2.0)
- `inertia`: Inertia weight (default: 0.5)

### Genetic Algorithm
- `n`: Population size (default: 16)
- `generations`: Number of generations (default: 30)
- `mutation_rate`: Mutation probability (default: 0.75)
- `added`: Fitness scaling factor (default: 2000)

## 🎯 Usage Examples

### Running Ant Colony Optimization
```python
# The script is self-contained and can be run directly
python antsystem.py
```

### Running Simulated Annealing
```python
# The script includes visualization of convergence
python "simulated annealing.py"
```

### Running Particle Swarm Optimization
```python
# The script shows convergence plot
python "particle swarm optimization.py"
```

### Running Genetic Algorithm
```python
# The script displays population evolution
python "genetic algorithm.py"
```

## 📈 Visualization

Several algorithms include visualization capabilities:
- **Simulated Annealing**: Plots objective function values over iterations
- **Particle Swarm Optimization**: Shows global best fitness convergence
- **Neural Networks**: Can be extended to plot training loss

## 🔧 Customization

Each algorithm can be customized by modifying the parameters at the top of each file. The algorithms are designed to be educational and can be easily adapted for different objective functions or problem domains.

## 📚 Educational Purpose

These implementations are primarily for educational purposes and demonstrate the core concepts of each metaheuristic algorithm. For production use, consider using established libraries like:
- `scipy.optimize` for optimization algorithms
- `tensorflow` or `pytorch` for neural networks
- `deap` for genetic algorithms

## 🤝 Contributing

Feel free to improve these implementations or add new metaheuristic algorithms to the collection!

## 📄 License

This project is open source and available under the MIT License.
