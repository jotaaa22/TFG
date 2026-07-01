from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from ultralytics import YOLO
import json
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontEnd/static", template_folder="../frontEnd/templates")
CORS(app)

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))

CARPETA_IMG_SUBIDAS = os.path.join(DIRECTORIO_BASE, "..", "data", "aportes_usuarios")
os.makedirs(CARPETA_IMG_SUBIDAS, exist_ok=True)

RUTA_MODELO = os.path.join(DIRECTORIO_BASE, "..", "modelos", "best.pt")
RUTA_JSON = os.path.join(DIRECTORIO_BASE, "..", "fosil_info", "familias.json")

modelo = YOLO(RUTA_MODELO)

with open(RUTA_JSON, "r", encoding="utf-8") as f:
    datos_info = json.load(f)

def predecir_imagen(ruta_imagen):
    resultados = modelo(ruta_imagen)

    probabilidades = resultados[0].probs
    nombres_clase = resultados[0].names

    if probabilidades is None:
        return "organismo o fósil desconocido", 0.0, []
    
    confianza = float(probabilidades.top1conf)

    top_3_clases_predecidas = probabilidades.top5[:3]
    predicciones = []

    for i in top_3_clases_predecidas:
        clase = nombres_clase[i]
        clase = clase.lower().strip().replace(" ", "_")
        predicciones.append({
            "clase": clase,
            "confianza": round(float(probabilidades.data[i]), 3),
            "info": datos_info.get(clase, {})
        })
    
    if confianza < 0.50:
        return "La probabilidad es demasiado baja como para afirmar con seguridad que el fósil pertenezca a una clase.", confianza, predicciones
    
    clase_predecida = nombres_clase[probabilidades.top1]
    clase_predecida = clase_predecida.lower().strip().replace(" ", "_")

    return clase_predecida, confianza, predicciones

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/prediccion", methods=["POST"])
def prediccion():
    if "archivo" not in request.files:
        return jsonify({"error": "No se ha enviado ninguna imagen"}), 400
    
    archivo = request.files["archivo"]

    if archivo.filename == "":
        return jsonify({"error": "Nombre de archivo vacío"}), 400
    
    ruta_imagen = os.path.join(CARPETA_IMG_SUBIDAS, archivo.filename)
    archivo.save(ruta_imagen)

    clase_predecida, confianza, predicciones = predecir_imagen(ruta_imagen)
    info = datos_info.get(clase_predecida, {})

    return jsonify({"clase": clase_predecida,
                    "confianza": round(confianza, 3),
                    "info": info, "imagen": f"http://127.0.0.1:5000/imagenes/{archivo.filename}",
                    "top_3_predicciones": predicciones})

@app.route("/imagenes/<nombre>")
def mostrar_imagen(nombre):
    return send_from_directory(CARPETA_IMG_SUBIDAS, nombre)

if __name__ == "__main__":
    app.run(debug=True)