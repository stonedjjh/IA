::page{title="Construir un Chatbot para Tus Datos"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-WD0231EN-SkillsNetwork/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo"  />

**Tiempo estimado necesario:** 60 min

## Introducción
En este proyecto, crearás un chatbot para tu propio archivo pdf utilizando Flask, un marco web popular, y LangChain, otro marco popular para trabajar con modelos de lenguaje grandes (LLMs). El chatbot que desarrolles no solo interactuará con los usuarios a través de texto, sino que también comprenderá y responderá preguntas relacionadas con el contenido de un documento específico.

¡Haz clic en el enlace de demostración a continuación para probar la aplicación final que crearás!

<a href="https://chatbot-for-own-data.xs6r134s1i6.us-east.codeengine.appdomain.cloud/" target="_blank" style="display: inline-block; background-color: #1c87c9; color: white; padding: 14px 20px; margin: 10px 2px; border: none; border-radius: 4px; cursor: pointer; font-size: 20px; text-decoration: none;">Prueba la aplicación de demostración</a>

Al final de este proyecto, obtendrás una comprensión más profunda de los chatbots, el desarrollo de aplicaciones web utilizando Flask y Python, y el uso del marco LangChain para interpretar y responder a una amplia variedad de entradas de usuario. Y lo más importante, ¡habrás construido una aplicación de chatbot completa e impresionante!

<div style="text-align:center">
<figure>
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0DTPEN/images/antonio_33943_a_person_is_search_a_paper_in_huge_pile_of_papers_bde54ec4-2671-4f77-abb1-3e77811d93db.png
" width="500" alt="">
<figcaption>Una persona busca un documento en una enorme pila de papeles.</figcaption>
</figure>
</div>

</br>
Antes de comenzar, veamos los elementos clave que utilizarás para construir tu aplicación.

### Chatbots
Los chatbots son aplicaciones de software diseñadas para participar en conversaciones similares a las humanas. Pueden responder a entradas de texto de los usuarios y se utilizan ampliamente en varios dominios, incluidos el servicio al cliente, el comercio electrónico y la educación. En este proyecto, construirás un chatbot capaz de no solo involucrar a los usuarios en una conversación general, sino también de responder consultas basadas en un documento particular.

### LangChain
LangChain es una herramienta versátil para construir aplicaciones de lenguaje impulsadas por IA. Proporciona diversas funcionalidades como recuperación de texto, resumido, traducción y muchas más, aprovechando modelos de lenguaje preentrenados. En este proyecto, integrarás LangChain en tu chatbot, dándole la capacidad de comprender y responder a diversas entradas de usuario de manera efectiva.

### Flask
Flask es un marco web ligero y flexible para Python, conocido por su simplicidad y velocidad. Un marco web es un marco de software diseñado para apoyar el desarrollo de aplicaciones web, incluida la creación de servidores web y la gestión de solicitudes y respuestas HTTP.

Utilizarás Flask para crear el lado del servidor o backend de tu chatbot. Esto implica manejar los mensajes entrantes de los usuarios, procesar estos mensajes y enviar respuestas adecuadas de vuelta al usuario.

### Rutas en Flask
Las rutas son una parte esencial del desarrollo web. Cuando tu aplicación recibe una solicitud de un cliente (típicamente un navegador web), necesita saber cómo manejar esa solicitud. Aquí es donde entra el enrutamiento.

En Flask, las rutas se crean utilizando el decorador @app.route para vincular una función a una ruta URL. Cuando un usuario visita esa URL, se ejecuta la función asociada. En tu proyecto de chatbot, utilizarás rutas para manejar las solicitudes POST que llevan los mensajes de los usuarios y para procesar los datos del documento.

### HTML - CSS - JavaScript

Se te proporciona un front-end de chatbot listo para usar, construido con HTML, CSS y JavaScript. HTML estructura el contenido web, CSS lo estiliza y JavaScript añade interactividad. Estas tecnologías crean una interfaz de chatbot visualmente atractiva e interactiva.

Aquí hay una instantánea de la interfaz:
<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0WEVEN/images/PDF_chatbot1.png" width="400" alt="">
</div>
<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0WEVEN/images/PDF_chatbot2.png" width="400" alt="">
</div>
<div style="text-align:center">
	Interfaz del Chatbot 
</div>

## Objetivos de aprendizaje
Al final de este proyecto, serás capaz de:

- Explicar los conceptos básicos de Langchain y las aplicaciones de IA
- Configurar un entorno de desarrollo para construir un asistente utilizando Python Flask
- Implementar la funcionalidad de carga de PDF para permitir que el asistente comprenda los archivos de entrada de los usuarios
- Integrar el asistente con modelos de código abierto para darle un alto nivel de inteligencia y la capacidad de comprender y responder a las solicitudes de los usuarios
- (Opcional) Desplegar el asistente de PDF en un servidor web para su uso por un público más amplio

## Requisitos previos

Tener conocimientos básicos de HTML/CSS, JavaScript y Python es recomendable, pero no esencial. Cada paso del proceso y el código tendrán una explicación completa en este laboratorio.

Con esto en mente, ¡comencemos con tu proyecto!

::page{title="Configuración y comprensión de la interfaz de usuario"}

En este proyecto, el objetivo es crear un chatbot con una interfaz que permita la comunicación.

Primero, configuremos el entorno ejecutando el siguiente código:

```bash
pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env
```


El frontend utilizará HTML, CSS y JavaScript. La interfaz de usuario será similar a muchos chatbots que ves y usas en línea. El código para la interfaz se proporciona y el enfoque de este proyecto guiado es conectar esta interfaz con el backend que maneja la carga de tus documentos personalizados e integrarlo con un modelo LLM para obtener respuestas personalizadas. El código proporcionado te ayudará a entender cómo interactúan el frontend y el backend, y a medida que lo revises, aprenderás sobre las partes importantes y cómo funciona, dándote una comprensión clara de cómo funciona el frontend y cómo crear esta simple página web.

Ejecuta los siguientes comandos para recuperar el proyecto, darle un nombre apropiado y finalmente moverte a ese directorio ejecutando lo siguiente:

```bash
git clone https://github.com/ibm-developer-skills-network/wbphl-build_own_chatbot_without_open_ai.git
mv wbphl-build_own_chatbot_without_open_ai build_chatbot_for_your_data
cd build_chatbot_for_your_data
```


instalando los requisitos para el proyecto

```bash
pip install -r requirements.txt
```


```bash
pip install "langchain==0.3.27" "langchain-core==0.3.80" "langchain-community==0.3.31" "langchain-huggingface==0.3.1" "langchain-text-splitters==0.3.11" "huggingface-hub==0.36.0" "tokenizers==0.19.1" "transformers==4.43.3" "sentence-transformers==2.7.0" "requests==2.32.5"
```


Toma una taza de café, tomará de 5 a 10 minutos instalar los requisitos (Puedes continuar con este proyecto mientras se instalan los requisitos).

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


La siguiente sección ofrece una breve comprensión de cómo funciona el frontend.

### HTML, CSS y JavaScript

El archivo `index.html` es responsable del diseño y la estructura de la interfaz web. Este archivo contiene el código para incorporar bibliotecas externas como JQuery, Bootstrap y FontAwesome Icons, así como el código CSS (`style.css`) y JavaScript (`script.js`) que controlan el estilo y la interactividad de la interfaz.

El archivo `style.css` es responsable de personalizar la apariencia visual de los componentes de la página. También gestiona la animación de carga utilizando keyframes de CSS. Los keyframes son una forma de definir los valores de una animación en varios puntos en el tiempo, permitiendo una transición suave entre diferentes estilos y creando animaciones dinámicas.

El archivo `script.js` es responsable de la interactividad y funcionalidad de la página. Contiene la mayor parte del código y maneja todas las funciones necesarias, como cambiar entre modo claro y oscuro, enviar mensajes y mostrar nuevos mensajes en la pantalla. Incluso permite a los usuarios grabar audio.

::page{title="Entendiendo el trabajador: Procesamiento de documentos y gestión de conversaciones, parte 1"}

`worker.py` es parte de una aplicación de chatbot que procesa mensajes de usuarios y documentos. Utiliza la biblioteca `langchain`, que es una biblioteca de Python para construir aplicaciones de IA conversacional. Es responsable de configurar el modelo de lenguaje, procesar documentos PDF en un formato que se pueda utilizar para la recuperación de conversaciones y manejar las solicitudes de los usuarios para generar respuestas basadas en los documentos procesados. Aquí hay una descripción general del script:

::openFile{path="build_chatbot_for_your_data/worker.py"}

**Tu tarea es completar los comentarios de `worker.py` con el código apropiado.**

Desglosemos cada sección en el archivo worker.
El worker.py está diseñado para proporcionar una interfaz conversacional que puede responder preguntas basadas en el contenido de un documento PDF dado.

| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0DTPEN/images/document%20processing.jpg" width="900" alt="análisis humano"> |
|:--:| 
| El diagrama ilustra el procedimiento de procesamiento de documentos y recuperación de información, integrando sin problemas un modelo de lenguaje grande (LLM) para facilitar la tarea de responder preguntas. Todo el proceso ocurre en `worker.py`. *crédito de la imagen [enlace](https://www.linkedin.com/pulse/question-answer-bot-using-openai-langchain-faiss-satish-srinivasan/).* |

1. Inicialización `init_llm()`:
	- Configuración de variables de entorno: Se establece la variable de entorno para el token de la API de HuggingFace.
	- Carga del modelo de lenguaje: El modelo de lenguaje WatsonX se inicializa con parámetros especificados.
	- Carga de embeddings: Los embeddings se inicializan utilizando un modelo preentrenado.
	
2. Procesamiento de documentos `process_document(document_path)`:
	Esta función es responsable de procesar un documento PDF dado.
	- Carga del documento: El documento se carga utilizando PyPDFLoader.
	- División de texto: El documento se divide en fragmentos más pequeños usando RecursiveCharacterTextSplitter.
	- Creación de base de datos de embeddings: Se crea una base de datos de embeddings a partir de los fragmentos de texto usando Chroma.
	- Configuración de la cadena RetrievalQA: Se configura una cadena RetrievalQA para facilitar el proceso de respuesta a preguntas. Esta cadena utiliza el modelo de lenguaje inicializado y la base de datos de embeddings para responder preguntas basadas en el documento procesado.

3. Procesamiento de solicitudes de usuario `process_prompt(prompt)`:
	Esta función procesa la solicitud o pregunta de un usuario.

	- Recepción de la solicitud del usuario: El sistema recibe una solicitud del usuario (pregunta).
	- Consulta al modelo: Se consulta al modelo utilizando la cadena de recuperación, y genera una respuesta basada en el documento procesado y el historial de chat anterior.
	- Actualización del historial de chat: El historial de chat se actualiza con la nueva solicitud y respuesta.

## Profundizando en cada sección

> IBM watsonX utiliza varios modelos de lenguaje, incluidos los modelos Llama de Meta, que han sido algunos de los modelos de lenguaje de código abierto más potentes publicados hasta ahora (en febrero de 2024).

1. Inicialización `init_llm()`:

Este código es para configurar y usar un modelo de lenguaje de IA, de IBM watsonX:

1. **Configuración de credenciales**: Inicializa un diccionario con la URL del servicio y un token de autenticación (`"skills-network"`).

2. **Configuración de parámetros**: Establece parámetros del modelo como la generación máxima de tokens (`256`) y la temperatura (`0.1`, controlando la aleatoriedad).

3. **Inicialización del modelo**: Crea una instancia del modelo con un `model_id` específico, utilizando las credenciales y parámetros definidos anteriormente, y especifica `"skills-network"` como el ID del proyecto.

4. **Uso del modelo**: Inicializa una interfaz (`WatsonxLLM`) con el modelo configurado para la interacción.

Este script está específicamente configurado para un proyecto o entorno asociado con la "skills-network".

Completa el siguiente código en `worker.py` insertando los embeddings.

En este proyecto, no necesitas especificar tu propio `Watsonx_API` y `Project_id`. Solo puedes especificar `project_id="skills-network"` y dejar `Watsonx_API` en blanco.  

Pero es importante notar que este método de acceso es exclusivo para este entorno de Cloud IDE. Si estás interesado en usar el modelo/API fuera de este entorno (por ejemplo, en un entorno local), hay instrucciones detalladas y más información disponibles en este [tutorial](https://medium.com/the-power-of-ai/ibm-watsonx-ai-the-interface-and-api-e8e1c7227358).

```python
# placeholder for Watsonx_API and Project_id incase you need to use the code outside this environment
Watsonx_API = "Your WatsonX API"
Project_id= "Your Project ID"

# Function to initialize the language model and its embeddings
def init_llm():
    global llm_hub, embeddings

    logger.info("Initializing WatsonxLLM and embeddings...")

    # Llama Model Configuration
    MODEL_ID ="meta-llama/llama-4-maverick-17b-128e-instruct-fp8"
    WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
    PROJECT_ID = "skills-network"

    # Use the same parameters as before:
    #   MAX_NEW_TOKENS: 256, TEMPERATURE: 0.1
    model_parameters = {
        # "decoding_method": "greedy",
        "max_new_tokens": 256,
        "temperature": 0.1,
    }

    # Initialize Llama LLM using the updated WatsonxLLM API
    llm_hub = WatsonxLLM(
        model_id=MODEL_ID,
        url=WATSONX_URL,
        project_id=PROJECT_ID,
        params=model_parameters
    )
    logger.debug("WatsonxLLM initialized: %s", llm_hub)

    #Initialize embeddings using a pre-trained model to represent the text data.
    embeddings =  # create object of Hugging Face Embeddings with (model_name,  model_kwargs={"device": DEVICE} )
    
    logger.debug("Embeddings initialized with model device: %s", DEVICE)
```


<details>
	<summary>Haz clic aquí para ver la solución</summary>
  
  ```python
    
	 embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", 
        model_kwargs={"device": DEVICE}
    )
    logger.debug("Embeddings inicializados con el dispositivo del modelo: %s", DEVICE)

 ```
  </details>

::page{title="Comprendiendo el trabajador, parte 2"}

2. **Procesamiento de documentos:** la función `process_document` es responsable de procesar los documentos PDF. Utiliza el PyPDFLoader para cargar el documento, divide el documento en fragmentos utilizando el `RecursiveCharacterTextSplitter`, y luego crea un almacén de vectores (Chroma) a partir de los fragmentos del documento utilizando las incrustaciones del modelo de lenguaje. Este almacén de vectores se utiliza para crear una interfaz de recuperación, que se usa para crear un `ConversationalRetrievalChain`.

	* **Carga de documentos:** El documento PDF se carga utilizando la clase `PyPDFLoader`, que toma la ruta del documento como argumento. (Ejercicio: asignar PyPDFLoader(...) a `loader`)

	* **División de documentos:** El documento cargado se divide en fragmentos utilizando la clase `RecursiveCharacterTextSplitter`. Se pueden especificar el `chunk_size` y el `overlap`. (Ejercicio: asignar RecursiveCharacterTextSplitter(...) a `text_splitter`)

	* **Creación de almacén de vectores:** Se crea un almacén de vectores, que es una especie de índice, a partir de los fragmentos del documento utilizando las incrustaciones del modelo de lenguaje. Esto se realiza utilizando la clase `Chroma`.

	* **Configuración del sistema de recuperación:** Se configura un sistema de recuperación utilizando el almacén de vectores. Este sistema llama a un `ConversationalRetrievalChain`, utilizado para responder preguntas basadas en el contenido del documento.

Por hacer: completar las partes en blanco

```python
# Function to process a PDF document
def process_document(document_path):
    global conversation_retrieval_chain

    logger.info("Loading document from path: %s", document_path)
    # Load the document
    loader =  # ---> use PyPDFLoader and document_path from the function input parameter <---
    documents = loader.load()
    logger.debug("Loaded %d document(s)", len(documents))

    # Split the document into chunks, set chunk_size=1024, and chunk_overlap=64. assign it to variable text_splitter
    text_splitter = # ---> use Recursive Character TextSplitter and specify the input parameters <---
    texts = text_splitter.split_documents(documents)
    logger.debug("Document split into %d text chunks", len(texts))

    # Create an embeddings database using Chroma from the split text chunks.
    logger.info("Initializing Chroma vector store from documents...")
    db = Chroma.from_documents(texts, embedding=embeddings)
    logger.debug("Chroma vector store initialized.")

    # Optional: Log available collections if accessible (this may be internal API)
    try:
        collections = db._client.list_collections()  # _client is internal; adjust if needed
        logger.debug("Available collections in Chroma: %s", collections)
    except Exception as e:
        logger.warning("Could not retrieve collections from Chroma: %s", e)

    # Build the QA chain, which utilizes the LLM and retriever for answering questions. 
    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
        return_source_documents=False,
        input_key="question"
        # chain_type_kwargs={"prompt": prompt}  # if you are using a prompt template, uncomment this part
    )
    logger.info("RetrievalQA chain created successfully.")
```


<details>
	<summary>Haga clic aquí para ver la solución</summary>
  
  ```python	
# Función para procesar un documento PDF
def process_document(document_path):
    global conversation_retrieval_chain

    logger.info("Cargando documento desde la ruta: %s", document_path)

    # Cargar el documento
    loader = PyPDFLoader(document_path)
    documents = loader.load()
    logger.debug("Cargado %d documento(s)", len(documents))

    # Dividir el documento en fragmentos
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(documents)
    logger.debug("Documento dividido en %d fragmentos de texto", len(texts))

    # Crear una base de datos de embeddings usando Chroma a partir de los fragmentos de texto divididos
    logger.info("Inicializando la tienda de vectores Chroma a partir de documentos...")
    db = Chroma.from_documents(texts, embedding=embeddings)
    logger.debug("Tienda de vectores Chroma inicializada.")

    # Opcional: Registrar colecciones disponibles si son accesibles (esto puede ser una API interna)
    try:
        collections = db._client.list_collections()  # _client es interno; ajustar si es necesario
        logger.debug("Colecciones disponibles en Chroma: %s", collections)
    except Exception as e:
        logger.warning("No se pudieron recuperar colecciones de Chroma: %s", e)

    # Construir la cadena de QA, que utiliza el LLM y el recuperador para responder preguntas
    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
        return_source_documents=False,
        input_key="question"
        # chain_type_kwargs={"prompt": prompt}  # si está utilizando una plantilla de prompt, descomente esta parte
    )
    logger.info("Cadena RetrievalQA creada con éxito.")
  	
  ```
</details>

3. **Procesamiento de prompts (`process_prompt` function)**: Esta función maneja el prompt o pregunta de un usuario, recupera una respuesta basada en el contenido del documento PDF previamente procesado y mantiene un historial de chat. Hace lo siguiente:

    * Pasa el prompt y el historial de chat al objeto `ConversationalRetrievalChain`. `conversation_retrieval_chain` es la herramienta principal utilizada para consultar el modelo de lenguaje y obtener una respuesta basada en el contenido del documento PDF procesado.
    * Agrega el prompt y la respuesta del bot al historial de chat.
    * Devuelve la respuesta del bot.
	
Aquí hay un esqueleto de la función `process_prompt` para el ejercicio:

```python
# Function to process a user prompt
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history

    logger.info("Processing prompt: %s", prompt)
    # Query the model using the new .invoke() method
    output = conversation_retrieval_chain.invoke({"question": prompt, "chat_history": chat_history})
    answer = output["result"]
    logger.debug("Model response: %s", answer)

    # Update the chat history
    # TODO: Append the prompt and the bot's response to the chat history using chat_history.append and pass `prompt` `answer` as arguments
    # --> write your code here <--	
    
    logger.debug("Chat history updated. Total exchanges: %d", len(chat_history))

    # Return the model's response
    return answer
	
```


<details>
	<summary>Haz clic aquí para ver la solución</summary>
  
  ```python
  
# Función para procesar un aviso del usuario
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history

    logger.info("Procesando aviso: %s", prompt)

    # Consultar el modelo usando el método .invoke()
    output = conversation_retrieval_chain.invoke({
        "question": prompt,
        "chat_history": chat_history
    })
    answer = output["result"]
    logger.debug("Respuesta del modelo: %s", answer)

    # Actualizar el historial de chat
    chat_history.append((prompt, answer))
    logger.debug("Historial de chat actualizado. Total de intercambios: %d", len(chat_history))

    # Devolver la respuesta del modelo
    return answer
```

```
	
</details>

4. **Global variables:**
    
    * `llm` and `llm_embeddings` are used to store the language model and its embeddings `conversation_retrieval_chain` and `chat_history` is used to store the chat and history. `global` is used inside the functions `init_llm`, `process_document`, and `process_prompt` to indicate that the variables `llm`, `llm_embeddings`, `conversation_retrieval_chain`, and `chat_history` are global variables. This means that when these variables are modified inside these functions, the changes will persist outside the functions as well, affecting the global state of the program.

Here is the complete `worker.py`. 

<details>
	<summary>Click here to see the complete worker.py</summary>
	
```python	


```python
import os
import torch
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from langchain_core.prompts import PromptTemplate  # Importación actualizada según el aviso de desaprobación
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ibm import WatsonxLLM

# Verificar la disponibilidad de GPU y establecer el dispositivo apropiado para el cálculo.
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Variables globales
conversation_retrieval_chain = None
chat_history = []
llm_hub = None
embeddings = None

# Función para inicializar el modelo de lenguaje y sus embeddings
def init_llm():
    global llm_hub, embeddings

    logger.info("Inicializando WatsonxLLM y embeddings...")

    # Configuración del modelo Llama
    MODEL_ID = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"
    WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
    PROJECT_ID = "skills-network"

    # Parámetros del modelo
    model_parameters = {
        "max_new_tokens": 256,
        "temperature": 0.1,
    }

    # Inicializar Watsonx LLM
    llm_hub = WatsonxLLM(
        model_id=MODEL_ID,
        url=WATSONX_URL,
        project_id=PROJECT_ID,
        params=model_parameters
    )
    logger.debug("WatsonxLLM inicializado: %s", llm_hub)

    # Inicializar embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": DEVICE}
    )
    logger.debug("Embeddings inicializados con dispositivo: %s", DEVICE)

# Función para procesar un documento PDF
def process_document(document_path):
    global conversation_retrieval_chain

    logger.info("Cargando documento desde la ruta: %s", document_path)

    loader = PyPDFLoader(document_path)
    documents = loader.load()
    logger.debug("Cargados %d documento(s)", len(documents))

    # Dividir el documento en fragmentos
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(documents)
    logger.debug("Documento dividido en %d fragmentos de texto", len(texts))

    # Crear almacén de vectores Chroma
    logger.info("Inicializando almacén de vectores Chroma a partir de documentos...")
    db = Chroma.from_documents(texts, embedding=embeddings)
    logger.debug("Almacén de vectores Chroma inicializado.")

    # Opcional: Registrar colecciones disponibles
    try:
        collections = db._client.list_collections()  # _client es interno; ajustar si es necesario
        logger.debug("Colecciones disponibles en Chroma: %s", collections)
    except Exception as e:
        logger.warning("No se pudieron recuperar colecciones de Chroma: %s", e)

    # Construir la cadena QA
    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
        return_source_documents=False,
        input_key="question"
    )
    logger.info("Cadena RetrievalQA creada con éxito.")

# Función para procesar un aviso del usuario
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history

    logger.info("Procesando aviso: %s", prompt)

    output = conversation_retrieval_chain.invoke({"question": prompt, "chat_history": chat_history})
    answer = output["result"]
    logger.debug("Respuesta del modelo: %s", answer)

    # Actualizar el historial de chat
    chat_history.append((prompt, answer))
    logger.debug("Historial de chat actualizado. Total de intercambios: %d", len(chat_history))

    return answer

# Inicializar el modelo de lenguaje
init_llm()
logger.info("Inicialización de LLM y embeddings completa.")
```

```
</details>

::page{title="Running the app in CloudIDE"}

To implement your chatbot, you need to run the `server.py` file, first.
```bash


python3 server.py

```
You will have the following output in the terminal. This shows the server is running. 

<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0WEVEN/images/server%20running%20screenshot.png" width="500" alt="">
</div>
<div style="text-align:center">
	Server.py
</div>
(If you are running the file locally, you can open the browser and copy the running URL, in this case, it is `http://127.0.0.1:8000`.)

Now click the following button to open your application:

::startApplication{port="8000" display="internal" name="Open the application" route="/"}

A new window will open for your application.

<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0WEVEN/images/running_the_app_final_screenshot.png" width="500" alt="">
</div>
<div style="text-align:center">
	Chatbot Application
</div>

__Great job, you completed your project!__

If you want to understand the server file and JavaScript, continue with the project. You will also learn to containerize the app for deployment using Docker.

Once you\'ve had a chance to run and play around with the application, please press `Crtl` (a.k.a. `control (^)` for Mac) and `C` at the same time to stop the container and continue the project (as it is also mentioned in terminal).

::page{title="(optional) Using HuggingFace API for the worker"}

Another option for watsonX is using HuggingFace API. However, the model type and performance are very limited for the free version. As of Sep 2023, Llama2 is not supported for free, and you will use the `meta-llama/Llama-3.1-8B-Instruct` model instead.Please note since this is a free model, the results may not be fully accurate.

You need to update `init_llm` and insert your Hugging Face API key. 

    
    * The `HuggingFace` is hosting some LLM models which can be called free (if the model is below 10GB). You can also download any model and run it locally.
	

- Create the base LLM using `HuggingFaceEndpoint` : The HuggingFaceEndpoint object connects to a HuggingFace-hosted model using the Inference API.The `HuggingFaceEndpoint` object is created with the specified `repo_id` and additional parameters like `temperature`, `max_new_tokens` and your `your HuggingFace API token`to control the behavior of the model. [Here](https://python.langchain.com/docs/integrations/llms/huggingface_hub) you can find more examples.

- Wrap the base LLM with `ChatHuggingFace` : The `ChatHuggingFace` wrapper converts the base LLM into a chat-compatible model, allowing it to work seamlessly with LangChain chat-based chains (such as RetrievalQA).

- The embeddings are initialized using a class called `HuggingFaceEmbeddings`, pre-trained model named `sentence-transformers/all-MiniLM-L6-v2`. A list of leaderboards of embeddings are available [here](https://huggingface.co/spaces/mteb/leaderboard). This embedding model has shown a good balance in both performance and speed.

- The model uses the specified device (CPU or GPU) for computation.

To do: Complete the function `init_llm()`

```python


```python
def init_llm():
    global llm_hub, embeddings

    # Configurar la variable de entorno para HuggingFace
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "Tu API de HuggingFace"

    # Paso 1: Crear el LLM base utilizando HuggingFaceEndpoint
    base_llm = # --> crear HuggingFaceEndpoint con 
               #     repo_id="agregar nombre del modelo",
               #     task="text-generation",
               #     huggingfacehub_api_token="agregar variable de entorno",
               #     temperature=0.1,
               #     max_new_tokens=600

    # Paso 2: Envolver el LLM base con ChatHuggingFace para interacción basada en chat
    llm_hub = # --> envolver el base_llm utilizando ChatHuggingFace

    # Inicializar embeddings utilizando un modelo de transformador de oraciones preentrenado
    embeddings = # --> crear HuggingFaceEmbeddings con
                  #     model_name="sentence-transformers/all-MiniLM-L6-v2",
                  #     model_kwargs={"device": DEVICE}
```

```

<details>
	<summary>Click here to see the solution</summary>
  
  ```python
# Function to initialize the language model and its embeddings
def init_llm():
    global llm_hub, embeddings

    # Set HuggingFace API token
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR API KEY"

    # Initialize the base LLM endpoint
    base_llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        temperature=0.1,
        max_new_tokens=600,
    )

    # Wrap the base LLM with ChatHuggingFace for conversational capabilities
    llm_hub = ChatHuggingFace(llm=base_llm)

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": DEVICE},
    )

 ```
</details>

You also need to insert your LLM API key. Here\'s a demonstration to show you how to get your API key.

Initialize HuggingFace API key from your account with the following steps: 

1. Go to the https://huggingface.co/
2. Log in to your account (or sign up free if it is your first time)
3. Go to Settings -> Access Tokens -> click on New Token (refer image below)
4. Select either read or write option and copy the token

<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0DTPEN/images/HF%20key%201.png
" width="600" alt="">
</div>

<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0DTPEN/images/HF%20key%202.png
" width="600" alt="">
</div>
<div style="text-align:center">
	HuggingFace Token
</div>

<details>
	<summary>Click here to see the complete worker.py for huggingface version</summary>
  
```python


```python
import os
import torch

from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFaceEmbeddings,
    ChatHuggingFace,
)

# Verificar la disponibilidad de GPU
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Variables globales
conversation_retrieval_chain = None
chat_history = []
llm_hub = None
embeddings = None

# Inicializar el modelo de lenguaje y las incrustaciones
def init_llm():
    global llm_hub, embeddings

    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "TU CLAVE API"

    base_llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
        temperature=0.1,
        max_new_tokens=600,
    )

    # Envolver el LLM base con ChatHuggingFace
    llm_hub = ChatHuggingFace(llm=base_llm)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": DEVICE},
    )

# Procesar un documento PDF
def process_document(document_path):
    global conversation_retrieval_chain

    loader = PyPDFLoader(document_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=64
    )
    texts = text_splitter.split_documents(documents)

    db = Chroma.from_documents(texts, embedding=embeddings)

    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
        input_key="question",
    )

# Procesar un aviso del usuario
def process_prompt(prompt):
    global conversation_retrieval_chain, chat_history

    output = conversation_retrieval_chain.invoke(
        {"question": prompt, "chat_history": chat_history}
    )
    answer = output["result"]

    chat_history.append((prompt, answer))
    return answer.strip()

# Inicializar LLM y incrustaciones
init_llm()
```

```
    
</details>

To implement your chatbot, you need to run the `server.py` file, first.
```bash


python3 server.py

```
Now click the following button to open your application:

::startApplication{port="8000" display="internal" name="Open the application" route="/"}

A new window will open for your application.

<div style="text-align:center">
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0WEVEN/images/running_the_app_final_screenshot.png" width="500" alt="">
</div>
<div style="text-align:center">
	Chatbot Application
</div>

::page{title="Understanding the server"}

The server is how the application will run and communicate with all of your services. Flask is a web development framework for Python and can be used as a backend for the application. It is a lightweight and simple framework that makes it quick and easy to  build web applications.

With Flask, you can create web pages and applications without needing to know a lot of complex coding or use additional tools or libraries. You can create your own routes and handle user requests, and it also allows you to connect to external APIs and services to retrieve or send data.

This guided project uses Flask to handle the backend of your chatbot. This means that you will be using Flask to create routes and handle HTTP requests and responses. When a user interacts with the chatbot through the front-end interface, the request will be sent to the Flask backend. Flask will then process the request and send it to the appropriate service.

::openFile{path="build_chatbot_for_your_data/server.py"}

In `server.py`, at the top of the file, you import `worker` which refers to the worker.py file which you will use to handle the core logic of your chatbot. Underneath the imports, the Flask application is initialized, and a CORS policy is set. A CORS policy is used to allow or prevent web pages from making requests to different domains than the one that served the web page. Currently, it is set to `*` to allow any request.

The `server.py` file consists of 3 functions which are defined as routes, and the code to start the server.

The first route is:
```python


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

```
When a user tries to load the application, they initially send a request to go to the `/` endpoint. They will then trigger this `index` function and execute the code above. Currently, the returned code from the function is a render function to show the `index.html` file which is the frontend interface.

The second and third routes are what will be used to process all requests and handle sending information between the application. The `process_document_route()` function is responsible for handling the route when a user uploads a PDF document, processing the document, and returning a response. The `process_message_route()` function is responsible for processing a user\'s message or query about the processed document and returning a response from the bot.

Finally, the application is started with the `app.run` command to run on port `8080` and  the host as `0.0.0.0` (a.k.a. `localhost`).

::page{title=" (Optional) Explaining JavaScript file `Script.js`"}

The JavaScript file is responsible for managing the user interface and interactions of a chatbot application. It is located in `static` folder. The main components of the file are as follows:

1. **Message processing:**  The function `processUserMessage(userMessage)` sends a POST request to the server with the user\'s message and waits for a response. The server processes the message and returns a response that is displayed in the chat window.

```javascript


```javascript
const processUserMessage = async (userMessage) => {
  let response = await fetch(baseUrl + "/process-message", {
    method: "POST",
    headers: { Accept: "application/json", "Content-Type": "application/json" },
    body: JSON.stringify({ userMessage: userMessage }),
  });
  response = await response.json();
  console.log(response);
  return response;
};
```

``` 
2. **Loading animations:**  The functions `showBotLoadingAnimation()` and `hideBotLoadingAnimation()` show and hide a loading animation while the server is processing a message or document.

```javascript


```javascript
async function showBotLoadingAnimation() {
  await sleep(200);
  $(".loading-animation")[1].style.display = "inline-block";
  document.getElementById('send-button').disabled = true;
}

function hideBotLoadingAnimation() {
  $(".loading-animation")[1].style.display = "none";
  if(!isFirstMessage){
    document.getElementById('send-button').disabled = false;
  }
}
```

``` 
3. **Message display:**  The functions `populateUserMessage(userMessage, userRecording)` and `populateBotResponse(userMessage)` format and display user messages and bot responses in the chat window.

```javascript


```javascript
const populateUserMessage = (userMessage, userRecording) => {
  $("#message-input").val("");
  $("#message-list").append(
    `<div class='message-line my-text'><div class='message-box my-text${
      !lightMode ? " dark" : ""
    }'><div class='me'>${userMessage}</div></div></div>`
  );
  scrollToBottom();
};

const populateBotResponse = async (userMessage) => {
  // ... omitido por brevedad
  $("#message-list").append(
    `<div class='message-line'><div class='message-box${!lightMode ? " dark" : ""}'>${response.botResponse.trim()}<br>${uploadButtonHtml}</div></div>`
  );
  scrollToBottom();
};
```

``` 
4. **Input cleaning:**  The function `cleanTextInput(value)` cleans the user\'s input to remove unnecessary spaces, newlines, tabs, and HTML tags.

```javascript


```javascript
const cleanTextInput = (value) => {
  return value
    .trim() // eliminar espacios al inicio y al final
    .replace(/[\n\t]/g, "") // eliminar saltos de línea y tabulaciones
    .replace(/<[^>]*>/g, "") // eliminar etiquetas HTML
    .replace(/[<>&;]/g, ""); // sanitizar entradas
};
```

``` 
5. **File upload:**  The event listener for `$("#file-upload").on("change", ...)` handles the file upload process. When a file is selected, it reads the file data and sends it to the server for processing.

```javascript


```javascript
$("#file-upload").on("change", function () {
  const file = this.files[0];
  const reader = new FileReader();

  reader.onload = async function (e) {
    // Ahora envía estos datos al endpoint /process-document
    let response = await fetch(baseUrl + "/process-document", {
      method: "POST",
      headers: { Accept: "application/json", "Content-Type": "application/json" },
      body: JSON.stringify({ fileData: e.target.result }),
    });
    response = await response.json6. **Restablecer Chat:** El listener de eventos para `$("#reset-button").click(...)` proporciona una forma de restablecer el chat, borrando todos los mensajes y comenzando de nuevo con el saludo inicial del bot.
```

```

6. **Chat reset:** It provides a way to reset the chat, clearing all messages and starting over with the initial bot greeting.

	
```javascript


$("#reset-button").click(async function () {
  // Limpiar la lista de mensajes
  $("#message-list").empty();

  // Reiniciar el array de respuestas
  responses.length = 0;

  // Reiniciar la bandera isFirstMessage
  isFirstMessage = true;

  // Comenzar de nuevo
  populateBotResponse();
});

``` 
7. **Light/Dark mode switch:**  The event listener for `$("#light-dark-mode-switch").change(...)` allows the user to switch between light and dark modes for the chat interface.

```javascript


```javascript
$("#light-dark-mode-switch").change(function () {
  $("body").toggleClass("dark-mode");
  $(".message-box").toggleClass("dark");
  $(".loading-dots").toggleClass("dark");
  $(".dot").toggleClass("dark-dot");
  lightMode = !lightMode;
});
```

```

::page{title="Running the application"}

First, in the `server.py` you have the following code:

```python


if __name__ == "__main__":
	app.run(debug=True, port=8000, host='0.0.0.0')

```
The line `if __name__ == "__main__":` checks if the script is being run directly. If so, it starts the Flask application with `app.run(debug=True, port=8000, host='0.0.0.0')`. This starts a web server that listens on port 8000 and is accessible from any IP address (`'0.0.0.0'`). The server runs in debug mode (`debug=True`), which provides detailed error messages and automatically reloads the server when code changes.

### Creating the Docker container
Docker allows for the creation of "containers" that package an application and its dependencies together. This allows the application to run consistently across different environments, as the container includes everything it needs to run. Additionally, using a Docker image to create and run applications can simplify the deployment process, as the image can be easily distributed and run on any machine that has Docker. This easy distribution of image ensures that the application runs in the same way in development, testing, and production environments.

The `g&#8203;it clone` from the second page already comes with a `Dockerfile` and `requirements.txt` for this application. These files are used to build the image with the dependencies already installed. 

Replace the contents of the `Dockerfile` with the following.

```bash


# Usar la imagen base de Python 3.10
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . .

# Instalar dependencias desde requirements.txt
# Luego instalar versiones específicas de langchain, huggingface, transformers, etc.
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir \
       langchain==0.3.27 \
       langchain-core==0.3.80 \
       langchain-community==0.3.31 \
       langchain-huggingface==0.3.1 \
       langchain-text-splitters==0.3.11 \
       huggingface-hub==0.36.0 \
       tokenizers==0.19.1 \
       transformers==4.43.3 \
       sentence-transformers==2.7.0 \
       requests==2.32.5

# Exponer el puerto si es necesario (Flask por defecto 8000)
EXPOSE 8000

# Ejecutar el servidor
CMD ["python", "-u", "server.py"]

```

Looking into the `Dockerfile` you can see it is fairly simple, it just creates a Python environment, moves all the files from the local directory to the container, installs the required packages, and then starts the application by running the `p&#8203;ython` command.

### Starting the application

This image is quick to build as the application is quite small. These commands first build the application running the commands in the `Dockerfile` and provide a tag or name to the built container as `build_chatbot_for_your_data`, then run it in the foreground on `port 8000`. `no-cache` ensures Docker does not use any cached layers from previous builds. This forces a fresh build, which is useful when you\'ve made recent changes.**You\'ll need to run these commands every time you wish to make a new change to one of the files.**

```bash


docker build --no-cache -t build_chatbot_for_your_data .
docker run -p 8000:8000 build_chatbot_for_your_data

```

::startApplication{port="8000" display="external" name="Open app" route="/"}

*The application must be opened in a new tab since the minibrowser in this environment does not support certain required features.*

Your browser may deny "pop-ups" but please allow them for the new tab to open up.

At this point, the application will run but return `null` for any input.

Once you\'ve had a chance to run and play around with the application, please press `Crtl` (a.k.a. `control (^)` for Mac) and `C` at the same time to stop the container and continue the project.

The application will only run while the container is up. If you make new changes to the files and would like to test them, you will have to rebuild the image.

::page{title="Conclusion"}

**Congratulations on completing this guided project!** 
You learned how to implement "Retrieval Augmented Search", in Generative AI. You also learned how to work with LLMs, and vector store, how to create Embeddings, and how to integrate everything using Langchain.You created a real application, a chatbot, using Python, Flask, and JavaScript and you packaged and deployed it using containers and Kubernetes. You can share your achievements on LinkedIn, Twitter, and other social media. The guided project detail page has buttons to help you do this.

## Next steps
If generative AI and large language models (LLMs) interest you, we encourage you to apply for a [free trial of the IBM watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?utm_source=skills_network&utm_content=in_lab_content_link&utm_id=Lab-IBMSkillsNetwork-GPXX0DTPEN&context=wx). WatsonX is IBM enterprise-ready AI and data platform designed to multiply the impact of AI across your business. The platform comprises three powerful products: the watsonx.ai studio for new foundation models, generative AI and machine learning; and the watsonx.data fit-for-purpose data store, built on an open lakehouse architecture; and the watsonx.governance toolkit, to accelerate AI workflows that are built with responsibility, transparency, and explainability.

Moving forward, dive deeper into chatbot creation. The following guided project can assist you in acquiring the necessary skills for that endeavor. 

### [Create a voice assistant with IBM Watson]("https://cognitiveclass.ai/courses/chatapp-powered-by-openai")

Furthermore, you can delve into learning about Langchain and its functionalities. This allows you to add more capabilities to the chatbot, such as analyzing various types of files and generating output plots. Following guided project can be helpful.

### [Create AI-powered apps with open source LangChain]("https://cognitiveclass.ai/courses/course-v1:IBMSkillsNetwork+GPXX0W2REN+v1")

## Author(s)
#### Sina Nazeri 
#### Talha Siddiqui 
## <h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>
<!--
## Change log
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2023-06-15 | 0.1 | Sina Nazeri, Talha Siddiqui| Created project first draft |
| 2024-03-28 | 0.2 | Javed Ansari | Fixed QA comments |
| 2024-04-09 | 0.3 | Anita Narain| Id Reviewed |
| 2025-03-25 | 0.4 | Ratima| Added Instruction |
| 2025-05-26 | 0.5 | Sapthashree| Update the repo link |
| 2025-12-26 | 0.5 | Sapthashree| Update the Model for Langchain |
-->
