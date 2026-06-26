# BLIP


BLIP, cuyo nombre significa Bootstrapping Language-Image Pre-training(Preentrenamiento de Lenguaje-Imágen por Bootstrap), es un modelo de IA que destaca por su capacidad para entender tanto texto como imágenes.

BLIP representa un avance significativo en la intersección del procesamiento del lenguaje natural (NLP) y la visión por computadora. BLIP, diseñado para mejorar los modelos de IA, potencia su capacidad para entender y generar descripciones de imágenes. Aprende a asociar imágenes con texto relevante, lo que le permite generar subtítulos, responder preguntas relacionadas con imágenes y apoyar consultas de búsqueda basadas en imágenes.

## Hugging Face Transformers

Es una popular biblioteca de código abierto que proporciona modelos y herramientas de procesamiento de lenguaje natural (NLP) de última generación.

### Características 

- **Soporte para el aprendizaje multimodal:** aprovecha tanto los datos de texto como los de imagen para mejorar la comprensión y generación de descripciones de imágenes por parte de los modelos de IA.

- **Comprensión mejorada:** Proporciona una comprensión más matizada del contenido dentro de las imágenes, yendo más allá del reconocimiento de objetos para comprender escenas, acciones e interacciones.

- **Aprendizaje multimodal:** Al integrar datos de texto e imagen, BLIP facilita el aprendizaje multimodal, que se asemeja más a cómo los humanos perciben el mundo.

- **Accesibilidad:** Generar descripciones precisas de imágenes puede hacer que el contenido sea más accesible para personas con discapacidades visuales.

- **Creación de contenido:** Apoya esfuerzos creativos y de marketing al generar textos descriptivos para contenido visual, ahorrando tiempo y mejorando la creatividad.

### Comenzando con BLIP en Hugging Face

Hugging Face ofrece una plataforma para experimentar con BLIP y otros modelos de IA. A continuación se muestra un ejemplo de cómo usar BLIP para la generación de subtítulos de imágenes en Python.

Asegúrate de tener Python y la biblioteca Transformers instalados. Si no, puedes instalar la biblioteca transformers usando pip. Consulta el siguiente código.

> [!NOTE] En el próximo laboratorio, “Laboratorio: Asigna Nombres Significativos a Tus Fotos con IA de Subtitulación de Imágenes,” podrás practicar el concepto de BLIP para la generación de subtítulos de imágenes.

```Python
# Install the transformers library
!pip install transformers Pillow torch torchvision torchaudio
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
# Initialize the processor and model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
# Load an image
image = Image.open("path_to_your_image.jpg")
# Prepare the image
inputs = processor(image, return_tensors="pt")
# Generate captions
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0],skip_special_tokens=True)
 
print("Generated Caption:", caption)
```

> [!NOTE]
> En el ejemplo anterior, reemplaza "path_to_your_image.jpg" con la ruta a tu archivo de imagen.

### Respuesta a Preguntas Visuales

BLIP también puede responder preguntas sobre el contenido de una imagen. Consulta el siguiente código.

```PYTHON
# Install required libraries
!pip install transformers Pillow torch torchvision torchaudio
# Import required modules
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
# Load BLIP processor and model (large version for better understanding + VQA)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
# Load image from URL
img_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")
# Define question about the image
question = "What is in the image?"
# Prepare both image + question as input
inputs = processor(image, question, return_tensors="pt")
# Generate answer
outputs = model.generate(**inputs)
# Decode output into readable text
answer = processor.decode(outputs[0], skip_special_tokens=True)
# Print final answer
print("Answer:", answer)
```
