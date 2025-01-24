import json

# Cargar el archivo JSON
file_path = '/Users/maria/Desktop/Máster IA/Visión Artificial Avanzada/Proyecto BreCaHAD/dataset/labels/_annotations.coco_train.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Categorías a eliminar
categories_to_remove = ["apoptosis", "mitosis"]

# Obtener los IDs de las categorías a eliminar
category_ids_to_remove = [
    category["id"] for category in data["categories"]
    if category["name"] in categories_to_remove
]

# Filtrar las categorías eliminadas
filtered_categories = [
    category for category in data["categories"]
    if category["id"] not in category_ids_to_remove
]

# Crear un mapeo para reasignar los IDs
new_id_mapping = {category["id"]: new_id for new_id, category in enumerate(filtered_categories)}

# Actualizar los IDs en las categorías
for category in filtered_categories:
    category["id"] = new_id_mapping[category["id"]]

# Actualizar los IDs en las anotaciones
for annotation in data["annotations"]:
    if annotation["category_id"] in new_id_mapping:
        annotation["category_id"] = new_id_mapping[annotation["category_id"]]

# Reemplazar las categorías en el dataset
data["categories"] = filtered_categories

# Guardar el JSON modificado
output_path = '/Users/maria/Desktop/Máster IA/Visión Artificial Avanzada/Proyecto BreCaHAD/dataset/labels/_annotations_normalized.coco_train.json'
with open(output_path, 'w') as file:
    json.dump(data, file)

print(f"Archivo guardado en: {output_path}")
