from ultralytics import YOLO
import os

RUTA_MODELO = "modelos/best.pt"
RUTA_IMAGENES = "data/imagenes_test"
modelo = YOLO(RUTA_MODELO)

def prediccion():

    total = 0
    aciertos = 0

    for imagenes in os.listdir(RUTA_IMAGENES):
        if imagenes.lower().endswith((".jpg", ".png", ".jpeg")):

            ruta_imagen = os.path.join(RUTA_IMAGENES, imagenes)

            resultados = modelo(ruta_imagen)
            clase_predecida = resultados[0].names[resultados[0].probs.top1]
            clase_real = imagenes.split("_")[0]

            print(f"{imagenes} Prediccion: {clase_predecida} | Real: {clase_real}")

            if clase_predecida == clase_real:
                aciertos += 1
            
            total += 1
    
    porcentaje_acierto = aciertos / total if total > 0 else 0

    print("\n----------------------")
    print(f"Aciertos: {aciertos}/{total}")
    print(f"Porcentaje de acierto: {porcentaje_acierto:.2f}")
    print("-----------------------")

if __name__ == "__main__":
    prediccion()