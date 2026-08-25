::page{title="Crear un chatbot simple con LLMs de código abierto usando Python y Hugging Face"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-WD0231EN-SkillsNetwork/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo"  />

En este laboratorio, ¡crearás un chatbot muy simple pero funcional!  
<center> 

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04ESEN/images/1.jpeg" width="500" alt="chatbot">

</center>

## Resultados de aprendizaje:

Al final de este laboratorio, serás capaz de:

- Describir los componentes principales de un chatbot
- Explicar qué es un LLM
- Seleccionar un LLM para tu aplicación
- Describir cómo funciona esencialmente un transformer
- Introducir datos en un transformer (tokenización)
- Programar tu propio chatbot simple en Python

## Introducción: Detrás de un chatbot

### Introducción: ¿Cómo funciona un chatbot?

Un chatbot es un programa de computadora que toma una entrada de texto y devuelve una salida de texto correspondiente.

Los chatbots utilizan un tipo especial de programa de computadora llamado transformer, que es como su cerebro. Dentro de este sistema hay un modelo de lenguaje (LLM), que es el componente central que genera respuestas. Esto ayuda al chatbot a entender y generar respuestas similares a las humanas. Descifra muchos ejemplos de conversaciones humanas que ha visto antes de responder de manera sensata.

Los transformers y los LLM trabajan juntos dentro de un chatbot para habilitar la conversación. Aquí hay una explicación simplificada de cómo interactúan:

- **Procesamiento de entrada:** Cuando envías un mensaje al chatbot, el transformer ayuda a procesar tu entrada. Descompone tu mensaje en partes más pequeñas y las representa de una manera que el chatbot puede entender. Cada parte se llama un token.

- **Comprensión del contexto:** El transformer pasa estos tokens al LLM, que es un modelo de lenguaje entrenado con muchos datos de texto. El LLM ha aprendido patrones y significados de estos datos, por lo que intenta entender el contexto de tu mensaje basado en lo que ha aprendido.

- **Generación de respuesta:** Una vez que el LLM entiende tu mensaje, genera una respuesta basada en su comprensión. Luego, el transformer toma esta respuesta y la convierte en un formato que puede ser fácilmente enviado de vuelta a ti.

- **Conversación iterativa:** A medida que la conversación continúa, este proceso se repite. El transformer y el LLM trabajan juntos para procesar cada nuevo mensaje de entrada, entender el contexto y generar una respuesta relevante.

La clave es que el LLM aprende de una gran cantidad de datos de texto para entender los patrones del lenguaje y generar respuestas significativas. El transformer ayuda con los aspectos técnicos del procesamiento y representación de los datos de entrada/salida, permitiendo que el LLM se concentre en entender y generar lenguaje.

Una vez que el chatbot entiende tu mensaje, utiliza el modelo de lenguaje para generar una respuesta que cree que será útil o interesante para ti. La respuesta se envía de vuelta a ti, y el proceso continúa mientras mantienes una conversación de ida y vuelta con el chatbot.

### Introducción: Hugging Face

Hugging Face es una organización que se centra en el procesamiento de lenguaje natural (NLP) y la IA. Proporcionan una variedad de herramientas, recursos y servicios para apoyar tareas de NLP.

Utilizarás su biblioteca de Python `transformers` en este proyecto.

¡Bien! Ahora que sabes cómo funciona un chatbot a un alto nivel, ¡comencemos a implementar un chatbot simple!

## Paso 1: Instalación de requisitos

Sigue estos pasos para crear un entorno virtual de Python e instalar las bibliotecas necesarias. Primero, abre una nueva terminal.
Configura tu entorno virtual:

```bash
pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env
```


Para este ejemplo, utilizamos la biblioteca transformers, un conjunto de herramientas de NLP de código abierto, junto con PyTorch (torch) para el aprendizaje profundo, mientras que accelerate ayuda a ejecutar modelos de IA de manera eficiente en CPU/GPU y numpy soporta cálculos numéricos y de arreglos rápidos en Python.

Fijamos las versiones de las bibliotecas para garantizar que el código se ejecute de manera consistente sin romperse debido a actualizaciones futuras o cambios en las dependencias.

```bash
pip install transformers==4.41.2 torch==2.2.2 accelerate==0.30.1 numpy==1.26.4
```


Espera unos minutos para instalar los paquetes.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0331EN-SkillsNetwork/DALL%C2%B7E%202024-01-03%2014.23.28%20-%20An%20ASCII%20art%20representation%20of%20a%20cup%20of%20coffee.%20The%20image%20should%20depict%20a%20steaming%20cup%20of%20coffee%2C%20composed%20entirely%20of%20ASCII%20characters.%20The%20ASCII%20art.png" width="300" alt="chatbot">

Para crear un nuevo archivo de Python, haz clic en `File Explorer`, luego haz clic derecho en el área del explorador y selecciona `New File`. Nombra este nuevo archivo `chatbot.py`.

::openFile{path="chatbot.py"}

<center> 

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0331EN-SkillsNetwork/images/create_new_file.jpg" width="800" alt="chatbot">

</center>

::page{title="Parte 1: Construyendo un Chatbot Simple Usando Modelos Transformer"}

## Paso 2: Importar nuestras herramientas necesarias de la biblioteca transformers

Para este ejemplo, utilizarás `AutoTokenizer` y `AutoModelForSeq2SeqLM` de la biblioteca `transformers`. 

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
```


**AutoTokenizer** : convierte texto en tokens que el modelo entiende

**AutoModelForSeq2SeqLM** : carga un modelo de generación de secuencia a secuencia para diálogos

Agrega el paso en el archivo `chatbot.py`.

## Paso 3: Elegir un modelo

Elegir el modelo adecuado para tus propósitos es una parte importante de la construcción de chatbots. Puedes leer sobre los diferentes tipos de modelos disponibles en el sitio web de Hugging Face: https://huggingface.co/models.

Los modelos difieren en arquitectura (codificador, decodificador o codificador-decodificador), métodos de entrenamiento (preentrenamiento, ajuste fino, ajuste por instrucciones) y capacidades. Veamos algunos ejemplos para ver cómo diferentes modelos se adaptan mejor a varios contextos.

- **Generación de texto**:
   La generación de texto y los chatbots han evolucionado con el tiempo, utilizando diferentes tipos de modelos según la complejidad y el caso de uso. Los sistemas anteriores utilizaban modelos de codificador-decodificador basados en transformadores (Seq2Seq) como facebook/blenderbot-400M-distill, así como modelos como T5 y BART. Estos son ligeros, de código abierto y pueden ejecutarse en CPUs, lo que los hace adecuados para chatbots simples y entornos de aprendizaje.

  Sin embargo, los chatbots modernos se construyen utilizando modelos de lenguaje grandes (LLMs) que utilizan arquitecturas de transformadores solo de decodificador y están entrenados en conjuntos de datos muy grandes. Ejemplos incluyen modelos estilo GPT, LLaMA y sistemas Mistral. Estos modelos son mucho más poderosos en razonamiento y conversación, pero requieren más recursos informáticos o acceso a API. Ambos enfoques utilizan transformadores, pero difieren en escala, métodos de entrenamiento y capacidad.

    Ejemplo: Quieres construir un chatbot que genere respuestas creativas y coherentes a la entrada del usuario.

- **Análisis de sentimiento**:
    Para tareas de análisis de sentimiento, modelos como BERT o RoBERTa son opciones populares. Están entrenados para entender el sentimiento y el tono emocional del texto.

  
    Ejemplo: Quieres analizar la retroalimentación de los clientes y determinar si es positiva o negativa.

- **Reconocimiento de entidades nombradas**:
    Modelos como BERT o RoBERTa (ajustados para clasificación de tokens) se utilizan comúnmente para tareas de Reconocimiento de Entidades Nombradas (NER). Tienen un buen rendimiento en la comprensión y extracción de entidades como nombres de personas, ubicaciones, organizaciones, etc.

  
    Ejemplo: Quieres construir un sistema que extraiga nombres de personas y lugares de un texto dado.

- **Respuesta a preguntas**:
    Modelos como BERT (ajustados para QA) o LLMs modernos ajustados por instrucciones (por ejemplo, GPT-4–class, LLaMA, Mistral) pueden ser efectivos para tareas de respuesta a preguntas. Pueden comprender preguntas y proporcionar respuestas precisas basadas en el contexto dado.

  
    Ejemplo: Quieres construir un chatbot que pueda responder preguntas fácticas a partir de un conjunto de documentos dado.

- **Traducción de idiomas**:
    Para tareas de traducción de idiomas, considera modelos como MarianMT, T5 o modelos multilingües y ajustados por instrucciones más nuevos como mT5, NLLB o LLMs modernos. Están diseñados específicamente para traducir texto entre diferentes idiomas.

  
    Ejemplo: Quieres construir una herramienta de traducción de idiomas que traduzca texto en inglés a francés.

Sin embargo, estos ejemplos son muy limitados y la idoneidad de un LLM puede depender de muchos factores como la disponibilidad de datos, los requisitos de rendimiento, las limitaciones de recursos y consideraciones específicas del dominio. Es importante explorar diferentes LLMs a fondo y experimentar con ellos para encontrar la mejor opción para tu aplicación específica.

Otros propósitos importantes que deben tenerse en cuenta al elegir un LLM incluyen (pero no se limitan a):
- Licencias: Asegúrate de que se te permita utilizar tu modelo elegido de la manera que pretendes
- Tamaño del modelo: Los modelos más grandes pueden ser más precisos, pero también pueden requerir más recursos
- Datos de entrenamiento: Asegúrate de que los datos de entrenamiento del modelo se alineen con el dominio o contexto para el que pretendes utilizar el LLM
- Rendimiento y precisión: Considera factores como la precisión, el tiempo de ejecución o cualquier otra métrica que sea importante para tu caso de uso específico

Para explorar todas las diferentes opciones, consulta los [modelos disponibles en el sitio web de Hugging Face](https://huggingface.co/models?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkGuidedProjectsIBMSkillsNetworkGPXX04ESEN3232-2023-01-01).

Para este ejemplo, utilizarás `facebook/blenderbot-400M-distill`. Este modelo se selecciona porque:

Es de código abierto  
Está optimizado para diálogos  
Es ligero y se ejecuta de manera eficiente en la CPU  

```
model_name = "facebook/blenderbot-400M-distill"
```


Agrega este paso a tu archivo `chatbot.py` de Python.

## Paso 4: Obtener el modelo e inicializar un tokenizador

Al ejecutar este código por primera vez, la máquina anfitriona descargará el modelo de la API de Hugging Face. Sin embargo, después de ejecutar el código una vez, el script no volverá a descargar el modelo y, en su lugar, hará referencia a la instalación local.

Estarás observando dos términos aquí: `model` y `tokenizer`.

En este script, inicias variables utilizando dos clases útiles de la biblioteca `transformers`:
- `model` es una instancia de la clase `AutoModelForSeq2SeqLM`, que te permite interactuar con tu modelo de lenguaje elegido.
- `tokenizer` es una instancia de la clase `AutoTokenizer`, que optimiza tu entrada y la pasa al modelo de lenguaje de manera eficiente. Lo hace convirtiendo tu entrada de texto en "tokens", que es cómo el modelo interpreta el texto.

```
# Load model (download on first run and reference local installation for subsequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```


::page{title="Detalles de la conversación"}

## Paso 5: Chat

Ahora que estás listo, ¡comencemos a chatear!

Hay varias cosas que harás para tener una conversación efectiva con tu chatbot.

Antes de interactuar con tu modelo, necesitas inicializar un objeto donde puedas almacenar el historial de la conversación.
1. Inicializa un objeto para almacenar el historial de la conversación

Después, harás lo siguiente para cada interacción con el modelo:

2. Codifica el historial de la conversación como una cadena
3. Obtén el aviso del usuario
4. Tokeniza (optimiza) el aviso
5. Genera la salida del modelo usando el aviso y el historial
6. Decodifica la salida
7. Actualiza el historial de la conversación

### Paso 5.1: Mantener un registro del historial de la conversación

El historial de la conversación es importante al interactuar con un chatbot porque el chatbot también hará referencia a las conversaciones anteriores al generar la salida.

Para tu implementación simple en Python, puedes usar una lista. Según la implementación de Hugging Face, utilizarás esta lista para almacenar el historial de la conversación de la siguiente manera:

>conversation_history
>
> conversation_history [Usuario: input_1, Bot: output_1, Usuario: input_2, Bot: output_2, ...] 

Inicialicemos esta lista antes de que ocurran conversaciones.

```
conversation_history = []

```


Imprimamos un mensaje simple que te ayudará a salir del chatbot una vez que todo el código esté listo:

```
print("Chatbot ready! (type 'exit' to quit)\n")

```


Agrega este paso a tu código Python en chatbot.py

### Paso 5.2: Codificando el historial de la conversación

Durante cada interacción, pasarás tu historial de conversación al modelo junto con tu entrada para que también pueda referirse a la conversación anterior al generar la siguiente respuesta.

La función de la biblioteca `transformers` que estás utilizando espera recibir el historial de conversación como una cadena, con cada elemento separado por el carácter de nueva línea `'\n'`. Así, crearás tal cadena.

Usarás el método `join()` en Python para hacer exactamente eso. (Inicialmente, tu history_string será una cadena vacía, lo cual está bien, y crecerá a medida que avanza la conversación).

```python
history_string = "\n".join(conversation_history)
```


Agrega esto a `chatbot.py`

### Paso 5.3: Obtener el mensaje del usuario

Antes de comenzar a construir un chatbot simple en la terminal, veamos un ejemplo de la entrada:

```python
input_text = input("> ")
```


Agrega esto a `chatbot.py`

### Paso 5.4: Tokenización del mensaje del usuario y del historial de chat

Los tokens en PLN son unidades o elementos individuales en los que se divide el texto o las oraciones. La tokenización o vectorización es el proceso de convertir los tokens en representaciones numéricas. La tokenización convierte el texto en un formato numérico que el modelo puede entender.

En esta implementación, pasamos tanto el historial como la nueva entrada juntos como una única entrada. Esta línea crea un único mensaje al combinar el historial de la conversación con la última entrada del usuario. El formato `User: ...` y `Bot:` separa claramente los roles y señala al modelo que genere la siguiente respuesta del bot. El `Bot:` final ayuda al modelo a continuar el texto en el estilo del asistente.

```
prompt = history_string + f"\nUser: {input_text}\nBot:"

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)
```


- t**okenizer(...):** Convierte texto en bruto en tokens numéricos que el modelo puede entender.
- **history_string:** Historial de conversación anterior utilizado para proporcionar contexto.
- **input_text:** Mensaje actual del usuario.
- **return_tensors="pt":** Devuelve tensores de PyTorch (requeridos por el modelo).
- **truncation=True:** Trunca la entrada si excede los límites del modelo.
- **max_length=512:** Número máximo de tokens permitidos como entrada.

Agrega esto a `chatbot.py` y ejecútalo:

```
python3 chatbot.py
```


Al hacerlo, ahora has creado un objeto similar a un diccionario de tensores tokenizados que contiene palabras clave especiales que permiten al modelo hacer referencia a su contenido correctamente.

### Paso 5.5: Generar salida del modelo

Ahora que tienes tus entradas listas, tanto las pasadas como las presentes, puedes pasarlas al modelo y generar una respuesta. Según la documentación, puedes usar la función `generate()` y pasar las entradas como argumentos de palabra clave ([kwargs](https://www.freecodecamp.org/news/args-and-kwargs-in-python/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkGuidedProjectsIBMSkillsNetworkGPXX04ESEN3232-2023-01-01)).

```
outputs = model.generate(
    **inputs,
    max_new_tokens=60,
    no_repeat_ngram_size=3,
    repetition_penalty=1.3,
    do_sample=True,
    temperature=0.6,
    top_p=0.85
)
## Remove this print statement after testing
print(outputs)
```


- **inputs**: Envía el mensaje del usuario y el historial del chat al modelo. Esto ayuda al chatbot a entender la conversación completa antes de responder.
- **max_new_tokens**: Establece la longitud máxima de la respuesta. Evita que el modelo escriba demasiado texto.
- **no_repeat_ngram_size**: Impide que el modelo repita las mismas frases de 3 palabras una y otra vez.
- **repetition_penalty**: Reduce las palabras repetidas en la respuesta para que la salida suene más natural.
- **do_sample=True**: Hace que las respuestas del chatbot sean más aleatorias y menos fijas, por lo que las respuestas se sienten más naturales.
- **temperature**: Controla cuán creativa es la respuesta. Menor = respuestas más seguras, mayor = respuestas más creativas.
- **top_p**: Mantiene solo las elecciones de palabras más probables al generar texto, lo que ayuda a que la respuesta sea clara y significativa.

Agrega esto a `chatbot.py` y ejecútalo:

Inicia la conversación preguntando `Hola, ¿cómo estás?`

```bash
python3 chatbot.py
```


La salida:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nWQnI1Tztp60zce3jigGfA/Screenshot%202026-05-07%20092420.png" width="1000" />

Genial, ¡ahora tienes tus salidas! Sin embargo, la salida contiene IDs de tokens (valores de tensor), no texto legible.

Por lo tanto, solo necesitas decodificar el primer índice de `outputs` para ver la respuesta en texto plano.

### Paso 5.6: Decodificar salida

Puedes decodificar la salida usando `tokenizer.decode()`. Esto se conoce como "detokenización" o "reconstrucción". Es el proceso de combinar o fusionar tokens individuales de nuevo en su forma original, para reconstruir el texto o la oración original.

```
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print(response)
```


- **tokenizer.decode(outputs[0])**: Convierte la salida del modelo de números (tokens) de nuevo a texto legible. El modelo primero genera números, y este paso los transforma en una oración comprensible para humanos.
- **outputs[0]**: Toma la primera respuesta generada por el modelo (ya que el modelo puede generar múltiples salidas internamente).
- **skip_special_tokens=True**: Elimina tokens especiales como relleno o símbolos del sistema para que no aparezcan en la salida final.
- **.strip()**: Elimina espacios extra al principio y al final del texto para una salida limpia.
- **print(response)**: Muestra la respuesta final del chatbot en la terminal para que el usuario pueda verla.

Agrega esto a `chatbot.py` y ejecútalo:

Inicia la conversación preguntando `Hola, ¿cómo estás?`

```bash
python3 chatbot.py
```


La salida:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/sYoDm5UBBvi8v506dMrZXQ/response.png" width="1000" />

¡Bien hecho! ¡Has tenido con éxito una interacción con tu chatbot! Le has dado un aviso y has recibido su respuesta.

Ahora, lo único que queda por hacer es actualizar tu historial de conversación, para que puedas pasarlo con la próxima iteración.

### Paso 5.7: Actualizar el historial de conversación

Todo lo que necesitas hacer aquí es agregar tanto la entrada como la respuesta a `conversation_history` en texto plano.

```python
conversation_history.append(f"User: {input_text}")
conversation_history.append(f"Bot: {response}")
print(conversation_history)
```


Agrega esto a `chatbot.py` y ejecútalo:

Comienza la conversación preguntando `Hola, ¿cómo estás?`

```bash
python3 chatbot.py
```


La salida

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/qzsdTAw76VIbJ7YU0s6EQA/Screenshot%202026-05-07%20092702.png" width="1000" />

# Paso 6: Repetir

Has pasado por todos los pasos de interacción con tu chatbot. ¡Ahora puedes poner todo en un bucle y llevar a cabo toda una conversación!

Lo hemos mejorado aún más al agregar

```python
    # keep only last few exchanges (prevents confusion)
    conversation_history = conversation_history[-6:]
```


porque el modelo solo puede manejar una cantidad limitada de texto a la vez. En una conversación larga, los mensajes antiguos no siempre son útiles para generar la siguiente respuesta e incluso pueden confundir al modelo o diluir el contexto. 
Al mantener solo los últimos intercambios:
- El chatbot se centra en la parte más reciente y relevante de la conversación
- Evita sentirse abrumado por un historial de chat largo
- Reduce la repetición y mejora la calidad de la respuesta
- Mantiene la entrada dentro del límite de tokens del modelo

Ahora, necesitamos agregar todo en un bucle para que la conversación siga fluyendo.

```python

while True:
    # keep only last few exchanges (prevents confusion)
    conversation_history = conversation_history[-6:]
    
    history_string = "\n".join(conversation_history)

    input_text = input("> ")
## This will help you exit by typing exit in the prompt 
    if input_text.lower() == "exit":
        break

    prompt = history_string + f"\nUser: {input_text}\nBot:"

    inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        no_repeat_ngram_size=3,
        repetition_penalty=1.3,
        do_sample=True,
        temperature=0.6,
        top_p=0.85
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print("Bot:", response)

    conversation_history.append(f"User: {input_text}")
    conversation_history.append(f"Bot: {response}")

  
```


Agrega esto a `chatbot.py` y ejecútalo:

Comienza la conversación preguntando `Hola, ¿cómo estás?`

```bash
python3 chatbot.py
```


> **Nota:** El modelo utilizado en este proyecto es una versión básica y ligera, no destinada a manejar consultas complejas y puede producir respuestas genéricas o inconsistentes durante conversaciones prolongadas. Para modelos de lenguaje más avanzados y robustos, puedes explorar una amplia gama de opciones en huggingface.com.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/yguWib-7HtDfKKBuerTWBw/finalOutput.png" width="1000" />

Esta será la solución final:
<details>
  
  <summary>Haz clic para expandir</summary>
  


```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Chatbot ready! (type 'exit' to quit)\n")
conversation_history = []

while True:
    # Keep only recent conversation
    conversation_history = conversation_history[-6:]
    history_string = "\n".join(conversation_history)

    input_text = input("> ")

    if input_text.lower() == "exit":
        break

        
    prompt = history_string + f"\nUser: {input_text}\nBot:"

    inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        no_repeat_ngram_size=3,
        repetition_penalty=1.3,
        do_sample=True,
        temperature=0.6,
        top_p=0.85
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    print("Bot:", response)

    # Save bot response
    conversation_history.append(f"User: {input_text}")
    conversation_history.append(f"Bot: {response}")
      
```


</details>

¡Voilà! Has construido un chatbot simple y funcional con el que puedes interactuar a través de tu terminal.

Presiona `cntrl + c` para salir de la conversación. O simplemente escribe `exit` en el aviso.

::page{title="Parte 2: Construyendo un Chatbot LLM Moderno con Plantillas de Chat"}

En la Parte 1, construiste un chatbot simple utilizando un modelo Seq2Seq. Creaste manualmente el texto de entrada, lo convertiste en tokens y almacenaste el historial de chat por tu cuenta. Esto te ayuda a entender el funcionamiento básico de un chatbot y cómo los transformadores generan respuestas.

En la Parte 2, utilizas un modelo de IA más moderno (un LLM causal). Aquí, no construyes manualmente los prompts. En su lugar, usas mensajes estructurados como “usuario” y “asistente”, y el modelo maneja el formato de la conversación por sí mismo.

## Paso 1: Importar bibliotecas necesarias

Al principio, comienza creando un nuevo archivo llamado `chatbot_llm.py`

Importa las bibliotecas necesarias

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")
```


Agrega este paso a `chatbot_llm.py`

**AutoTokenizer** para la tokenización

**AutoModelForCausalLM** para cargar un modelo de lenguaje causal

**torch** para la inferencia del modelo

**warnings.filterwarnings("ignore")** suprime mensajes de advertencia innecesarios de Hugging Face para mantener la salida más limpia.

## Paso 2: Elige un LLM moderno

Para este ejemplo, utilizarás:

```python
model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"
```


Agrega este paso a `chatbot_llm.py`

Este es un LLM causal ajustado para instrucciones ligero diseñado para tareas de conversación.

## Paso 3: Cargar modelo y tokenizador

```python
print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.unk_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)
```


Agrega este paso a `chatbot_llm.py`

- **pad_token**: En los modelos de transformadores, las entradas en un lote a menudo deben tener la misma longitud. Las secuencias más cortas se rellenan con un token especial llamado el token de relleno (pad_token). Esto indica al modelo qué partes de la entrada son palabras reales y cuáles son relleno.
- **device_map**: Controla dónde se ejecuta el modelo (por ejemplo, CPU o GPU) y asegura que se cargue correctamente en el dispositivo disponible.
- **torch_dtype**: Establece la precisión numérica de los cálculos (por ejemplo, float32 o float16) para equilibrar velocidad, uso de memoria y precisión.

## Paso 4: Inicializar mensajes de conversación

En los LLMs modernos basados en chat, usamos un formato de conversación estructurado compuesto de mensajes. Cada mensaje tiene un rol específico que indica al modelo quién está hablando y cómo comportarse.

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Give short and concise answers in 2-3 lines."
    }
]
```


Agrega este paso a `chatbot_llm.py`

**messages**: Este es el historial completo de la conversación entre el usuario y la IA. Cada mensaje tiene dos partes:
**role**  quién está hablando y **content**  lo que están diciendo

Hay tres tipos de **roles** en un sistema de IA basado en chat. El rol **system** define las reglas y el comportamiento de la IA, como cómo debería responder. El rol **user** representa las preguntas o entradas dadas por la persona que usa el chatbot. El rol **assistant** contiene las respuestas de la IA generadas en función de las instrucciones del sistema y la entrada del usuario, formando el flujo de la conversación.

## Paso 5: Iniciar bucle del chatbot

Agrega estos pasos a `chatbot_llm.py`

```python
print("Chatbot started. Type 'exit' to quit.\n")
while True:
  user_input = input("> ")

  if user_input.lower() == "exit":
      break

```


#### Paso 5.1: Actualizar el historial de conversación

Almacena el mensaje del usuario en el historial de conversación.

```python
  messages.append({"role": "user", "content": user_input})
```


Para evitar conversaciones muy largas, mantén solo los intercambios recientes:

```python
  messages = [messages[0]] + messages[-10:]
```


Esto mantiene:
- el mensaje del sistema
- el historial de conversación más reciente
  
#### Paso 5.2 : Aplicar plantilla de chat

Los modelos de chat modernos de Hugging Face utilizan plantillas de chat para formatear conversaciones automáticamente.

```python
  tokenized = tokenizer.apply_chat_template(
      messages,
      tokenize=True,
      add_generation_prompt=True,
      return_tensors="pt",
      return_dict=True,
      max_length=512
  )
```


- **apply_chat_template()**: Esta función convierte el formato de mensaje estructurado (sistema, usuario, asistente) en un solo aviso correctamente formateado que el modelo puede entender. Asegura que la conversación siga el formato esperado por el modelo, incluyendo tokens especiales y estructura.
- **tokenize**: convierte texto en tokens
- **add_generation_prompts**: indica al modelo que genere una respuesta. Esta bandera le dice al modelo que la entrada termina aquí y que ahora debe comenzar a generar una respuesta. Asegura que el modelo sepa dónde debe comenzar la respuesta del asistente en el formato de conversación.
- **return_tensors**: devuelve tensores de PyTorch

##### Paso 5.3: Generar respuesta

Este código se utiliza para generar una respuesta de un modelo de lenguaje basado en el texto de entrada dado. Toma tu entrada tokenizada y hace que el modelo prediga y genere una respuesta token por token, mientras controla el estilo, la longitud y la aleatoriedad de la salida.

```python
  with torch.inference_mode():
      outputs = model.generate(
          tokenized["input_ids"],
          attention_mask=tokenized["attention_mask"],
          max_new_tokens=60,
          temperature=0.5,
          top_p=0.8,
          do_sample=True,
          repetition_penalty=1.3,
          no_repeat_ngram_size=3,
          pad_token_id=tokenizer.pad_token_id
      )
```


- **with torch.inference_mode()**: Ejecuta el código en modo de inferencia (sin entrenamiento). Hace que la generación sea más rápida y eficiente en memoria.

- **model.generate()**: Esta es la función que realmente hace que el modelo produzca una respuesta basada en los tokens de entrada.

- **tokenized["input_ids"]**: Estos son los tokens numéricos que representan tu texto de entrada. El modelo los utiliza como punto de partida para generar la salida.

- **attention_mask=tokenized["attention_mask"]**: Esto le indica al modelo qué tokens son palabras reales y cuáles son relleno. Asegura que el modelo ignore los tokens de relleno durante la generación.

- **pad_token_id=tokenizer.pad_token_id**: Especifica el ID del token de relleno para que el modelo sepa cómo manejar el relleno durante la generación, evitando errores o advertencias.

#### Step 5.4: Decodificar y mostrar la respuesta

Después de que el modelo genera la salida, todavía está en forma de tokens (números). Este paso lo convierte de nuevo en texto legible y lo muestra al usuario.

```python

  response = tokenizer.decode(
      outputs[0][tokenized["input_ids"].shape[-1]:],
      skip_special_tokens=True
  )
  print(f"Bot: {response}\n")
```


**outputs[0][tokenized["input_ids"].shape[-1]:]**
Esta parte extrae solo la respuesta recién generada del modelo.

  - **outputs[0]** : secuencia completa (entrada + texto generado)
  
  - **tokenized["input_ids"].shape[-1]** : longitud de la entrada original
  
  - **[...] **: corta solo la parte generada (elimina la entrada)

    
 Así que el modelo no repite la pregunta del usuario en la salida.

#### Paso 5.5 : Guardar respuesta del asistente

```python
  messages.append({"role": "assistant", "content": response})

```


En caso de que te lo hayas perdido, añade el código del bucle while del paso 5 a `chatbot_llm.py`

<details>
  <summary>Haz clic para expandir</summary>
  


```python
print("Chatbot started. Type 'exit' to quit.\n")
while True:
  user_input = input("> ")

  if user_input.lower() == "exit":
      break

  messages.append({"role": "user", "content": user_input})

  messages = [messages[0]] + messages[-10:]

  tokenized = tokenizer.apply_chat_template(
      messages,
      tokenize=True,
      add_generation_prompt=True,
      return_tensors="pt",
      return_dict=True,
      max_length=512
  )

  with torch.inference_mode():
      outputs = model.generate(
          tokenized["input_ids"],
          attention_mask=tokenized["attention_mask"],
          max_new_tokens=60,
          temperature=0.5,
          top_p=0.8,
          do_sample=True,
          repetition_penalty=1.3,
          no_repeat_ngram_size=3,
          pad_token_id=tokenizer.pad_token_id
      )

  response = tokenizer.decode(
      outputs[0][tokenized["input_ids"].shape[-1]:],
      skip_special_tokens=True
  )

  print(f"Bot: {response}\n")

  messages.append({"role": "assistant", "content": response}) 

```


</details>
Ejecuta el laboratorio. Comienza la conversación preguntando `Hola, ¿cómo estás?`

```bash
python3 chatbot_llm.py
```


La salida:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/CuxTPA_EFYhqXXvCQd0fiw/Screenshot%202026-05-07%20175733.png" width="1000" />

Ahora has construido un chatbot moderno utilizando un LLM causal y plantillas de chat de Hugging Face. Este flujo de trabajo es similar a cómo se implementan muchos asistentes de IA modernos y sistemas conversacionales hoy en día.

Puedes experimentar con diferentes configuraciones para ver cómo cambia el comportamiento del bot. Esto es similar a cómo los sistemas de IA reales se ajustan para sentirse más amigables, creativos o estrictos dependiendo del caso de uso. 
Por ejemplo, puedes hacer que el bot sea más amigable cambiando el aviso del sistema:

```
messages = [{
    "role": "system",
    "content": "You are a very friendly and cheerful assistant. Always respond in a warm, casual, and encouraging tone."
}]
```


Entonces intenta cambiar los parámetros de generación para ver la diferencia en las respuestas:

```
temperature=0.9
top_p=0.95
```


Esta es la solución final para tu referencia:

<details>
  
  <summary>Haz clic para expandir</summary>

  ```python
  
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")

model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"

print("Cargando modelo...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.unk_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)

messages = [
    {
        "role": "system",
        "content": "Eres un asistente de IA útil. Da respuestas cortas y concisas en 2-3 líneas."
    }
]

print("Chatbot iniciado. Escribe 'exit' para salir.\n")
while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    messages = [messages[0]] + messages[-10:]

    tokenized = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
        max_length=512
    )

    with torch.inference_mode():
        outputs = model.generate(
            tokenized["input_ids"],
            attention_mask=tokenized["attention_mask"],
            max_new_tokens=60,
            temperature=0.5,
            top_p=0.8,
            do_sample=True,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.pad_token_id
        )

    response = tokenizer.decode(
        outputs[0][tokenized["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    print(f"Bot: {response}\n")

    messages.append({"role": "assistant", "content": response})
    
   ```
    
 </details>

::page{title="Conclusión"}

¡Felicidades, has completado con éxito este laboratorio!  
Este laboratorio muestra la creación de un chatbot básico utilizando Python y los modelos de lenguaje de código abierto de Hugging Face. El proyecto guía a los aprendices a través de los conceptos clave de los chatbots, incluyendo la comprensión y el uso de transformadores y tokenización. Proporciona un enfoque paso a paso para configurar el entorno, elegir un modelo y codificar un chatbot capaz de mantener una conversación. Este proyecto práctico, elaborado por el Dr. Sina Nazeri, es un gran recurso para principiantes interesados en explorar la IA y el desarrollo de chatbots, demostrando cómo construir un chatbot funcional de manera accesible y atractiva.

## Authors

**Vandana Pandey**  
 **[Sina Nazeri (Ph.D.)](https://www.linkedin.com/in/sina-nazeri)**

![Sina](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0Q8REN/images/sina_low_qual.jpeg)

 | Como científico de datos en IBM, siempre he estado apasionado por compartir mi conocimiento y ayudar a otros a aprender sobre el campo. Creo que todos deberían tener la oportunidad de aprender sobre ciencia de datos, independientemente de su origen o nivel de experiencia. Esta creencia me ha inspirado a convertirme en un proveedor de contenido educativo, creando y compartiendo materiales accesibles y atractivos para todos. |

## <h3 align="center"> &#169; IBM Corporation. Todos los derechos reservados. <h3/>