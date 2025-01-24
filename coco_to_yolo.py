import json
import os

# Ruta al archivo COCO JSON
coco_json_path = "/Users/maria/Desktop/Máster IA/Visión Artificial Avanzada/Proyecto BreCaHAD/dataset/labels/_annotations_normalized.coco_val.json"

# Directorio donde se guardarán los archivos .txt
output_dir = "/Users/maria/Desktop/Máster IA/Visión Artificial Avanzada/Proyecto BreCaHAD/dataset/labels/val"

# Crear las carpetas de salida si no existen
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo JSON
with open(coco_json_path, "r") as f:
    coco_data = json.load(f)

# Crear un diccionario para mapear image_id a nombres de archivo
image_id_to_filename = {img["id"]: img["file_name"] for img in coco_data["images"]}

# Procesar anotaciones
for annotation in coco_data["annotations"]:
    image_id = annotation["image_id"]
    file_name = image_id_to_filename[image_id]
    txt_file_path = os.path.join(output_dir, file_name.replace(".jpg", ".txt").replace(".png", ".txt"))

    # Extraer datos de la anotación
    category_id = annotation["category_id"]
    bbox = annotation["bbox"]  # [x, y, width, height] en píxeles
    img_width = next(img["width"] for img in coco_data["images"] if img["id"] == image_id)
    img_height = next(img["height"] for img in coco_data["images"] if img["id"] == image_id)

    # Convertir bbox al formato YOLO [x_center, y_center, width, height] normalizado
    x_center = (bbox[0] + bbox[2] / 2) / img_width
    y_center = (bbox[1] + bbox[3] / 2) / img_height
    width = bbox[2] / img_width
    height = bbox[3] / img_height

    # Escribir al archivo .txt
    with open(txt_file_path, "a") as txt_file:
        txt_file.write(f"{category_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

print("Conversión completada. Archivos .txt generados.")
