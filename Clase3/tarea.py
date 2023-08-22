# import random
# from fuzzywuzzy import fuzz

# # Lista con todos los caracteres del abecedario
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# # Función para generar una población inicial de cadenas aleatorias
# def generate_initial_population(size, length):
#     return [''.join(random.choice(alphabet) for _ in range(length)) for _ in range(size)]

# # Función para evaluar la similitud entre una cadena y la palabra objetivo
# def fitness(target, candidate):
#     return fuzz.ratio(target, candidate)

# # Función para seleccionar individuos de la población según su ajuste (fitness)
# def select_parents(population, target):
#     fitness_scores = [fitness(target, candidate) for candidate in population]
#     total_fitness = sum(fitness_scores)
#     probabilities = [score / total_fitness for score in fitness_scores]
#     return random.choices(population, probabilities, k=2)

# # Función para realizar el cruce entre dos cadenas (individuos)
# def crossover(parent1, parent2):
#     midpoint = random.randint(1, len(parent1) - 1)
#     child1 = parent1[:midpoint] + parent2[midpoint:]
#     child2 = parent2[:midpoint] + parent1[midpoint:]
#     return child1, child2

# # Función para realizar la mutación en una cadena
# def mutate(candidate, mutation_rate):
#     mutated_candidate = ''
#     for char in candidate:
#         if random.random() < mutation_rate:
#             mutated_candidate += random.choice(alphabet)
#         else:
#             mutated_candidate += char
#     return mutated_candidate

# # Función principal del algoritmo genético
# def genetic_algorithm(target, population_size=100, mutation_rate=0.1, max_generations=1000):
#     population = generate_initial_population(population_size, len(target))
#     for generation in range(max_generations):
#         parents = select_parents(population, target)
#         child1, child2 = crossover(parents[0], parents[1])
#         child1 = mutate(child1, mutation_rate)
#         child2 = mutate(child2, mutation_rate)
#         population = [child1, child2] + population[2:]
#         best_candidate = max(population, key=lambda candidate: fitness(target, candidate))

#         if fitness(target, best_candidate) == 100:
#             print(f"Generación {generation + 1}: Encontrada la palabra '{best_candidate}'")
#             break

# # Pedir al usuario que ingrese una palabra de cuatro caracteres
# while True:
#     user_input = input("Ingresa una palabra de cuatro letras: ")
#     if len(user_input) == 4 and user_input.isalpha():
#         break
#     else:
#         print("La palabra debe tener cuatro letras. Inténtalo nuevamente.")

# # Ejecutar el algoritmo genético
# genetic_algorithm(user_input)



# PROFESOR

import random 
from random import randint, choice

from fuzzywuzzy import fuzz

lista=["a", "e", "i", "o", "u"]
print(choice(lista))

p1 = "mama"
p2 = "mi abuela"


aprox = fuzz.ratio(p1, p2)  #esto determina un valor entre 0 y 100 de aproximacion

print(aprox)