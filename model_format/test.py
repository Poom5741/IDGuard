import onnx

# Load and validate the ONNX model
onnx_model = onnx.load("./qwen2_5_1_5B_instruct.onnx")
onnx.checker.check_model(onnx_model)
print("ONNX model is valid.")