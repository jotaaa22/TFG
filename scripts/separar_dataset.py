import os
import shutil
import random

SOURCE_DIR = "data/reduced-FID"
OUTPUT_DIR = "data/dataset_procesado"

RATIO_SPLIT = (0.7, 0.2, 0.1)

def crear_carpeta(nombre_carpeta):
    for split in ["train", "val", "test"]:
        path = os.path.join(OUTPUT_DIR, split, nombre_carpeta)
        os.makedirs(path, exist_ok=True)

def dividir_archivos(archivos):
    random.shuffle(archivos)
    total = len(archivos)

    fin_entren = int(total * RATIO_SPLIT[0])
    fin_valid = fin_entren + int(total * RATIO_SPLIT[1])

    return(archivos[:fin_entren], archivos[fin_entren:fin_valid], archivos[fin_valid:])

def procesar_carpeta(nombre_carpeta):
    directorio_carpeta = os.path.join(SOURCE_DIR, nombre_carpeta)

    archivos = [f for f in os.listdir(directorio_carpeta) if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    if len(archivos) == 0:
        print(f"No hay imágenes: {directorio_carpeta}")
        return
    
    train, val, test = dividir_archivos(archivos)

    for dividir_nombre, dividir_lista_archivos in zip(["train", "val", "test"], [train, val, test]):
        for i, archivo in enumerate(dividir_lista_archivos):
            src = os.path.join(directorio_carpeta, archivo)
            nombre_imagen = f"{nombre_carpeta}_{i}.jpg" #los nombres de algunas imágenes son muy largos -> cambiamos nombre
            dst = os.path.join(OUTPUT_DIR, dividir_nombre, nombre_carpeta, nombre_imagen)
            shutil.copy2(src, dst)

    print(f"{nombre_carpeta}: {len(train)} entrenamiento, {len(val)} validación, {len(test)} test")

def main():
    carpetas = os.listdir(SOURCE_DIR)

    for nombre_carpeta in carpetas:
        directorio_carpeta = os.path.join(SOURCE_DIR, nombre_carpeta)

        if not os.path.isdir(directorio_carpeta):
            continue

        crear_carpeta(nombre_carpeta)
        procesar_carpeta(nombre_carpeta)

if __name__ == "__main__":
    main()