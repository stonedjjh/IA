from flask import Flask, render_template
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from flask import request


app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/bananas')
def bananas():
    return 'This page has bananas!'
	
@app.route('/bread')
def bread():
    return 'This page has bread!'


@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    input_text = data["prompt"]

    # Keep only recent conversation
    conversation_history[:] = conversation_history[-6:]

    # Create conversation history string
    history = "\n".join(conversation_history)
    prompt = history + f"\nUser: {input_text}\nBot:"

    # Tokenize input
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

    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Save conversation
    conversation_history.append(f"User: {input_text}")
    conversation_history.append(f"Bot: {response}")

    return response



if __name__ == '__main__':
    app.run()
