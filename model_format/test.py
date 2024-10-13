import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer

# Load the tokenizer
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare the input question (your text input)
question = "What is the weather like today?"

# Tokenize the input question
inputs = tokenizer(question, return_tensors="np", truncation=True, padding='max_length', max_length=528)

# Path to your ONNX model file
onnx_model_path = "/Users/poomcryptoman/codingZone/buildSomething/Ndid-icp/model_format/qwen2_5_1_5B_instruct.onnx"

# Load the ONNX model
session = ort.InferenceSession(onnx_model_path)

# Inspect the model inputs and outputs (if needed)
print("Model inputs:")
for input_metadata in session.get_inputs():
    print(f"Input name: {input_metadata.name}, shape: {input_metadata.shape}, type: {input_metadata.type}")

print("Model outputs:")
for output_metadata in session.get_outputs():
    print(f"Output name: {output_metadata.name}, shape: {output_metadata.shape}, type: {output_metadata.type}")

# Prepare the inputs
input_ids = inputs["input_ids"]
attention_mask = inputs["attention_mask"]

# Ensure that input_ids and attention_mask are padded to the correct length (528 tokens)
input_ids_padded = np.pad(input_ids, ((0, 0), (0, 528 - input_ids.shape[1])), 'constant', constant_values=0)
attention_mask_padded = np.pad(attention_mask, ((0, 0), (0, 528 - attention_mask.shape[1])), 'constant', constant_values=0)

# Get the correct input names from the ONNX model (if not already known)
input_name = session.get_inputs()[0].name  # Example: 'input_ids'
attention_name = session.get_inputs()[1].name  # Example: 'attention_mask'

# Run the ONNX model (passing tokenized input with padded sequences)
outputs = session.run(None, {input_name: input_ids_padded, attention_name: attention_mask_padded})

# Process the output (convert back to text using the tokenizer)
predicted_token_ids = np.argmax(outputs[0], axis=-1)

# Decode the predicted token IDs into text
generated_text = tokenizer.decode(predicted_token_ids[0], skip_special_tokens=True)

# Print the generated text
print("Generated Text:", generated_text)