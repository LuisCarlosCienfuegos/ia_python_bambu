# bambu_ia

Proyecto de pruebas con Python para clasificación de imágenes y una app simple en Streamlit.

## Contenido

- `predict.py`: script de predicción usando un modelo `.h5`.
- `mejor_modelo_cifar10.h5`: modelo entrenado.
- `imagesModelo.jpg`: imagen de ejemplo.
- `Nueva_app/algo.py`: app web básica en Streamlit.

## Requisitos

- Windows con PowerShell
- Python 3.10 o compatible

## Ejecutar `predict.py`

Crear y activar entorno virtual:

```powershell
cd C:\dockerImagenes\ia_python_bambu
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install tensorflow pillow matplotlib numpy opencv-python
```

Ejecutar el script:

```powershell
python .\predict.py
```

Nota:
`predict.py` todavía usa rutas de Google Colab como `/content/...`. Antes de correrlo en local, conviene ajustar esas rutas para que apunten a archivos dentro de esta carpeta.

## Ejecutar `Nueva_app/algo.py`

Usando el entorno virtual dentro de `Nueva_app`:

```powershell
cd C:\dockerImagenes\ia_python_bambu
.\Nueva_app\venv\Scripts\python.exe -m pip install streamlit
.\Nueva_app\venv\Scripts\python.exe -m streamlit run .\Nueva_app\algo.py
```

## Estructura

```text
bambu_ia/
|-- predict.py
|-- mejor_modelo_cifar10.h5
|-- imagesModelo.jpg
|-- Nueva_app/
|   |-- algo.py
```

## Git

Repositorio inicializado con rama principal `main`.
