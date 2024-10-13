import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare dummy input
input_text = """this data is ocr data from thai id card can you try to order data in the right way to make it correct and readable pls :
Extracted Text (English):
i ot
L4/ UnsuszdnirUseyryy Thai National ID Card

avdsEiilssvy 01234 56789101
Identification Number

= dotuardomna ww wiltiow nowin

= Name Mr. Meenoy wo wo

= EEE LastName ~~ Koyruk is he mill

= Goduil  14un2523 EE =

= Date of Birth 14Jan 1980 1 -

= fog 2300 alas 0dadu d.4. 20007

= 2un2ses 110.2573

EEE ow EE

= Ducoflssue in $5 Date of Expiry

Extracted Text (Thai):
                                                                            -
6 บัตรประจําตัวประชาชน 7โล217ง๑๓๐กล1 110 ละ๕

เลขประจําตัวประชาชน        0 1284 56789 10 1
.ไส๕๓น์มิอลพ์อท โงนทกไว๕

2 จื่อตัวและชื่อสกุล นาย หมีน้อย คอยรัก

=                         1งลกา๐              ไห. ไหโอ๕๓อ            ๐-                   0

=     ฮ         : เณ อ ยลง

=             เกิดวันที่ 714 ม.ค. 2523        - จ

=                โวลเ๑๐รไฝ๓ 14 ]ล๓ 1980.               ๊%

=- ที่อยู่2300 คาโลรามา วอชิงตัน ดี.ซี. 20007

5 2มค256                                         1ม.ค.2573

ธิ น ไรก

” โณ๒๐ไน๒๐ เจ้า1         กบัตร.         เปิดเ« อร์5เร"""
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

torch.onnx.export(
    model,
    input_ids,
    "qwen2_5_1_5B_instruct.onnx",
    export_params=True,
    opset_version=14,  # or a suitable version for your needs
    do_constant_folding=True,
    input_names=["input_ids"],
    output_names=["output"],
    dynamic_axes={"input_ids": {0: "batch_size"}, "output": {0: "batch_size"}},
)