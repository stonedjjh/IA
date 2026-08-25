from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")

# sAutoTokenizer para la tokenización
# AutoModelForCausalLM para cargar un modelo de lenguaje causal
# torch para la inferencia del modelo
# warnings.filterwarnings("ignore") suprime mensajes de advertencia innecesarios de Hugging Face para mantener la salida más limpia.

model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"


print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.unk_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)


# pad_token: En los modelos de transformadores, las entradas en un lote a menudo deben tener la misma longitud. Las secuencias más cortas se rellenan con un token especial llamado el token de relleno (pad_token). Esto indica al modelo qué partes de la entrada son palabras reales y cuáles son relleno.
# device_map: Controla dónde se ejecuta el modelo (por ejemplo, CPU o GPU) y asegura que se cargue correctamente en el dispositivo disponible.
# torch_dtype: Establece la precisión numérica de los cálculos (por ejemplo, float32 o float16) para equilibrar velocidad, uso de memoria y precisión.

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Give short and concise answers in 2-3 lines."
    }
]

# messages: Este es el historial completo de la conversación entre el usuario y la IA. Cada mensaje tiene dos partes: role quién está hablando y content lo que están diciendo

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

    # apply_chat_template(): Esta función convierte el formato de mensaje estructurado (sistema, usuario, asistente) en un solo aviso correctamente formateado que el modelo puede entender. Asegura que la conversación siga el formato esperado por el modelo, incluyendo tokens especiales y estructura.
    # tokenize: convierte texto en tokens
    # add_generation_prompts: indica al modelo que genere una respuesta. Esta bandera le dice al modelo que la entrada termina aquí y que ahora debe comenzar a generar una respuesta. Asegura que el modelo sepa dónde debe comenzar la respuesta del asistente en el formato de conversación.
    # return_tensors: devuelve tensores de PyTorch

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
  # with torch.inference_mode(): Ejecuta el código en modo de inferencia (sin entrenamiento). Hace que la generación sea más rápida y eficiente en memoria.
  # 
  # model.generate(): Esta es la función que realmente hace que el modelo produzca una respuesta basada en los tokens de entrada.
  # 
  # tokenized["input_ids"]: Estos son los tokens numéricos que representan tu texto de entrada. El modelo los utiliza como punto de partida para generar la salida.
  # 
  # attention_mask=tokenized["attention_mask"]: Esto le indica al modelo qué tokens son palabras reales y cuáles son relleno. Asegura que el modelo ignore los tokens de relleno durante la generación.
  # 
  # pad_token_id=tokenizer.pad_token_id: Especifica el ID del token de relleno para que el modelo sepa cómo manejar el relleno durante la generación, evitando errores o advertencias.  
  response = tokenizer.decode(
      outputs[0][tokenized["input_ids"].shape[-1]:],
      skip_special_tokens=True
  )

  # outputs[0][tokenized["input_ids"].shape[-1]:] Esta parte extrae solo la respuesta recién generada del modelo.
  # 
  # outputs[0] : secuencia completa (entrada + texto generado)
  # 
  # tokenized["input_ids"].shape[-1] : longitud de la entrada original
  # 
  # **[...] **: corta solo la parte generada (elimina la entrada)
  # 
  # Así que el modelo no repite la pregunta del usuario en la salida.  

  print(f"Bot: {response}\n")  

  messages.append({"role": "assistant", "content": response})   
  