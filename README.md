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

## Solución de errores para `predict.py`

Si `predict.py` no se ejecuta correctamente, reconstruye el entorno virtual con estos comandos:

```powershell
# 0) Ir al proyecto
cd C:\dockerImagenes\ia_python_bambu

# 1) Salir del venv actual (si está activo)
deactivate

# 2) Borrar entorno roto/anterior
Remove-Item -Recurse -Force .\.venv

# 3) Crear venv con Python 3.10
py -3.10 -m venv .venv

# 4) Activar venv
.\.venv\Scripts\Activate.ps1

# 5) Confirmar versión correcta
python --version
python -m pip --version

# 6) Actualizar pip/setuptools/wheel
python -m pip install --upgrade pip setuptools wheel

# 7) Instalar paquetes
python -m pip install tensorflow pillow matplotlib numpy
```

## Ejecutar `Nueva_app/algo.py`

Usando el entorno virtual dentro de `Nueva_app`:

```powershell
cd C:\dockerImagenes\ia_python_bambu
.\Nueva_app\venv\Scripts\python.exe -m pip install streamlit
.\Nueva_app\venv\Scripts\python.exe -m streamlit run .\Nueva_app\algo.py
```

`algo.py` es una app sencilla en Streamlit que funciona como una calculadora: recibe un número y muestra el 16% de ese valor.

## Deploy de `algo.py`

El despliegue se hará únicamente para `Nueva_app/algo.py` usando Streamlit Cloud:

`https://share.streamlit.io/deploy`

Nota:
Este deploy aplica solo a la app tipo calculadora hecha en Streamlit. No aplica a `predict.py`.

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


## Proyecto de Análisis de Sentimientos

```powershell
cd analisis_sentimientos
python -m venv venv #crear el entorno
venv\Scripts\activate #activar ele entorno
pip install gradio joblib scikit-learn pandas nltk imbalanced-learn #instralar librerias
```
