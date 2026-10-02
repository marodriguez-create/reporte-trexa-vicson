"""Reporte TREXA - VICSON · Febeca
Muestra en Streamlit el reporte HTML que está en la carpeta `reporte/`.
Para publicar una versión nueva basta con subir el HTML descargado a esa carpeta del repositorio.
"""
import re
from datetime import datetime
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Reporte TREXA - VICSON", page_icon="📊", layout="wide",
                   initial_sidebar_state="collapsed")

# Quitar márgenes de Streamlit para que el reporte ocupe toda la pantalla
st.markdown("""
<style>
  .block-container{padding-top:0.6rem;padding-bottom:0;padding-left:0.6rem;padding-right:0.6rem;max-width:100%}
  header[data-testid="stHeader"]{height:0;background:transparent}
  iframe{border:0;border-radius:9px}
</style>
""", unsafe_allow_html=True)

CARPETA = Path(__file__).parent / "reporte"


def fecha_de(nombre: str):
    """Toma la fecha DD-MM-AAAA del nombre del archivo (Reporte_TREXA_VICSON_01-10-2026.html)."""
    m = re.search(r"(\d{2})-(\d{2})-(\d{4})", nombre)
    if not m:
        return datetime.min
    try:
        return datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return datetime.min


@st.cache_data(show_spinner=False)
def leer(ruta: str, mtime: float) -> str:  # mtime invalida la caché cuando cambia el archivo
    return Path(ruta).read_text(encoding="utf-8")


# Busca los reportes en la carpeta reporte/ y también en la raíz del repositorio
RAIZ = Path(__file__).parent
archivos = list(CARPETA.glob("*.html")) + list(RAIZ.glob("*.html"))
versiones = sorted(set(archivos), key=lambda p: (fecha_de(p.name), p.stat().st_mtime), reverse=True)

with st.sidebar:
    st.markdown("### Reporte TREXA - VICSON")
    if not versiones:
        st.error("No hay ningún archivo .html del reporte en el repositorio.")
        st.stop()
    elegido = st.selectbox("Versión", versiones, format_func=lambda p: p.name,
                           help="Por defecto se muestra la de fecha más reciente.")
    alto = st.slider("Alto de la vista (px)", 700, 2400, 1150, 50)

html = leer(str(elegido), elegido.stat().st_mtime)
nombre = elegido.name

with st.sidebar:
    st.download_button("Descargar este HTML", html.encode("utf-8"), file_name=nombre, mime="text/html",
                       use_container_width=True)
    st.caption("Los movimientos que pegues o cargues dentro del reporte se guardan en tu navegador. "
               "Usa «Descargar reporte actualizado» dentro del reporte para obtener el archivo nuevo.")

# st.iframe reemplaza a components.html en las versiones nuevas de Streamlit
if hasattr(st, "iframe"):
    st.iframe(html, height=alto)
else:
    components.html(html, height=alto, scrolling=True)
