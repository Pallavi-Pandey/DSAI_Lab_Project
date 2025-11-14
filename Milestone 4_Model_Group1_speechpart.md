## Milestone 4: Model Training

#### Speech Processing Part

## Overview / Objective
This milestone clarifies the input and routing flow: inputs can be speech, text, or both, provided by either a doctor or a patient. When speech is present, Whisper Small is used to transcribe to text; otherwise text is used as-is. The resulting text is routed to an LLM that behaves as either a Doctor Assistant or a Patient Assistant based on the selected role. We establish the ASR pipeline and its integration points (dataset prep, preprocessing, model config, initial eval) to support this role-aware flow.

Flow:
- Input (speech and/or text) from Doctor or Patient
- If speech: Whisper → transcript; merge with any provided text
- Role selection: Doctor Assist or Patient Assist
- LLM generates role-specific output (SOAP/counseling for doctor; plain-language guidance for patient)

Link to previous context: Builds on the earlier data preprocessing and architecture rationale. Focus here is speech (ASR) with Whisper Small for practicality and deployability.

## Dataset Details

- Input type: Single-channel conversational clinical audio (doctor–patient style)
- Sampling: 16 kHz target (resampled where necessary)
- Formats: WAV/MP3 supported via soundfile/torchaudio
- Splits: Train/validation/test prepared in notebook as needed
- Notebook reference: notebooks/speech/data-prep.ipynb

### Sources & IO Stack
- Libraries: transformers, datasets, torchaudio, soundfile, accelerate, huggingface_hub, jiwer (for WER/CER), ffmpeg (I/O)
- Files organized for batched evaluation and logging

### Preprocessing
- Resampling to 16 kHz
- Waveform normalization and trimming (optional silence handling)
- Feature extraction via WhisperProcessor (log-Mel spectrograms)
- Label/normalization for evaluation (lowercasing, punctuation handling for WER/CER)

## Model Architecture

- Base Model: Whisper Small (openai/whisper-small)
- Components: WhisperForConditionalGeneration + WhisperProcessor
- Decoding: Beam search with temperature control; timestamps disabled for text-only downstream
- Configuration: Language set to English; task="transcribe"
- Output: Clean transcript per utterance for downstream text pipeline

### Rationale
- Whisper Small balances accuracy, speed, and resource usage (T4-class GPU) for demos and iterative experiments

## Training Setup

- Regime: Zero-shot baseline with optional light fine-tuning on in-domain clips
- Hardware: Single GPU (T4-class)
- Precision: FP16 where available
- Batch size / Epochs: Tuned to fit memory; gradient accumulation as needed
- Optimizer: AdamW
- Logging: Optional Weights & Biases; local logs saved

## Hyperparameter Experiments (Initial)

- Beam width: small grid (e.g., 1, 3, 5) to trade speed vs accuracy
- Temperature/top-p: tuned only if sampling used (default beam preferred for ASR)
- Chunking/stride: explored for long-form audio stability
- Normalization: multiple text normalization variants benchmarked for WER impact

### Results Snapshot (Qualitative)
- Clean audio: good readability
- Challenging audio: errors on drug names/medical terms; fast speech and overlaps reduce accuracy

## Regularization & Optimization

- Data augmentation (future): time/frequency masking, noise injection for robustness
- Grad norm clipping and small weight decay when fine-tuning

## Initial Training/Evaluation Results

- Baseline: Zero-shot Whisper Small on clinical-style snippets
- Metrics: WER and CER via jiwer with consistent text normalization
- Observed: domain terminology and overlapping speech are primary error sources

## Metrics – Initial

- WER/CER reported per split; store predictions and references for reproducibility
- Track effect of decoding settings (beam vs greedy) and normalization choices

## Model Artifacts

- Saved configs and processor settings for reproducibility
- Optional fine-tuned checkpoints (if run) and decoding configs
- Batch predictions and references CSV/JSON for metric computation
- Notebook: notebooks/speech/data-prep.ipynb

## Observations / Notes for Next Milestone

### Performance
- Whisper Small is adequate for demo; in-domain fine-tuning expected to reduce WER on medical vocabulary

### Issues
- Multi-speaker overlap and background noise
- Domain-specific terminology recognition (drug names, diagnoses)

### Next Steps
- Light fine-tuning on curated clinical clips
- Add domain lexicon/pronunciation hints and improved text normalization
- Evaluate diarization or turn-taking heuristics for cleaner role-aware transcripts
- Integrate ASR outputs with role-based prompts (Doctor Assist / Patient Assist) for end-to-end testing
