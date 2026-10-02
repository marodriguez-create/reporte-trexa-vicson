# Reporte TREXA - VICSON · Febeca (Streamlit)

Publica en Streamlit Community Cloud el reporte HTML `reporte/Reporte_TREXA_VICSON_01-10-2026.html`.

## Contenido

```
reporte-trexa-vicson/
├── app.py                 # app de Streamlit que muestra el reporte
├── requirements.txt       # streamlit
├── .streamlit/config.toml # colores Febeca (tema claro)
└── reporte/               # aquí van los HTML del reporte
    └── Reporte_TREXA_VICSON_01-10-2026.html
```

La app muestra siempre el HTML con la fecha más reciente en el nombre (`..._DD-MM-AAAA.html`).
En la barra lateral se puede elegir otra versión, ajustar el alto de la vista o descargar el HTML.

## Probar en tu computador (opcional)

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Actualizar el reporte publicado

1. Dentro del reporte, carga o pega los movimientos y pulsa **Descargar reporte actualizado**.
2. En GitHub, abre la carpeta `reporte/` → **Add file → Upload files** → sube el HTML nuevo → **Commit changes**.
3. Streamlit se actualiza solo en uno o dos minutos y muestra la versión de fecha más reciente.

Los movimientos que se pegan dentro de la página se guardan solo en el navegador de quien los pega.
Para que todos vean los mismos datos, sube el HTML descargado al repositorio (paso 2).
