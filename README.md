# BreCaHAD-VisionArtificial
Este repositorio recoge el código y los resultados obtenidos de la detección de tumores mediante diversos modelos de YOLO con el dataset de BreCaHAD. que recoge imágenes hispatológicas de cáncer de mama.

En la carpeta de resultados se encuentran todas las métricas y gráficas de los entrenamientos realizados con los diversos modelos. Asimismo, están divididos en diferentes Jupyter Notebook cada uno de los modelos probados con sus resultados específicos y el data.yaml que es común para todos.

- El archivo "etiquetar_imagen_test.py" etiqueta las imagenes con exactitud acorde al json correspondiente.
- El archivo "editar_cocojson.py" ha sido utilizado para editar las etiquetas y eliminar las dos clases menos representativas del dataset.
- -El archivo "coco_to_yolo.py" ha sido utilizado para adaptar los archivos json con el etiquetado a los modelos de YOLO.

## Creadores del proyecto

- ### María Millán Gordillo
- ### Pablo Parra Méndez
- ### María Victoria Rodríguez del Corral

