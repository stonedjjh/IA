::page{title="Compañero de Reuniones de IA Empresarial STT"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-WD0231EN-SkillsNetwork/IDSN-logo.png" alt="cognitiveclass.ai logo" width="200" />

## Introducción

Imagina que estás asistiendo a una reunión de negocios donde todas las conversaciones están siendo capturadas por una aplicación avanzada de IA. Esta aplicación no solo transcribe las discusiones con alta precisión, sino que también proporciona un resumen conciso de la reunión, enfatizando los puntos clave y las decisiones tomadas.

En nuestro proyecto, utilizaremos Whisper de OpenAI para transformar el habla en texto. A continuación, usaremos la IA de IBM Watson para resumir y encontrar puntos clave. Crearemos una aplicación con Hugging Face Gradio como interfaz de usuario.

### Objetivos de Aprendizaje

Después de finalizar este laboratorio, podrás:

-   Crear un script en Python para generar texto utilizando un modelo del Hugging Face Hub, identificar algunos parámetros clave que influyen en la salida del modelo y tener una comprensión básica de cómo cambiar entre diferentes modelos LLM.
    
-   Utilizar la tecnología Whisper de OpenAI para convertir grabaciones de conferencias en texto, de manera precisa.
    
-   Implementar la IA de IBM Watson para resumir de manera efectiva las conferencias transcritas y extraer puntos clave.
    
-   Crear una interfaz intuitiva y fácil de usar utilizando Hugging Face Gradio, asegurando la facilidad de uso para estudiantes y educadores.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0V2VEN/images/DALL%C2%B7E%202024-02-29%2014.12.41%20-%20In%20a%20minimalist%20meeting%20room%20with%20a%20large%2C%20plain%20round%20table%2C%20a%20small%20and%20simple%20digital%20display%20is%20mounted%20on%20a%20white%20wall.%20The%20display%20shows%20%27Key%20Po.webp" alt="langchain" width="500px" />

 Generado por DALLE-3

## Preparando el entorno

Comencemos configurando el entorno creando un entorno virtual de Python e instalando las bibliotecas necesarias, utilizando los siguientes comandos en la terminal:

```bash
pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env

```


Luego, instala las bibliotecas necesarias en el entorno (esto tomará tiempo ☕️☕️):

```bash
# installing required libraries in my_env
pip install --force-reinstall "setuptools<70" transformers==4.36.0 torch==2.1.1 gradio==5.23.2 langchain==0.0.343 ibm_watson_machine_learning==1.0.335 huggingface-hub==0.28.1

```


&nbsp;

Toma una taza de café, tomará unos minutos.

```
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'

```


Necesitamos instalar `ffmpeg` para poder trabajar con archivos de audio en python.

```bash
sudo apt update

```


Luego ejecuta:

```bash
sudo apt install ffmpeg -y

```


> Whisper de OpenAI está disponible en [github](https://github.com/openai/whisper). El código y los pesos del modelo de Whisper se publican bajo la Licencia MIT. Consulta [LICENSE](https://github.com/openai/whisper/blob/main/LICENSE) para más detalles.

::page{title="Paso 1: De voz a texto"}

Inicialmente, queremos crear un archivo Python simple de voz a texto utilizando OpenAI Whisper.

Puedes probar el archivo de audio de muestra **Voz de muestra** [\*\*enlace para descargar.\*\*](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3)

Crea y abre un archivo Python y llámalo `simple_speech2text.py` haciendo clic en el enlace de abajo:

&nbsp;

&nbsp;

::openFile{path="simple_speech2text.py"}

Primero descarguemos el archivo (puedes hacerlo manualmente, luego arrástralo y suéltalo en el entorno de archivos).

```python
import requests

# URL of the audio file to be downloaded
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"

# Send a GET request to the URL to download the file
response = requests.get(url)

# Define the local file path where the audio file will be saved
audio_file_path = "downloaded_audio.mp3"

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # If successful, write the content to the specified local file path
    with open(audio_file_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    # If the request failed, print an error message
    print("Failed to download the file")

```


Ejecuta el archivo de Python para probarlo.

```bash
python3 simple_speech2text.py

```


Deberías ver el archivo de audio descargado en el explorador de archivos.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/images/whisper_download.jpg.jpg" alt="langchain" width="300px" />

A continuación, implementa OpenAI Whisper para transcribir voz a texto.

Puedes sobrescribir el código anterior en el archivo Python.

```python
import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline from Hugging Face Transformers
# This uses the "openai/whisper-tiny.en" model for automatic speech recognition (ASR)
# The `chunk_length_s` parameter specifies the chunk length in seconds for processing
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-tiny.en",
  chunk_length_s=30,
)

# Define the path to the audio file that needs to be transcribed
sample = 'downloaded_audio.mp3'

# Perform speech recognition on the audio file
# The `batch_size=8` parameter indicates how many chunks are processed at a time
# The result is stored in `prediction` with the key "text" containing the transcribed text
prediction = pipe(sample, batch_size=8)["text"]

# Print the transcribed text to the console
print(prediction)

```


Ejecuta el archivo de Python y obtendrás la salida.

```bash
python3 simple_speech2text.py

```


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/images/whisper%20simple%20result.jpg" alt="langchain" width="600px" />

En el siguiente paso, utilizaremos `Gradio` para crear la interfaz de nuestra aplicación.

::page{title="Interfaz de Gradio"}

## Creando una demostración simple

A través de este proyecto, crearemos diferentes aplicaciones de LLM con la interfaz de Gradio. Familiaricémonos con Gradio creando una aplicación simple:

Aún en el directorio `project`, crea un archivo de Python y nómbralo `hello.py`.

Abre `hello.py`, pega el siguiente código de Python y guarda el archivo.

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)

```


El código anterior crea una **gradio.Interface** llamada `demo`. Envuelve la función `greet` con una interfaz de usuario simple de texto a texto con la que puedes interactuar.

La clase **gradio.Interface** se inicializa con 3 parámetros obligatorios:

-   fn: la función a la que se le aplicará la interfaz
    
-   inputs: qué componente(s) usar para la entrada (por ejemplo, "texto", "imagen" o "audio")
    
-   outputs: qué componente(s) usar para la salida (por ejemplo, "texto", "imagen" o "etiqueta")
    

La última línea `demo.launch()` lanza un servidor para servir nuestro `demo`.

## Lanzando la aplicación de demostración

Ahora vuelve a la terminal y asegúrate de que el nombre del entorno virtual `my_env` se muestre al principio de la línea.

A continuación, ejecuta el siguiente comando para ejecutar el script de Python.

```bash
python3 hello.py

```


Como el código de Python se sirve desde un host local, haz clic en el botón de abajo y podrás ver la aplicación simple que acabamos de crear. ¡Siéntete libre de experimentar con la entrada y salida de la aplicación web!

Haz clic aquí para ver la aplicación:

&nbsp;

&nbsp;

::startApplication{port="7860" route="/" display="internal" name="Aplicación web"}

Deberías ver lo siguiente, aquí ingresamos el nombre Bob:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0ZLFEN/images/bob.png)

Si terminas de jugar con la aplicación y deseas salir, **presiona** `Ctrl+c` **en la terminal y cierra la pestaña de la aplicación**.

Si deseas aprender un poco más sobre la personalización en Gradio, estás invitado a realizar el proyecto guiado llamado **Dale vida a tu modelo de Machine Learning con Gradio**. Puedes encontrarlo en **Cursos y Proyectos** en [cognitiveclass.ai](https://cognitiveclass.ai/)!

Para el resto de este proyecto, utilizaremos Gradio como interfaz para aplicaciones LLM.

::page{title="Paso 2: Creando una aplicación de transcripción de audio"}

Crea un nuevo archivo de python `speech2text_app.py`

&nbsp;

&nbsp;

::openFile{path="speech2text_app.py"}

#### Ejercicio: Completa la función `transcript_audio`.

Desde el paso 1: completa las partes que faltan en la función `transcript_audio`.

```python
import torch
from transformers import pipeline
import gradio as gr

# Function to transcribe audio using the OpenAI Whisper model
def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline
    pipe = #-----> Fill here <----
	
    # Transcribe the audio file and return the result
    result = #-----> Fill here <----
    return result

# Set up Gradio interface
audio_input = gr.Audio(sources="upload", type="filepath")  # Audio input
output_text = gr.Textbox()  # Text output

# Create the Gradio interface with the function, inputs, and outputs
iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, outputs=output_text, 
                     title="Audio Transcription App",
                     description="Upload the audio file")

