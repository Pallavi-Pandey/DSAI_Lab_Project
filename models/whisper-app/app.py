import gradio as gr
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import warnings
import os

# Suppress warnings
warnings.filterwarnings("ignore")

print("Starting Working Gradio Whisper ASR App...")

# Load model at startup (not lazy loading to avoid UI issues)
print("Loading Whisper model...")
model_path = "./"
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
print(f"Model loaded on {device}")

def transcribe_audio(audio_file):
    """Transcribe audio using the fine-tuned Whisper model"""
    print(f"Processing: {audio_file}")
    
    if audio_file is None:
        return "Please upload an audio file."
    
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

print("Creating simple Gradio interface...")

# Create the simplest possible interface
demo = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.inputs.Audio(source="upload", type="filepath"),
    outputs="text",  # Use simple text output
    title="Whisper ASR - Working Version",
    description="Upload audio file for transcription"
)

print("Launching app...")

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )
