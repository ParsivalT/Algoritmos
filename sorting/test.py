import random
from python.insertion_sort import insertion_sort

#Lista com numero leatorios
random_numbers = random.sample(range(1,1000), 42)

#Array já ordenado
array_sorted = [1, 2, 3, 5, 6, 8, 9, 15, 18, 22, 26,
                33, 34, 42, 47, 66, 68, 79, 102]

inversed = [87, 42, 15, 74, 63, 31, 92, 59, 23, 10]

repeat = [1, 1, 1, 7, 7, 7, 7, 4, 4, 4, 4, 3, 3, 3, 3, 3]

if __name__ == "__main__":
    lista = repeat
    print(lista)
    insertion_sort(lista)
    print("\nOrdenado: ")
    print(lista)