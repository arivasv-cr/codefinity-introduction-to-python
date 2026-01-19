# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Contar cuántas veces aparece "apples"
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

# Encontrar el índice de la primera ocurrencia de "bananas"
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

# Comprobar el nivel de stock de manzanas
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Contar cuántas veces aparece "grapes" y evaluar su stock
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Comprobar si existen "oranges" y mostrar su índice si están presentes
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")