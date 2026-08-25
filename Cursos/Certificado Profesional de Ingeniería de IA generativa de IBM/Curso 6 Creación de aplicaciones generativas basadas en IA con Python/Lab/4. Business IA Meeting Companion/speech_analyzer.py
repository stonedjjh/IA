import torch
import os
import gradio as gr

#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
mis_credenciales = {
    "url": "https://us-south.ml.cloud.ibm.com"
}
params = {
    GenParams.MAX_NEW_TOKENS: 800,  # El número máximo de tokens que el modelo puede generar en una sola ejecución.
    GenParams.TEMPERATURE: 0.1,    # Un parámetro que controla la aleatoriedad de la generación de tokens.
}
modelo_LLAMA2 = Model(
    model_id='meta-llama/llama-4-maverick-17b-128e-instruct-fp8',
    credentials=mis_credenciales,
    params=params,
    project_id="skills-network",
)
llm = WatsonxLLM(modelo_LLAMA2)
#######------------- Plantilla de Prompt -------------####
temp = """
<s><<sys>>
Enumera los puntos clave con detalles del contexto: 
[INST] El contexto : {context} [/INST] 
<</sys>>
"""
pt = PromptTemplate(
    input_variables=["context"],
    template=temp
)
prompt_a_LLAMA2 = LLMChain(llm=llm, prompt=pt)
#######------------- De voz a texto -------------####
def transcribir_audio(audio_file):
    # Inicializa la pipeline de reconocimiento de voz
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    # Transcribe el archivo de audio y devuelve el resultado
    transcripcion_txt = pipe(audio_file, batch_size=8)["text"]
    resultado = prompt_a_LLAMA2.run(transcripcion_txt)
    return resultado
#######------------- Gradio -------------####
entrada_audio = gr.Audio(sources="upload", type="filepath")
texto_salida = gr.Textbox()
iface = gr.Interface(
    fn=transcribir_audio,
    inputs=entrada_audio,
    outputs=texto_salida,
    title="Aplicación de Transcripción de Audio",
    description="Sube el archivo de audio"
)

iface.launch(server_name="0.0.0.0", server_port=7860)