from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "gpt2" 


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Sample input
prompt = "Describe a Bicycle"

def get_output(prompt):

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=500, do_sample=True, temperature=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return generated_text

# print(get_output(prompt))


