---
title: Fine-tuned Whisper ASR
emoji: 🎤
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
---

# Fine-tuned Whisper Automatic Speech Recognition

This is a Gradio app that uses a fine-tuned Whisper model for automatic speech recognition (ASR). The model has been specifically fine-tuned for improved performance on domain-specific audio data.

## Features

- 📁 **Upload Audio Files**: Support for various audio formats (WAV, MP3, FLAC, M4A, etc.)
- 🎙️ **Live Recording**: Record audio directly from your microphone
- 🎯 **High Accuracy**: Fine-tuned model for better transcription quality
- 🚀 **Fast Processing**: Optimized for quick transcription results

## Usage

1. **Upload Method**: Click on the "Upload Audio File" tab and upload your audio file
2. **Recording Method**: Click on the "Record Audio" tab and use your microphone to record
3. The transcription will appear automatically in the text box

## Model Details

This app uses a fine-tuned version of OpenAI's Whisper model, specifically optimized for:
- Better accuracy on domain-specific vocabulary
- Improved handling of various accents and speaking styles
- Enhanced performance on noisy audio conditions

## Technical Specifications

- **Model**: Fine-tuned Whisper (model.safetensors)
- **Framework**: Transformers, PyTorch
- **Interface**: Gradio
- **Audio Processing**: LibROSA, TorchAudio

## Tips for Best Results

- Use clear audio with minimal background noise
- Ensure good microphone quality for live recordings
- The model works well with various languages and accents
- Longer audio files may require more processing time

## License

This project is licensed under the Apache 2.0 License.