# Launch the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860)

```


<details>
<summary>Haz clic aquí para la respuesta</summary>
<pre><code class="language-python">import torch
from transformers import pipeline
import gradio as gr

# Función para transcribir audio usando el modelo OpenAI Whisper
def transcript_audio(audio_file):
    # Inicializa el pipeline de reconocimiento de voz
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    # Transcribe el archivo de audio y devuelve el resultado
    result = pipe(audio_file, batch_size=8)["text"]
    return result

# Configura la interfaz de Gradio
audio_input = gr.Audio(sources="upload", type="filepath")  # Entrada de audio
output_text = gr.Textbox()  # Salida de texto

# Crea la interfaz de Gradio con la función, entradas y salidas
iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, outputs=output_text, 
                     title="Aplicación de Transcripción de Audio",
                     description="Sube el archivo de audio")

# Inicia la aplicación de Gradio
iface.launch(server_name="0.0.0.0", server_port=7860)
</code></pre>
</details>

Luego, ejecuta tu aplicación:

```bash
python3 speech2text_app.py

```


Y comienza la aplicación:

&nbsp;

&nbsp;

::startApplication{port="7860" route="/" display="internal" name="Web application"}

Puedes descargar el archivo de audio de muestra que hemos proporcionado haciendo clic derecho sobre él en el explorador de archivos y seleccionando "Descargar". Una vez descargado, puedes subir este archivo a la aplicación. Alternativamente, siéntete libre de elegir y subir cualquier archivo de audio MP3 de tu computadora local.

El resultado será:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/images/speech2text_app.jpg" alt="langchain" width="600px" />

**Presiona Ctrl + C para detener la aplicación.**

::page{title="Paso 3: Integración de LLM: Usando Llama 3 en WatsonX como LLM"}

## Ejecución de LLM simple

Comencemos generando texto con LLMs. Crea un archivo de Python y nómbralo `simple_llm.py`. Puedes proceder haciendo clic en el enlace a continuación o haciendo referencia a la imagen que acompaña.

&nbsp;

&nbsp;

::openFile{path="simple_llm.py"}

En caso de que desees usar Llama 3 como una instancia de LLM, puedes seguir las instrucciones a continuación:

> IBM WatsonX utiliza varios modelos de lenguaje, incluido Llama 3 de Meta, que es actualmente el modelo de lenguaje de código abierto más potente.

Así es como funciona el código:

1.  **Configuración de credenciales**: Las credenciales necesarias para acceder a los servicios de IBM están preestablecidas por el equipo de Skills Network, por lo que no tienes que preocuparte por configurarlas tú mismo.
    
2.  **Especificación de parámetros**: El código define luego parámetros específicos para el modelo de lenguaje. 'MAX\_NEW\_TOKENS' establece el límite en el número de palabras que el modelo puede generar de una vez. 'TEMPERATURE' ajusta cuán creativo o predecible es el texto generado.
    
3.  **Configuración del modelo Llama 3**: A continuación, se configura el modelo LLAMA3 utilizando un ID de modelo, las credenciales proporcionadas, los parámetros elegidos y un ID de proyecto.
    
4.  **Creación de un objeto para Llama 3**: El código crea un objeto llamado llm, que se utiliza para interactuar con el modelo Llama 3. Se crea un objeto de modelo, LLAMA3\_model, utilizando la clase Model, que se inicializa con un ID de modelo específico, credenciales, parámetros e ID de proyecto. Luego, se crea una instancia de WatsonxLLM con LLAMA3\_model como argumento, inicializando el objeto del hub de modelo de lenguaje llm.
    
5.  **Generación e impresión de la respuesta**: Finalmente, se utiliza 'llm' para generar una respuesta a la pregunta, "¿Cómo leer un libro de manera efectiva?" La respuesta se imprime a continuación.

```python
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

