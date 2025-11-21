# Project Implementation Overview

- Project: Multi-Modal Clinical Assistant (Speech → OCR → Text → Role-Aware Summaries)
- Team: Group 1
- Course: DS & AI Lab Project
- Date: 2025-11-14

---
# Note
This document provides a sketch of the project. The detailed project report is included in the docs directory. Please do not use this document for evaluation. 

# Abstract

We present a practical clinical assistant that converts speech or text inputs and attached reports into two role-aware outputs: (1) clinician-oriented structured notes and insights, and (2) patient-friendly summaries. The pipeline combines Whisper Small for ASR, OCR for documents, and instruction-tuned LLMs for summarization with role-specific prompts. Earlier stages explored data preparation, model distillation (teacher: Mistral-7B-Instruct; student: TinyLlama-1.1B with LoRA), and evaluation using ROUGE/BERTScore (text) and WER/CER (speech). We also provide a deployment blueprint (Colab and local API). Results show acceptable semantic fidelity and practical latency, with clear next steps around domain adaptation, diarization, and safety.

---

# Introduction

Clinical encounters contain rich, unstructured information that must be accurately documented and communicated. Manual workflows can be time-consuming and inconsistent for both doctors and patients. We build an end-to-end, role-aware system that:

- Accepts input as speech and/or text, optionally with uploaded reports (PDFs/images).
- Uses Whisper to transcribe speech; OCR to extract report text.
- Generates two outputs via tailored prompts:
  - Doctor Assist (SOAP-style draft, counseling points, potential flags)
  - Patient Assist (plain-language explanation and next steps)

The design emphasizes deployability (compact models where possible), transparent metrics, and simple UX.

---

# Literature Review (Milestone 1)

- ASR in healthcare: Transformer-based models (e.g., Whisper) enable robust transcription across accents/noise.
- Clinical note generation: SOAP frameworks and prompt-based LLM summarization improve consistency.
- Teacher–student distillation: Larger models generate high-quality labels; smaller models (LoRA adapters) are efficient at runtime.
- Evaluation: ROUGE/BERTScore for summarization; WER/CER for speech; qualitative checks for hallucination/term retention.

References to project docs: Milestone PDFs in repo root.

---

# Dataset and Methodology (Milestone 2–3)

- Sources and Assets
  - Dialogue-to-SOAP generation via AutoSOAP exploration.
  - Summarization training pairs created from SOAP (assessment/plan) using a teacher LLM.
  - Speech snippets curated for ASR evaluation; vision assets used for OCR trials.
- Preprocessing
  - ASR: 16 kHz resampling, normalization, Whisper feature extraction.
  - Text: prompt construction, filtering missing fields, tokenization.
  - Vision: OCR from PDFs/images; basic normalization.
- Methodology
  - Role-aware prompting (Doctor vs Patient) with safety guidance.
  - Distillation workflow to study scaling and label quality.

Notebooks (examples):
- Text: notebooks/text/dsail-llm-part_ver1.ipynb, dsail-llm-part_ver2.ipynb, dsail-llm-inference.ipynb, autosoap-ai-powered-clinical-documentation.ipynb
- Speech: notebooks/speech/data-prep.ipynb
- Vision: notebooks/vision/OCR.ipynb

---

# Model Development and Hyperparameter Tuning (Milestone 4)

- Teacher model: Mistral-7B-Instruct-v0.3 generates patient-friendly labels from SOAP components.
- Student model: TinyLlama-1.1B-Chat with LoRA (r=8, α=16, dropout=0.1) for efficient fine-tuning.
- Whisper Small (openai/whisper-small) for ASR; decoding via greedy/beam; English, task="transcribe".
- Prompts: concise, empathetic, non-hallucinatory patterns for patient; structured SOAP + counseling for doctor.
- Training constraints: Batch size limited by T4-class GPU; gradient accumulation; AdamW; FP16 where supported.
- Observations: Trade-offs between context window and memory; blank-output mitigation via prompt/output handling; ASR vocabulary challenges on medical terms.

Visuals:
- Text model architecture (from Milestone 4):
  - https://github.com/user-attachments/assets/35b71e6f-f0db-4a86-9fd0-0e0d3e113d1b

---

# Evaluation & Analysis (Milestone 5)

- Summarization Metrics
  - ROUGE-L ≈ 0.24, BERTScore ≈ 0.88 (train/test parity suggests limited overfitting).
  - NaN/blank outputs reduced to ~1% after inference tuning.
- ASR Metrics
  - WER/CER via jiwer with consistent normalization.
  - Error modes: drug names, diagnoses, rapid/overlapping speech.
- Qualitative Highlights
  - Patient summaries are generally clear and aligned; occasional phrasing drift.
  - Doctor outputs benefit from structured prompts and safety constraints.

---

# Deployment & Documentation (Milestone 6)

- Runtime Components
  - Whisper Small for ASR; Llama 3.2 for role-aware text generation.
  - OCR pipeline for reports where used.
- Interaction Flow (role-aware)
  - Input (speech/text) → (If speech) Whisper transcript → Role selection (Doctor/Patient) → Prompt → LLM → Output
- Deliverables
  - Deployment deliverable with instructions (Colab-first) and examples.
  - Repository structure and inline links to notebooks/files.

---

# Conclusion and Future Work

We delivered a multi-modal assistant that produces role-aware outputs from speech/text inputs and attached reports. The approach demonstrates practical performance with compact models, clear prompts, and simple deployment pathways.

Future Work:
- Domain lexicon/pronunciation hints for ASR; in-domain fine-tuning to reduce WER on medical terms.
- Diarization/turn-taking for multi-speaker conversations.
- End-to-end evaluation harness combining WER/CER with downstream task metrics.
- Guardrails for medical safety and escalation guidance.
- Frontend polishing (Streamlit/Gradio) and fully containerized services.

---

# References and Appendix

- Repo documents:
  - Milestone 1_Problem Definition & Literature Review_Group1.md
  - Milestone 2_Dataset Preparation_Group1.md
  - Milestone 3_Architecture_Group1.md
  - Milestone 4_Model_Group1.md
  - Milestone 5_Evaluation_Group1.md
  - Milestone 6_Deployment Deliverable.md
- Notebooks:
  - notebooks/text/autosoap-ai-powered-clinical-documentation.ipynb
  - notebooks/text/dsail-llm-part_ver1.ipynb
  - notebooks/text/dsail-llm-part_ver2.ipynb
  - notebooks/text/dsail-llm-inference.ipynb
  - notebooks/speech/data-prep.ipynb
  - notebooks/vision/OCR.ipynb
- Tools/Models:
  - Whisper: https://github.com/openai/whisper
  - llama: https://github.com/ggerganov/llama.cpp
  - Hugging Face Transformers, PEFT, Datasets, Accelerate, Jiwer

Appendix materials can include additional prompts, metrics tables, and sample predictions.
