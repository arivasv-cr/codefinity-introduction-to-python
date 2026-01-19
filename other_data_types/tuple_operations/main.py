# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Convertir la lista de actualización en tupla
shelf1_update_tuple = tuple(shelf1_update)
shelf1_tuple = tuple(shelf1)

# Concatenar la tupla original con la tupla de actualización
shelf1_concat = shelf1_tuple + shelf1_update_tuple

# Contar cuántas veces aparece "celery"
celery_count = shelf1_concat.count("celery")

# Encontrar el índice de la primera aparición de "celery"
celery_index = shelf1_concat.index("celery")

# Imprimir los resultados en el formato solicitado
print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)