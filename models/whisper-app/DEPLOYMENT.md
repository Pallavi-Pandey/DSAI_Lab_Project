# Deployment Instructions for Hugging Face Spaces

## Quick Deployment Steps

1. **Create a new Hugging Face Space:**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Set the space name (e.g., "fine-tuned-whisper-asr")

2. **Upload the files:**
   - Upload all files from this `whisper-app/` folder to your HF Space
   - Make sure `model.safetensors` and all config files are included
   - The `README.md` will automatically configure the Space metadata

3. **Files to upload:**
   ```
   whisper-app/
   ├── app.py                    # Main Gradio application
   ├── requirements.txt          # Python dependencies
   ├── README.md                # Space configuration and description
   ├── model.safetensors         # Your fine-tuned Whisper model (151MB)
   ├── config.json              # Model configuration
   ├── generation_config.json   # Generation parameters
   ├── tokenizer_config.json    # Tokenizer configuration
   ├── preprocessor_config.json # Audio preprocessing config
   ├── special_tokens_map.json  # Special tokens mapping
   ├── vocab.json               # Vocabulary
   ├── merges.txt               # BPE merges
   ├── added_tokens.json        # Additional tokens
   ├── normalizer.json          # Text normalization
   └── training_args.bin        # Training arguments
   ```

4. **Alternative: Git-based deployment:**
   ```bash
   # Initialize git in whisper-app folder
   cd whisper-app
   git init
   git add .
   git commit -m "Initial commit: Fine-tuned Whisper ASR app"
   
   # Add HF Space as remote (replace USERNAME/SPACE_NAME)
   git remote add origin https://huggingface.co/spaces/USERNAME/SPACE_NAME
   git push -u origin main
   ```

## App Features

✅ **Upload audio files** (WAV, MP3, FLAC, M4A, etc.)
✅ **Live microphone recording**
✅ **Automatic transcription** using your fine-tuned model
✅ **Modern UI** with tabs and responsive design
✅ **Error handling** for robust operation

## Model Information

- **Model file:** `model.safetensors` (151MB)
- **Type:** Fine-tuned Whisper model
- **Framework:** Transformers + PyTorch
- **Audio processing:** LibROSA for preprocessing

## Testing Locally (Optional)

If you want to test locally before deployment:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at `http://localhost:7860`

## Troubleshooting

- **Large file upload:** If `model.safetensors` is too large for web upload, use Git LFS
- **Memory issues:** The model loads into memory; ensure your Space has sufficient RAM
- **Audio format issues:** The app handles most common formats via LibROSA

## Space Configuration

The `README.md` includes proper metadata for HF Spaces:
- SDK: Gradio 4.44.0
- License: Apache 2.0
- App file: app.py
- Emoji and colors for branding
