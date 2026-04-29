from ultralytics import YOLO

RUTA_DATAASET = "data/dataset_procesado"

def main():
    model = YOLO("yolov8n-cls.pt")

    model.train(data=RUTA_DATAASET, epochs=25, imgsz=224, batch=32,
                project="modelos", name="entrenamiento_25_epochs", exist_ok=True)
    #Se comprobó y comparó los resultasdos entre 10, 25 y 40 epochs, dando como resultado que la mejor opción son 25.
    
if __name__ == "__main__":
    main()