// Lógica de pestañas
const tabTexto = document.getElementById('tabTexto');
const tabArchivo = document.getElementById('tabArchivo');
const seccionTexto = document.getElementById('seccionTexto');
const seccionArchivo = document.getElementById('seccionArchivo');
const textareaIdea = document.getElementById('idea');
const inputArchivo = document.getElementById('archivoResumen');

let modoActual = 'texto';

tabTexto.addEventListener('click', () => {
    modoActual = 'texto';
    tabTexto.classList.add('activo');
    tabArchivo.classList.remove('activo');
    seccionTexto.classList.remove('oculto');
    seccionArchivo.classList.add('oculto');
    textareaIdea.required = true;
    inputArchivo.required = false;
});

tabArchivo.addEventListener('click', () => {
    modoActual = 'archivo';
    tabArchivo.classList.add('activo');
    tabTexto.classList.remove('activo');
    seccionArchivo.classList.remove('oculto');
    seccionTexto.classList.add('oculto');
    inputArchivo.required = true;
    textareaIdea.required = false;
});

// Envío del formulario
document.getElementById('ideaForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const nombre = document.getElementById('nombre').value;
    const btn = document.getElementById('btnAnalizar');
    const loading = document.getElementById('loading');
    const panelResultados = document.getElementById('resultados');

    // Estado UI: Cargando
    btn.disabled = true;
    loading.classList.remove('oculto');
    panelResultados.classList.add('oculto');

    // Usamos FormData porque enviamos archivos y texto mezclado
    const formData = new FormData();
    formData.append('nombre_cliente', nombre);
    formData.append('modo', modoActual);

    if (modoActual === 'texto') {
        formData.append('idea_texto', document.getElementById('idea').value);
    } else {
        const archivo = document.getElementById('archivoResumen').files[0];
        formData.append('archivo', archivo);
    }

    try {
        const response = await fetch('/api/analizar', {
            method: 'POST',
            // No enviamos JSON header, Fetch detecta FormData automáticamente
            body: formData 
        });

        const data = await response.json();

        if (data.estado === 'exito') {
            // 1. Rellenar Análisis IA
            document.getElementById('resSector').textContent = data.analisis_ia.sector;
            document.getElementById('resTech').textContent = data.analisis_ia.tecnologias.join(', ');
            document.getElementById('resTrl').textContent = data.analisis_ia.madurez_trl;
            document.getElementById('resResumen').textContent = data.analisis_ia.resumen_ejecutivo;

            // 2. Rellenar Socios con Explicabilidad
            const listaSocios = document.getElementById('listaSocios');
            listaSocios.innerHTML = '';
            if (data.socios && data.socios.length > 0) {
                data.socios.forEach(s => {
                    const badge = s.es_mejor_opcion ? '<div class="badge-mejor">⭐ MEJOR SOCIO</div>' : '';
                    listaSocios.innerHTML += `
                        <li class="item-lista">
                            ${badge}
                            <strong>${s.nombre}</strong>
                            <div class="explicacion">" ${s.explicacion} "</div>
                        </li>`;
                });
            } else {
                listaSocios.innerHTML = '<li>No se encontraron socios exactos para este proyecto.</li>';
            }

            // 3. Rellenar Subvenciones con Explicabilidad
            const listaSubvenciones = document.getElementById('listaSubvenciones');
            listaSubvenciones.innerHTML = '';
            if (data.subvenciones && data.subvenciones.length > 0) {
                data.subvenciones.forEach(sub => {
                    const badge = sub.es_mejor_opcion ? '<div class="badge-mejor">💰 MEJOR FINANCIACIÓN</div>' : '';
                    const presupuesto = sub.presupuesto ? ` - ${sub.presupuesto}€` : '';
                    
                    listaSubvenciones.innerHTML += `
                        <li class="item-lista">
                            ${badge}
                            <strong>${sub.titulo}</strong>${presupuesto}
                            <div class="explicacion">" ${sub.explicacion} "</div>
                        </li>`;
                });
            } else {
                listaSubvenciones.innerHTML = '<li>Aún no hay convocatorias activas para este sector.</li>';
            }

            // Mostrar el panel de resultados final
            panelResultados.classList.remove('oculto');
        } else {
            alert('Error en el análisis: ' + data.mensaje);
        }
    } catch (error) {
        alert('Fallo de conexión con el servidor. Revisa que main.py esté corriendo.');
        console.error(error);
    } finally {
        // Restaurar botón y ocultar mensaje de carga
        btn.disabled = false;
        loading.classList.add('oculto');
    }
});