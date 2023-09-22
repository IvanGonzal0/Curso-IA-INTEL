import random  # Importo el módulo random para generar números aleatorios
from fuzzywuzzy import fuzz  # Importo la función de similitud de cadenas de fuzzywuzzy

abecedario = "abcdefghijklmnopqrstuvwxyz"  # Defino una cadena con el alfabeto en minúsculas

# Funcion para generar una poblacion inicial de cadenas aleatorias
def generate_initial_population(size, length):
    return [''.join(random.choice(abecedario) for _ in range(length)) for _ in range(size)]

# Funcion para evaluar la similitud entre una cadena y la palabra objetivo
def fitness(target, candidate):
    return fuzz.ratio(target, candidate)

# Funcion para seleccionar individuos de la poblacion segun su ajuste (fitness)
def select_parents(population, target):
    # Calcula los puntajes de ajuste para cada candidato en la población
    fitness_scores = [fitness(target, candidate) for candidate in population]
    total_fitness = sum(fitness_scores)  # Calcula la suma de los puntajes de ajuste
    probabilities = [score / total_fitness for score in fitness_scores]  # Calcula las probabilidades de seleccion
    return random.choices(population, probabilities, k=2)  # Selecciona 2 padres aleatorios segun las probabilidades

# Función para realizar el cruce entre dos cadenas (individuos)
def crossover(parent1, parent2):
    midpoint = random.randint(1, len(parent1) - 1)  # Calcula un punto de corte aleatorio
    child1 = parent1[:midpoint] + parent2[midpoint:]  # Crea un hijo combinando partes de ambos padres
    child2 = parent2[:midpoint] + parent1[midpoint:]  # Crea otro hijo intercambiando las partes
    return child1, child2

# Funcion para realizar la mutacion en una cadena
def mutate(candidate, mutation_rate):
    mutated_candidate = ''
    for char in candidate:
        if random.random() < mutation_rate:  # Decide si realizar una mutacion basada en la tasa de mutacion
            mutated_candidate += random.choice(abecedario)  # Agrega un carocter aleatorio como mutacion
        else:
            mutated_candidate += char  # Conserva el caracter original si no hay mutacion
    return mutated_candidate

# Funcion principal del algoritmo genetico
def genetic_algorithm(target, population_size=100, mutation_rate=0.1, max_generations=10000):
    population = generate_initial_population(population_size, len(target))  # Genera una poblacion inicial
    for generation in range(max_generations):
        parents = select_parents(population, target)  # Selecciona padres para la siguiente generacion
        child1, child2 = crossover(parents[0], parents[1])  # Cruza los padres para crear dos hijos
        child1 = mutate(child1, mutation_rate)  # Aplica mutaciin a los hijos
        child2 = mutate(child2, mutation_rate)
        population = [child1, child2] + population[2:]  # Reemplaza a los dos padres menos aptos con los hijos
        best_candidate = max(population, key=lambda candidate: fitness(target, candidate))  # Encuentra el candidato ms apto
        
        if fitness(target, best_candidate) > 74:  # Si se alcanza un nivel de similitud deseado
            print(f"Generación {generation + 1}: Encontrada la palabra '{best_candidate}'")
            break  # Sale del ciclo si se cumple el criterio

# Pido al usuario que ingrese una palabra de cuatro caracteres
while True:
    user_input = input("Ingresa una palabra de cuatro letras: ").lower()
    if len(user_input) == 4 and user_input.isalpha():
        break  # Sale del ciclo si se ingresa una palabra valida
    else:
        print("La palabra debe tener cuatro letras. Inténtalo nuevamente.")

# Ejecutar el algoritmo gentico
genetic_algorithm(user_input)  # Llama a la funcion principal con la palabra ingresada


