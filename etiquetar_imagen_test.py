import cv2

def draw_bounding_boxes(image_path, bbox_file, output_path, class_map, class_colors):
    """
    Dibuja las bounding boxes en una imagen según un archivo con coordenadas normalizadas y colores por clase.
    
    Args:
        image_path (str): Ruta de la imagen de entrada.
        bbox_file (str): Ruta del archivo .txt con coordenadas normalizadas y clases.
        output_path (str): Ruta donde guardar la imagen de salida.
        class_map (dict): Diccionario que mapea IDs de clase a nombres.
        class_colors (dict): Diccionario que mapea IDs de clase a colores (BGR).
    """
    # Leer la imagen
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: No se pudo cargar la imagen de {image_path}")
        return

    # Obtener dimensiones de la imagen
    height, width, _ = image.shape

    # Leer el archivo de bounding boxes
    try:
        with open(bbox_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {bbox_file}")
        return

    # Iterar por las líneas y dibujar las cajas
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            print(f"Línea inválida en {bbox_file}: {line}")
            continue
        
        # Parsear ID de clase y coordenadas normalizadas
        class_id = int(parts[0])
        x_center, y_center, bbox_width, bbox_height = map(float, parts[1:])

        # Obtener el nombre de la clase
        class_name = class_map.get(class_id, f"Clase {class_id}")

        # Desnormalizar y convertir a formato de esquinas
        x_min = int((x_center - bbox_width / 2) * width)
        y_min = int((y_center - bbox_height / 2) * height)
        x_max = int((x_center + bbox_width / 2) * width)
        y_max = int((y_center + bbox_height / 2) * height)

        # Obtener el color para la clase
        color = class_colors.get(class_id, (0, 255, 0))  # Verde por defecto

        # Dibujar el rectángulo en la imagen
        thickness = 2
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)

        # Añadir el texto de la clase
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1
        text_size, _ = cv2.getTextSize(class_name, font, font_scale, font_thickness)
        text_origin = (x_min, y_min - 10 if y_min > 20 else y_min + 20)

        # Dibujar un fondo para el texto
        cv2.rectangle(image, 
                      (text_origin[0], text_origin[1] - text_size[1] - 2), 
                      (text_origin[0] + text_size[0], text_origin[1] + 2), 
                      color, 
                      cv2.FILLED)

        # Dibujar el texto
        text_color = (0, 0, 0) if sum(color) > 382 else (255, 255, 255)  # Texto blanco o negro según fondo
        cv2.putText(image, class_name, text_origin, font, font_scale, text_color, font_thickness)

    # Guardar la imagen de salida
    success = cv2.imwrite(output_path, image)
    if success:
        print(f"Imagen guardada correctamente en {output_path}")
    else:
        print(f"Error al guardar la imagen en {output_path}. Verifica la extensión y permisos.")

# Diccionario de mapeo de clases
class_map = {
    0: 'cells-A6sP',
    1: 'lumen',
    2: 'nolumen',
    3: 'notumor',
    4: 'tumor'
}

# Diccionario de colores para las clases (BGR)
class_colors = {
    1: (255, 216, 100),  # Azul celeste (lumen)
    2: (255, 255, 255),  # Blanco (nolumen)
    3: (0, 0, 255),      # Rojo (tumor)
    4: (139, 0, 0),      # Azul oscuro (notumor)
}

# Ejemplo de uso
image_path = 'C:/Users/pparr/Desktop/Breca/115_png_jpg.rf.18e8de520bd7242e8bddae0718ab5977.jpg'
bbox_file = 'C:/Users/pparr/Desktop/Breca/115_png_jpg.rf.18e8de520bd7242e8bddae0718ab5977.txt'
output_path = 'C:/Users/pparr/Desktop/Breca/test_image.jpg'
draw_bounding_boxes(image_path, bbox_file, output_path, class_map, class_colors)