my_credentials = {
    "url"    : "https://us-south.ml.cloud.ibm.com"
}

params = {
        GenParams.MAX_NEW_TOKENS: 700, # The maximum number of tokens that the model can generate in a single run.
        GenParams.TEMPERATURE: 0.1,   # A parameter that controls the randomness of the token generation. A lower value makes the generation more deterministic, while a higher value introduces more randomness.
    }

LLAMA2_model = Model(
        model_id= 'meta-llama/llama-4-maverick-17b-128e-instruct-fp8', 
        credentials=my_credentials,
        params=params,
        project_id="skills-network",  
        )

llm = WatsonxLLM(LLAMA2_model)  

print(llm("How to read a book effectively?"))

```


Puedes ejecutar este script en la terminal utilizando el siguiente comando:

```bash
python3 simple_llm.py

```


Al ejecutar el script, deberías ver el texto generado en tu terminal, como se muestra a continuación:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/images/llama2_read_book.jpg
" width="900" />

Puedes ver cómo watsonx Llama 2 proporciona una buena respuesta.

::page{title="Paso 4: Juntar todo"}

Crea un nuevo archivo de Python y llámalo `speech_analyzer.py`

&nbsp;

&nbsp;

::openFile{path="speech_analyzer.py"}

En este ejercicio, configuraremos una instancia de modelo de lenguaje (LLM), que podría ser IBM WatsonxLLM, HuggingFaceHub o un modelo de OpenAI. Luego, estableceremos una plantilla de aviso. Estas plantillas son guías estructuradas para generar avisos para modelos de lenguaje, ayudando a la organización de la salida (más información en [langchain prompt template](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/).

A continuación, desarrollaremos una función de transcripción que emplea el modelo Whisper de OpenAI para convertir el habla en texto. Esta función toma un archivo de audio subido a través de una interfaz de aplicación Gradio (preferiblemente en formato .mp3). El texto transcrito se alimenta luego a un LLMChain, que integra el texto con la plantilla de aviso y lo envía al LLM elegido. La salida final del LLM se muestra en el cuadro de texto de salida de la aplicación Gradio.

La salida debería verse así:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/images/final_result_whisper.jpg
" width="700" />

Observa cómo el LLM corrigió un pequeño error cometido por el modelo de habla a texto, resultando en una salida coherente y precisa.

## Ejercicio: Completa las partes que faltan:

```python
import torch
import os
import gradio as gr
#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

