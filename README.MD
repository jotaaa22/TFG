# CLASIFICADOR DE FÓSILES MEDIANTE IMÁGENES UTILIZANDO DEEP LEARNING
Aplicación web que permite identificar fósiles mediante imágenes utilizando un modelo de red convolucional (CNN) entrenado basado en YOLOv8.
La aplicación permite al usuario subir imágenes desde local, obtener la predicción del fósil e información en base a la predicción realizada.

---

## Características del proyecto

- Subir imágenes desde el local al navegador.
- Clasificación del fósil de manera automática utilizando IA.
- Permite ver Top 3 predicciones junto a la confianza de la misma.
- Información básica sobre la clase a la que pertenece el fósil (descripción, características, taxonomía).
- Interfaz web responsive (mobile-first).

---

## Arquitectura del proyecto

- **frontEnd**: HTML, CSS, JavaScript (Bootstrap).
- **backEnd**: Flask (API REST).
- **Modelo de IA**: YOLOv8 (Ultralytics).
- **Datos de los fósiles**: JSON creado a mano con la información pertinente.

**Cliente web**
    |
    |
**frontEnd**
    |
    |
**API REST Flask**
    |
    |
**Modelo YOLOv8**
    |
    |
**Respuesta JSON**

---

## Estructura del proyecto

TFG/
│
├── backEnd/
│ └── app.py
│
├── frontEnd/
│ ├── templates/
│ │ └── index.html
│ │
│ └── static/
│ ├── css/
│ │ └── estilos.css
│ ├── js/
│ │ └── script.js
│ └── imagenes/
│
├── data/
│ └── (dataset no incluido)
│
├── modelos/
│ ├── entrenamiento/
│ └── inferencia/
│
├── reentrenamiento/
│
├── resultados_experimentos/
│
├── scripts/
│
├── requirements.txt
└── README.md

---

## Instalación

1. Clonar el repositorio en tu carpeta local

```bash

git clone https://github.com/jotaaa22/TFG.git
cd TFG

```

2. Instalar dependencias

```bash

pip install -r requirements.txt

```
3. Ejecución del proyecto

```bash

python backEnd/app.py

```

4. Acceder al enlace que se muestra por terminal

---

### Endpoint

POST /prediccion

---

### Parámetros

- file: imagen a clasificar

---

### Respuesta

```json
{
  "clase": "trilobite",
  "confianza": 0.54,
  "imagen": "http://127.0.0.1:5000/imagenes/imagen.png",
  "info": {...},
  "top_3_predicciones": [...]
}

```
---

## Dataset

El dataset que ha sido utilizado en este proyecto para entrenar el modelo no se incluye en el repositorio del proyecto para evitar problemas de Copyright de las imágenes.

Se incluye en el proyecto solo el modelo entrenado y el sistema de inferencia.

---

## Mejoras a implementar a futuro

- Ampliación del dataset, ya sea agregando imágenes o usando los aportes de los usuarios.
- Mejorar la precisión del modelo YOLO.

---