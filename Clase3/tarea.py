import random
from fuzzywuzzy import fuzz

# Lista con todos los caracteres del abecedario
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Función para generar una población inicial de cadenas aleatorias
def generate_initial_population(size, length):
    return [''.join(random.choice(alphabet) for _ in range(length)) for _ in range(size)]

# Función para evaluar la similitud entre una cadena y la palabra objetivo
def fitness(target, candidate):
    return fuzz.ratio(target, candidate)

# Función para seleccionar individuos de la población según su ajuste (fitness)
def select_parents(population, target):
    fitness_scores = [fitness(target, candidate) for candidate in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    return random.choices(population, probabilities, k=2)

# Función para realizar el cruce entre dos cadenas (individuos)
def crossover(parent1, parent2):
    midpoint = random.randint(1, len(parent1) - 1)
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]
    return child1, child2

# Función para realizar la mutación en una cadena
def mutate(candidate, mutation_rate):
    mutated_candidate = ''
    for char in candidate:
        if random.random() < mutation_rate:
            mutated_candidate += random.choice(alphabet)
        else:
            mutated_candidate += char
    return mutated_candidate

# Función principal del algoritmo genético
def genetic_algorithm(target, population_size=100, mutation_rate=0.1, max_generations=10000):
    population = generate_initial_population(population_size, len(target))
    for generation in range(max_generations):
        parents = select_parents(population, target)
        child1, child2 = crossover(parents[0], parents[1])
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        population = [child1, child2] + population[2:]
        best_candidate = max(population, key=lambda candidate: fitness(target, candidate))

        if fitness(target, best_candidate) > 74:
            print(f"Generación {generation + 1}: Encontrada la palabra '{best_candidate}'")
            break

# Pedir al usuario que ingrese una palabra de cuatro caracteres
while True:
    user_input = input("Ingresa una palabra de cuatro letras: ").lower()
    if len(user_input) == 4 and user_input.isalpha():
        break
    else:
        print("La palabra debe tener cuatro letras. Inténtalo nuevamente.")

# Ejecutar el algoritmo genético
genetic_algorithm(user_input)



import random  # Importa el módulo random para generar números aleatorios
from fuzzywuzzy import fuzz  # Importa la función de similitud de cadenas de fuzzywuzzy

alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define una cadena con el alfabeto en minúsculas

# Función para generar una población inicial de cadenas aleatorias
def generate_initial_population(size, length):
    return [''.join(random.choice(alphabet) for _ in range(length)) for _ in range(size)]

# Función para evaluar la similitud entre una cadena y la palabra objetivo
def fitness(target, candidate):
    return fuzz.ratio(target, candidate)

# Función para seleccionar individuos de la población según su ajuste (fitness)
def select_parents(population, target):
    # Calcula los puntajes de ajuste para cada candidato en la población
    fitness_scores = [fitness(target, candidate) for candidate in population]
    total_fitness = sum(fitness_scores)  # Calcula la suma de los puntajes de ajuste
    probabilities = [score / total_fitness for score in fitness_scores]  # Calcula las probabilidades de selección
    return random.choices(population, probabilities, k=2)  # Selecciona 2 padres aleatorios según las probabilidades

# Función para realizar el cruce entre dos cadenas (individuos)
def crossover(parent1, parent2):
    midpoint = random.randint(1, len(parent1) - 1)  # Calcula un punto de corte aleatorio
    child1 = parent1[:midpoint] + parent2[midpoint:]  # Crea un hijo combinando partes de ambos padres
    child2 = parent2[:midpoint] + parent1[midpoint:]  # Crea otro hijo intercambiando las partes
    return child1, child2

# Función para realizar la mutación en una cadena
def mutate(candidate, mutation_rate):
    mutated_candidate = ''
    for char in candidate:
        if random.random() < mutation_rate:  # Decide si realizar una mutación basada en la tasa de mutación
            mutated_candidate += random.choice(alphabet)  # Agrega un carácter aleatorio como mutación
        else:
            mutated_candidate += char  # Conserva el carácter original si no hay mutación
    return mutated_candidate

# Función principal del algoritmo genético
def genetic_algorithm(target, population_size=100, mutation_rate=0.1, max_generations=10000):
    population = generate_initial_population(population_size, len(target))  # Genera una población inicial
    for generation in range(max_generations):
        parents = select_parents(population, target)  # Selecciona padres para la siguiente generación
        child1, child2 = crossover(parents[0], parents[1])  # Cruza los padres para crear dos hijos
        child1 = mutate(child1, mutation_rate)  # Aplica mutación a los hijos
        child2 = mutate(child2, mutation_rate)
        population = [child1, child2] + population[2:]  # Reemplaza a los dos padres menos aptos con los hijos
        best_candidate = max(population, key=lambda candidate: fitness(target, candidate))  # Encuentra el candidato más apto
        
        if fitness(target, best_candidate) > 74:  # Si se alcanza un nivel de similitud deseado
            print(f"Generación {generation + 1}: Encontrada la palabra '{best_candidate}'")
            break  # Sale del ciclo si se cumple el criterio

# Pedir al usuario que ingrese una palabra de cuatro caracteres
while True:
    user_input = input("Ingresa una palabra de cuatro letras: ").lower()
    if len(user_input) == 4 and user_input.isalpha():
        break  # Sale del ciclo si se ingresa una palabra válida
    else:
        print("La palabra debe tener cuatro letras. Inténtalo nuevamente.")

# Ejecutar el algoritmo genético
genetic_algorithm(user_input)  # Llama a la función principal con la palabra ingresada


# PROFESOR

# import random 
# from random import randint, choice

# from fuzzywuzzy import fuzz

# lista=["a", "b", "c", "d", "e","f", "g", "h", "i", "j","k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t" ,"u", "v", "w", "x", "y", "z"]
# print(choice(lista))

# p1 = "mama"
# p2 = "mama"

# aprox = fuzz.ratio(p1, p2)  #esto determina un valor entre 0 y 100 de aproximacion entre 2 variables (palabras o letras) trabaja con la cantidad de caracteres, los caracteres y la posicion de los caracteres

# print(aprox)

# #palabra clave
# palabra= "jose"


# #pedirle al usuario una palabra q tenga 4 caracteres
# entrada_usuario=input("coloque la palabra a crear: ")

# igualdad = fuzz.ratio(palabra, entrada_usuario)

# print(igualdad)
# if len(entrada_usuario)!=4:
#     usuario=input("coloque la palabra a crear que contenga 4 letras: ")
#     igualdad = fuzz.ratio(palabra, entrada_usuario)
# else:
#     exit()

#desarrollar el algoritmo usando ratio, y me diga la similitud entre la palabra ingresada y la palabra clave
# generar 4 palabras con valores aleatorios del diccionario
# seleccionar las 2 palabras
# hacer una generacion nueva de individuos


# palabra 4 letras clave, y el algoritmo tiene que llegar a esa misma palabra que eligio el usuario
# crear una poblacion de palabras de 5 palabras aleatorios
# comparar la palabra del usuario y buscar la que mas peso tenga
# comparar caracter a caracter e ir mutando
# hacer un criterio de seleccion y con ratio seleccionar la que tenga mas promedio de ponderacion

# OTRA FORMA DE HACERLO