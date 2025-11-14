## Milestone 5: Model Evaluation & Analysis

#### Speech Processing Part (ASR)

## Overview / Objective
This milestone reports the evaluation of the Speech (ASR) component that feeds the role-aware LLM pipeline. We assess Whisper Small performance on clinical-style audio using standard ASR metrics and summarize qualitative findings, limitations, and next steps.

## Evaluation Setup

- Data: Clinical-style conversational audio (doctor/patient). See: notebooks/speech/data-prep.ipynb
- Runtime: Single GPU (T4-class) or CPU for small batches
- Model: Whisper Small (openai/whisper-small) with WhisperProcessor
- Decoding: Greedy/beam search (timestamps disabled). Language: English; task="transcribe"
- Normalization for metrics: lowercasing, punctuation removal, whitespace normalization (consistent across refs/preds)

## Performance Metrics

- Word Error Rate (WER) — primary metric for ASR
- Character Error Rate (CER) — useful when words are short or domain terms are frequent
- Optional: Entity/term accuracy on a curated list of medical terms (manual/regex)

## Quantitative Results (Placeholder schema)

- Report WER/CER per split (Train/Val/Test) and by audio condition when available (clean vs noisy)
- Example table structure:

| Metric | Train | Val | Test |
| :-- | --: | --: | --: |
| WER | 0.21 | 0.24 | 0.26 |
| CER | 0.12 | 0.14 | 0.15 |

Notes:
- Insert actual numbers after running evaluation cells in notebooks/speech/data-prep.ipynb
- Keep normalization consistent for fair comparison

## Qualitative Results

- Clean audio: transcripts generally accurate and readable
- Challenging audio: frequent errors on drug names and diagnoses; rapid speech and overlaps degrade performance
- Common error types:
  - Substitutions near medical terminology
  - Dropped short words in fast speech
  - Mis-segmentation when long utterances are not chunked

## Error Analysis

- By category: environment (noise/reverb), speaker (rate/accent), content (domain vocabulary)
- Analyze per-utterance WER distribution to identify tail cases
- Check effect of decoding settings (greedy vs small beam) and chunk/stride for long audio

## Limitations

- No diarization/role attribution in ASR (role handled by UI selection in downstream LLM)
- Domain vocabulary not specialized (no lexicon biasing)
- Hardware constraints limit batch size and long-context decoding

## Notes for Next Iteration

- Explore light fine-tuning on in-domain clips to reduce WER on medical terms
- Add domain lexicon/pronunciation hints, improved text normalization
- Consider diarization or turn-taking detection for cleaner transcripts
- Evaluate augmentation (noise/time/freq masking) for robustness

## Artifacts

- Evaluation notebook: notebooks/speech/data-prep.ipynb
- Saved predictions and references (CSV/JSON) per split
- Decoding configs used for reported metrics

## Integration Reminder

- Downstream flow remains role-aware:
  - Input (speech/text) → (If speech) Whisper transcript → Role selection (Doctor/Patient) → LLM prompt → Output
- ASR quality directly affects both Doctor Assist (SOAP/counseling) and Patient Assist (plain-language guidance)
