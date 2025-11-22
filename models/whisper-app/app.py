import gradio as gr
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import warnings
import os
import sys

# Suppress warnings
warnings.filterwarnings("ignore")

print("Starting Working Gradio Whisper ASR App...")

# Load model at startup (not lazy loading to avoid UI issues)
print("Loading Whisper model...")
model_path = "./"

# Check if model files exist
required_files = ["config.json", "model.safetensors"]
# Fallback to pytorch_model.bin if safetensors is missing
if not os.path.exists(os.path.join(model_path, "model.safetensors")) and os.path.exists(os.path.join(model_path, "pytorch_model.bin")):
    required_files = ["config.json", "pytorch_model.bin"]

missing_files = [f for f in required_files if not os.path.exists(os.path.join(model_path, f))]

if missing_files:
    print(f"ERROR: Missing model files: {missing_files}")
    print("Please ensure you have 'config.json' and 'model.safetensors' (or 'pytorch_model.bin') in the current directory.")
    # We will not exit here to allow the UI to load, but it will fail when processing
    model = None
    processor = None
else:
    try:
        processor = WhisperProcessor.from_pretrained(model_path)
        model = WhisperForConditionalGeneration.from_pretrained(model_path)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = model.to(device)
        print(f"Model loaded on {device}")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None
        processor = None

def transcribe_audio(audio_file):
    """Transcribe audio using the fine-tuned Whisper model"""
    if model is None or processor is None:
        return "Error: Model not loaded. Please check server logs for missing files."

    print(f"Processing: {audio_file}")
    
    if audio_file is None:
        return "Please upload an audio file or record using the microphone."
    
    if not os.path.exists(audio_file):
        return f"File not found: {audio_file}"
    
    try:
        # Load and process audio
        audio, _ = librosa.load(audio_file, sr=16000)
        print(f"Audio loaded: {len(audio)} samples")
        
        if len(audio) == 0:
            return "Empty audio file."
        
        # Process with Whisper
        inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
        inputs = inputs.to(device)
        
        with torch.no_grad():
            predicted_ids = model.generate(
                inputs["input_features"],
                max_length=448,
                num_beams=5,
                early_stopping=True,
                task="transcribe",
                language="en"
            )
        
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        transcription = transcription.strip()
        
        print(f"Transcription: '{transcription}'")
        
        if not transcription:
            return "No speech detected."
        
        # Return simple string without formatting
        return transcription
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        return error_msg

print("Creating Gradio Blocks interface...")

with gr.Blocks(title="Whisper ASR") as demo:
    gr.Markdown("# Fine-tuned Whisper ASR")
    gr.Markdown("Upload an audio file or record directly from your microphone to transcribe speech to text.")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["upload", "microphone"],
                type="filepath",
                label="Audio Input"
            )
            submit_btn = gr.Button("Transcribe", variant="primary")
        
        with gr.Column():
            text_output = gr.Textbox(
                label="Transcription",
                lines=5,
                show_copy_button=True
            )
    
    submit_btn.click(
        fn=transcribe_audio,
        inputs=audio_input,
        outputs=text_output
    )

print("Launching app...")

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
