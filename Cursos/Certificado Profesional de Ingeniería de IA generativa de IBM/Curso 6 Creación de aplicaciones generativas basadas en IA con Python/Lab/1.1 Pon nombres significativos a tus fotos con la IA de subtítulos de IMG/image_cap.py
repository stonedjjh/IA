import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model

'''
AutoProcessor : Esta es una clase de procesador que se utiliza para el preprocesamiento de datos 
para el modelo BLIP. Envuelve un procesador de imágenes BLIP y un tokenizador OPT/T5 en un solo 
procesador. Esto significa que puede manejar tanto datos de imagen como de texto, preparándolos 
para la entrada en el modelo BLIP.
'''
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

'''
BlipForConditionalGeneration : Esta es una clase de modelo que se utiliza para la generación de 
texto condicional dado una imagen y un texto opcional. En otras palabras, puede generar texto 
basado en una imagen de entrada y una pieza de texto opcional. Esto lo hace útil para tareas como 
la generación de descripciones de imágenes o la respuesta a preguntas visuales, donde el modelo 
necesita generar texto que describa una imagen o responda a una pregunta sobre una imagen.
'''
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image, DON'T FORGET TO WRITE YOUR IMAGE NAME
img_path = "american wirehair.jpg"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')

'''
A continuación, la imagen preprocesada se pasa por el procesador para generar entradas en el formato 
requerido. El argumento return_tensors se establece en "pt" para devolver tensores de PyTorch.
'''

# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)


'''
Finalmente, la salida generada es una secuencia de tokens. Para transformar estos tokens en texto legible 
por humanos, utilizas el método decode proporcionado por el procesador. El argumento skip_special_tokens 
se establece en True para ignorar los tokens especiales en el texto de salida.
'''

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)