#######------------- LLM-------------####

# initiate LLM instance, this can be IBM WatsonX, huggingface, or OpenAI instance

llm = ###---> write your code here

#######------------- Prompt Template-------------####

# This template is structured based on LLAMA2. If you are using other LLMs, feel free to remove the tags
temp = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context : {context} [/INST] 
<</SYS>>
"""
# here is the simplified version of the prompt template
# temp = """
# List the key points with details from the context: 
# The context : {context} 
# """

pt = PromptTemplate(
    input_variables=["context"],
    template= temp)

prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=pt)

#######------------- Speech2text-------------####

def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline
    
	pipe = #------> write the code here
	
    # Transcribe the audio file and return the result
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
	# run the chain to merge transcript text with the template and send it to the LLM
    result = prompt_to_LLAMA2.run(transcript_txt) 

    return result

#######------------- Gradio-------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

# Create the Gradio interface with the function, inputs, and outputs
iface = #---> write code here

iface.launch(server_name="0.0.0.0", server_port=7860)

```


<details>
<summary>Haz clic aquí para la respuesta</summary>
<pre><code class="language-python">import torch
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
&lt;s&gt;&lt;&lt;sys&gt;&gt;
Enumera los puntos clave con detalles del contexto: 
[INST] El contexto : {context} [/INST] 
&lt;&lt;/sys&gt;&gt;
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
</code></pre>
</details>

Ejecuta tu código:

```bash
python3 speech_analyzer.py

```


Si no hay error, ejecuta la aplicación web:

&nbsp;

&nbsp;

::startApplication{port="7860" route="/" display="internal" name="Aplicación web"}

::page{title="Conclusión"}

¡Felicidades por completar este proyecto! Ahora has sentado una base sólida para aprovechar potentes Modelos de Lenguaje (LLMs) para tareas de generación de texto a partir de voz. Aquí tienes un breve resumen de lo que has logrado:

-   Generación de texto con LLM: Has creado un script en Python para generar texto utilizando un modelo del Hugging Face Hub, aprendido sobre algunos parámetros clave que influyen en la salida del modelo y tienes un entendimiento básico de cómo cambiar entre diferentes modelos de LLM.
    
-   Conversión de voz a texto: Utiliza la tecnología Whisper de OpenAI para convertir grabaciones de conferencias en texto de manera precisa.
    
-   Resumen de contenido: Implementa la IA de IBM Watson para resumir de manera efectiva las conferencias transcritas y extraer puntos clave.
    
-   Desarrollo de interfaz de usuario: Crea una interfaz intuitiva y fácil de usar utilizando Hugging Face Gradio, asegurando la facilidad de uso para estudiantes y educadores.
    

## Author(s)

#### Sina Nazeri

### © IBM Corporation. Todos los derechos reservados.

&nbsp;