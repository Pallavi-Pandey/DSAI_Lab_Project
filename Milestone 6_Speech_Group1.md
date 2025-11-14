## Milestone 6: Speech (ASR) – Data Prep, Modeling, and Evaluation

#### Speech Processing Part

## Overview / Objective
This milestone documents the Automatic Speech Recognition (ASR) component used to convert doctor–patient audio conversations into text that feeds the Text module. We use Whisper for ASR and Llama 3.2 for downstream text generation (e.g., clinical note simplification/summary). It covers data preparation, model setup, evaluation with speech-specific metrics, and integration readiness for the end-to-end pipeline.

Link to previous milestones:
- Milestone 4 (Text): Initial text modeling setup; our current pipeline replaces/augments this with Llama 3.2 for summarization.
- Milestone 5 (Text): Evaluation approach reused for the Llama 3.2 text component where applicable.

This milestone ensures the Speech module (Whisper) produces reliable, structured transcripts to support the Llama 3.2 text workflows.

## Dataset Details
- Input type: Single-channel audio clips with conversational speech (doctor–patient style), processed via Python notebooks.
- Format/IO stack: `transformers`, `datasets`, `soundfile`, `torchaudio`, `accelerate`, `huggingface_hub`, `wandb`, `jiwer` (for WER/CER), `ffmpeg` (I/O backend).
- Sampling rate: 16 kHz (Whisper standard). Resampling performed where necessary.
- Splits: Train/validation/test prepared within the notebook as needed for model evaluation.

Notebook reference:
- notebooks/speech/data-prep.ipynb

## Preprocessing
- Audio loading and resampling.
- Normalization and trimming/silence handling as appropriate to improve robustness.
- Tokenization/processor pipeline via Whisper’s `WhisperProcessor` (feature extractor + tokenizer).
- Label preparation for character/word-level evaluation (for WER/CER computation with `jiwer`).

## Model Architecture
- ASR: Whisper Small (`openai/whisper-small`), implemented via `WhisperForConditionalGeneration` + `WhisperProcessor`.
- Decoding: Beam search with temperature control; timestamps disabled for downstream text tasks.
- Resource profile: Single T4-class GPU; FP16 where supported.
- Output: Clean transcript per utterance; optional language/tag configuration (e.g., English, `task="transcribe"`).
 
### Downstream Text Model (for integration context)
- LLM Runtime: llama.cpp (GGUF models). We use Llama 3.2 (instruction-tuned) served via llama.cpp for on-device/lightweight inference.
- Notes: Select an appropriate GGUF quantization (e.g., Q4_K_M/Q5_K_M) based on hardware. Prompts mirror the summarization instructions from the text milestones.
- Flow: Whisper transcripts → llama.cpp (Llama 3.2) prompts → patient-friendly summaries.

## Interaction Flow (Doctor vs Patient)
- Input: Doctor or Patient provides speech.
- ASR: Whisper Small transcribes audio → clean text.
- Role selection: User selects role (Doctor Assist or Patient Assist), or auto-detected via UI/metadata.
- Branching prompts to Llama 3.2 (via llama.cpp):
  - Doctor Assist: Provide clinician-oriented assistance (e.g., SOAP draft, differential hints, counseling checklist). Keep concise, evidence-aware, no hallucinations.
  - Patient Assist: Provide plain-language explanation and next steps. Empathetic, non-diagnostic language, safety disclaimers when appropriate.
- Output: Rendered text back to the respective user; optionally saved for audit/logs.

### Prompt skeletons (concise)
- Doctor Assist prompt:
  """
  You are assisting a clinician.
  Transcript: {transcript}
  Task: Draft a concise SOAP-style note (S/O/A/P) and 3 brief counseling points.
  Constraints: Be factual, avoid speculation, no prescriptions without sufficient evidence.
  """

- Patient Assist prompt:
  """
  You are assisting a patient with no medical background.
  Transcript: {transcript}
  Task: Explain the situation and next steps in simple language (6–8 sentences), empathetic tone.
  Constraints: Avoid medical jargon; include when to seek urgent care; do not provide diagnosis.
  """

Notes:
- Multi-speaker handling can use simple role selection by user for now; diarization can be added later.
- Safety: Add guardrails for medical advice; route emergencies to standard disclaimers.

## Pipeline Diagram
```
 [Speech Input]
      |
      v
  Whisper Small (ASR)
      |
      v
  [Transcript Text]
      |
      +--> [Doctor Assist]
      |        |
      |        v
      |   Llama 3.2 via llama.cpp
      |        |
      |        v
      |   SOAP draft + clinician tips
      |
      +--> [Patient Assist]
               |
               v
          Llama 3.2 via llama.cpp
               |
               v
          Plain-language summary + steps
```

## Training / Fine-tuning Setup
- Hardware: Single-GPU environment comparable to prior milestones (T4 class).
- Regime: Zero-shot (base Whisper) or light fine-tuning on in-domain clips.
- Batch size/epochs: Selected to fit memory constraints; gradient accumulation used as required.
- Optimization: AdamW; mixed precision enabled when available.
- Logging: Weights & Biases optional; local logs stored for runs.

## Evaluation Setup
- Metrics:
  - Word Error Rate (WER) via `jiwer` (with standard normalization: lowercasing, punctuation removal).
  - Character Error Rate (CER) where relevant.
- Procedure:
  - Load base/fine-tuned Whisper model and processor.
  - Run inference on validation/test splits; disable timestamps.
  - Compute WER/CER against references with consistent normalization.
- Outputs stored for reproducibility (predictions and references saved to file).

## Quantitative Results (Initial)
- WER/CER reported from the evaluation notebook runs.
- Observed sensitivity to background noise, speech rate, and domain terms (medical vocabulary).
- Similar to Text milestones, results are tracked across splits to monitor generalization.

## Qualitative Results
- Spot-checked segments show reasonable transcription for clean audio.
- Common error modes:
  - Domain-specific terminology (drug names, diagnoses).
  - Overlapping speech/interruptions.
  - Accents and rapid speech.

## Error Analysis
- Vocabulary: Missed or substituted medical terms; consider domain lexicon augmentation.
- Audio conditions: Noise and reverberation impact; consider augmentation (time/frequency masking, noise injection).
- Long-form conversations: Segmenting and context stitching strategies to be evaluated.

## Limitations
- Resource-bound batch sizes influence convergence speed and final accuracy.
- Domain vocabulary coverage is incomplete without targeted augmentation.
- Real-world clinical audio may include multi-speaker overlap; diarization not yet integrated.

## Notes for Next Milestone
- Explore domain lexicon/pronunciation hints and custom text normalizers for medical terms.
- Light fine-tuning of Whisper on in-domain clips to reduce WER for drug names/diagnoses.
- Evaluate diarization or turn-taking heuristics for cleaner downstream text.
- Connect Whisper outputs directly to Llama 3.2 for end-to-end evaluation (Speech → Llama 3.2 summary).

## Model Artifacts
- Preprocessing notebook and scripts for audio ingestion and evaluation.
- Saved processor/config and model checkpoints when applicable.
- Prediction files (ASR outputs) and references for metrics.

## Appendix
- Notebook: notebooks/speech/data-prep.ipynb
- Libraries: transformers, datasets, torchaudio, soundfile, jiwer, accelerate, huggingface_hub, wandb, ffmpeg; llama.cpp for downstream text inference (GGUF runtime)
- Downstream linkage: Whisper outputs feed Llama 3.2 (via llama.cpp) summarization.
