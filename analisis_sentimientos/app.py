import joblib
import gradio as gr
from text_utils import limpiar_texto

modelo_cargado = joblib.load("sentiment_model.joblib")

# Extraer vectorizer y modelo
vectorizer = modelo_cargado["vectorizer"]
model = modelo_cargado["model"]

def predecir_sentimiento(texto_usuario):
    if not texto_usuario or not texto_usuario.strip():
        return "Por favor escribe una reseña."

    texto_limpio = limpiar_texto(texto_usuario)
    texto_vect = vectorizer.transform([texto_limpio])
    prediccion = model.predict(texto_vect)[0]

    etiqueta = "Positivo" if prediccion == 1 else "Negativo"
    return f"Sentimiento detectado: {etiqueta}"

demo = gr.Interface(
    fn=predecir_sentimiento,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Escribe aquí una reseña de Alexa..."
    ),
    outputs=gr.Textbox(label="Resultado"),
    title="Análisis de sentimientos",
    description="Escribe una reseña y el modelo predice si el sentimiento es positivo o negativo.",
    examples=[
        ["I love this device, it works great"],
        ["This is a bad device"],
        ["Amazing sound and very easy to use"],
        ["It stopped working after one day"]
    ]
)

if __name__ == "__main__":
    demo.launch()