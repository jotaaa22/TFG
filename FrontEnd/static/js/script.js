const archivoCargado = document.getElementById("archivoCargado");
const boton = document.getElementById("botonPrediccion");
const resultado = document.getElementById("resultado");

boton.addEventListener("click", async () => {
    const archivo = archivoCargado.files[0];

    if(!archivo){
        mostrarError("Seleccione una imagen para analizar.");
        return;
    }

    if (!archivo.name.toLowerCase().endsWith(".jpg") && !archivo.name.toLowerCase().endsWith(".jpeg") && !archivo.name.toLowerCase().endsWith(".png")){
        mostrarError("Formato no válido. Solo se permiten imágenes JPG, JPEG o PNG.");
        return;
        }

    const formData = new FormData();
    formData.append("archivo", archivo);

    try{
        const respuesta = await fetch("http://127.0.0.1:5000/prediccion", {
            method: "POST", body: formData
        });
        
        const info = await respuesta.json();

        if(!respuesta.ok){
            mostrarError(data.error || "Error al procesar la imagen.");
            return;
        }

        mostrarResultado(info);

    } catch (error){
        console.error(error);
        alert("Error al realizar la conexión con el servidor");
    }
});

function mostrarResultado(info){
    resultado.innerHTML = `
        <h2 class="mt-4">RESULTADO DE LA CLASIFICACIÓN</h2>

        <div class="row mt-3">

            <div class="col-md-4 text-center">
                <div class="card p-3 h-100 mb-3 top-card">
                    <img src="${info.imagen}" class="preview">
                </div>
            </div>

            <div class="col-md-8">

                <div class="card p-3 mb-3 top-card">
                    <h4>Resultado</h4>
                    <p><span class="info">Clase:</span> <span class="valor">${info.clase}</span></p>
                    <p><span class="info">Confianza:</span> <span class="valor">${info.confianza}</span></p>
                </div>

                <div class="card p-3 mb-3 top-card">
                    <h4>Información</h4>
                    <p><span class="info">Nombre:</span> <span class="valor">${info.info.nombre_esp || "N/A"}</span></p>
                    <p><span class="info">Tipo:</span> <span class="valor">${info.info.tipo || "N/A"}</span></p>
                    <div class ="taxonomia">
                        <p><span class="info">Taxonomía:</span></p>
                        ${
                            info.info.taxonomia ? Object.entries(info.info.taxonomia).filter(([clave, valor]) => valor && valor != "N/A").map(([clave, valor]) =>
                            `<p class="taxon">
                                <span class="info">${clave.charAt(0).toUpperCase() + clave.slice(1)}:</span>
                                <span class="valor">${valor}</span>
                            </p>
                            `).join("")
                            : `<p class="taxon"><span class="valor">N/A</span></p>`
                        }
                    </div>
                    <p><span class="info">Época:</span> <span class="valor">${info.info.epoca || "N/A"}</span></p>
                    <p><span class="info">Descripción:</span> <span class="valor">${info.info.descripcion || "N/A"}</span></p>
                    <p><span class="info">Características:</span> <span class="valor">${info.info.caracteristicas || "N/A"}</span></p>
                </div>

            </div>
        </div>

        <div class="mt-5">
            <h4>Top 3 predicciones</h4>

            <div class="row">
                ${info.top_3_predicciones.map(p => `
                    <div class="col-md-4">
                        <div class="card p-3 mt-3 top-card">
                            <p><span class="info"><strong>${p.clase}</strong></span> <span class="valor">(${p.confianza})</span></p>
                            <p class="valor">${p.info?.descripcion || ""}</p>
                        </div>
                    </div>
                `).join("")}
            </div>
        </div>
    `;
}

function mostrarError(mensaje){
    resultado.innerHTML = `
        <div class="alert alert-danger mt-4" role="alert">
            ${mensaje}
        </div>
    `;
}