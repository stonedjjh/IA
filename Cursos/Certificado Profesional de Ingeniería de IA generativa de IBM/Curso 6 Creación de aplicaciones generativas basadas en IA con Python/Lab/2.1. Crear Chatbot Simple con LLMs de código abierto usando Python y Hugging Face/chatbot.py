from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# AutoTokenizer : convierte texto en tokens que el modelo entiende

# AutoModelForSeq2SeqLM : carga un modelo de generación de secuencia a secuencia para diálogos

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for subsequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

print("Chatbot ready! (type 'exit' to quit)\n")

history_string = "\n".join(conversation_history)

input_text = input("> ")

prompt = history_string + f"\nUser: {input_text}\nBot:"

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

# tokenizer(...): Convierte texto en bruto en tokens numéricos que el modelo puede entender.
# history_string: Historial de conversación anterior utilizado para proporcionar contexto.
# input_text: Mensaje actual del usuario.
# return_tensors="pt": Devuelve tensores de PyTorch (requeridos por el modelo).
# truncation=True: Trunca la entrada si excede los límites del modelo.
# max_length=512: Número máximo de tokens permitidos como entrada.


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

# inputs: Envía el mensaje del usuario y el historial del chat al modelo. Esto ayuda al chatbot a entender la conversación completa antes de responder.
# max_new_tokens: Establece la longitud máxima de la respuesta. Evita que el modelo escriba demasiado texto.
# no_repeat_ngram_size: Impide que el modelo repita las mismas frases de 3 palabras una y otra vez.
# repetition_penalty: Reduce las palabras repetidas en la respuesta para que la salida suene más natural.
# do_sample=True: Hace que las respuestas del chatbot sean más aleatorias y menos fijas, por lo que las respuestas se sienten más naturales.
# temperature: Controla cuán creativa es la respuesta. Menor = respuestas más seguras, mayor = respuestas más creativas.
# top_p: Mantiene solo las elecciones de palabras más probables al generar texto, lo que ayuda a que la respuesta sea clara y significativa.

response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print(response)

# tokenizer.decode(outputs[0]): Convierte la salida del modelo de números (tokens) de nuevo a texto legible. El modelo primero genera números, y este paso los transforma en una oración comprensible para humanos.
# outputs[0]: Toma la primera respuesta generada por el modelo (ya que el modelo puede generar múltiples salidas internamente).
# skip_special_tokens=True: Elimina tokens especiales como relleno o símbolos del sistema para que no aparezcan en la salida final.
# .strip(): Elimina espacios extra al principio y al final del texto para una salida limpia.
# print(response): Muestra la respuesta final del chatbot en la terminal para que el usuario pueda verla.

conversation_history.append(f"User: {input_text}")
conversation_history.append(f"Bot: {response}")
print(conversation_history)

# keep only last few exchanges (prevents confusion)
conversation_history = conversation_history[-6:]

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

  
