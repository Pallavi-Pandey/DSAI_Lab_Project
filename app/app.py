# HF spaces app for LLM summarization

# imports

import gradio as gr
import torch
from peft import PeftModel, PeftConfig
from transformers import AutoTokenizer, AutoModelForCausalLM


# before loading model - check directories
import requests
response = requests.get("https://huggingface.co/srsrini/medical_conv_summary/resolve/main/adapter_config.json")
print("Got this response code ...", response.status_code)


# remove any auth tokens - HF gave some issues on access

from huggingface_hub import HfFolder, login


token = HfFolder.get_token()  
if token is not None:
    HfFolder.delete_token()  # This removes the token


# now load the model - same as inference code
# add flag to not use auth token

from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "srsrini/medical_conv_summary"
peft_config = PeftConfig.from_pretrained(model_name, use_auth_token=False)
base_model = AutoModelForCausalLM.from_pretrained(
    peft_config.base_model_name_or_path,
    use_auth_token=False
)

model = PeftModel.from_pretrained(base_model, model_name, use_auth_token=False)
tokenizer = AutoTokenizer.from_pretrained(
    peft_config.base_model_name_or_path,
    use_auth_token=False
)


# main inference function - gradio format

def generate_patient_summary(assessment, plan):

    prompt = f"Assessment: {assessment}\nPlan: {plan}\nRewrite the above for a patient with no medical background."
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        gen_output = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            top_p=0.95,
            temperature=0.7,
            eos_token_id=tokenizer.eos_token_id
        )
    full_output = tokenizer.decode(gen_output[0], skip_special_tokens=True)
    generated_text = full_output[len(prompt):].strip()
    return generated_text

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Patient Summary Generator")
    with gr.Row():
        assessment = gr.Textbox(lines=2, label="Assessment")
        plan = gr.Textbox(lines=2, label="Plan")
    submit = gr.Button("Generate Summary")
    output = gr.Textbox(lines=10, label="Generated Patient-Friendly Summary")
    submit.click(fn=generate_patient_summary, inputs=[assessment, plan], outputs=output)

# Launch app
demo.launch()
