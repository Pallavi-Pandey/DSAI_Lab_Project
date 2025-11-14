
# Technical Overview of LLM Summarization Module



## **B. Technical Documentation (`/docs/technical.md`)**

# Technical Documentation

## 1. Environment Setup
- **Python Version:** 3.10
- **Key Libraries:**
  - torch
  - transformers
  - peft
  - streamlit
  - huggingface_hub
- **Install Instructions:**
  ```
  pip install -r requirements.txt
  ```
- **Hardware:** Minimum GPU for inference, local CPU for testing.

## 2. Data Pipeline
- **Preprocessing:** ASR for voice, text normalization, structured EHR cleaning.
- **Feature Extraction:** Tokenization, context alignment.
- **Datasets:** `patient_summary_finetune_data_400records.jsonl` (credit State Government of Bihar, anonymized).
- **Data Location:** Attached to project, or hosted on HF Datasets.

## 3. Model Architecture
- **Base Model:** TinyLlama/TinyLlama-1.1B-Chat-v1.0
- **Fine-Tuning:** PEFT LoRA adapter.
- **Diagram:** [$ARCHITECTURE_IMAGE]
- **Hyperparameters:** batch_size=4, max_new_tokens=256, top_p=0.95, temperature=0.7.

## 4. Training Summary
- **Time:** 4 hours (T4 GPU)
- **Epochs:** 10
- **Optimizer:** 8-bit AdamW
- **Loss:** Cross-entropy
- **Metrics:** ROUGE-L, BERTScore, Medical Term Retention

## 5. Evaluation Summary
- **Test Metrics:** ROUGE-L 0.26, BERTScore F1 0.88, Medical Term Retention 70%.
- **Insights:** LoRA improves factual accuracy; hallucinations reduce with larger context.

## 6. Inference Pipeline
- **Input:** Assessment and Plan (text).
- **Output:** Patient-friendly summary.
- **Snippet:**
  ```
  prompt = f"Assessment: {assessment}\nPlan: {plan}\nRewrite the above for a patient with no medical background."
  inputs = tokenizer(prompt, return_tensors="pt").to(device)
  outputs = model.generate(**inputs, max_new_tokens=256, ...)
  generated_text = tokenizer.decode(outputs, skip_special_tokens=True)[len(prompt):]
  ```

## 7. Deployment Details
- **Platform:** Hugging Face Spaces (Gradio/Streamlit).
- **Model Hosting:** PEFT LoRA adapter on HF Model Hub.


## 8. System Design Considerations
- **Modular:** Segregated preprocessing, inference, and UI.
- **Scalable:** Model can be updated with new data.
- **Data Flow:** Input → preprocessing → model → UI/API.

## 9. Error Handling & Monitoring
- **NaN Handling:** Fallback for empty outputs.
- **Latency:** Monitoring via app logs.
- **Failures:** Re-load checkpoint and retry.

## 10. Reproducibility Checklist
- **Paths:** `./distilled-student-peft`, `./docs/`
- **Seed:** Fixed seed for training/inference.
- **Checkpoints:** Model and tokenizer checkpoints on HF Hub.
- **Config:** See `config.json` and `requirements.txt`.

- **Interaction:** UI at https://huggingface.co/spaces/srsrini/DSAIL_endpoint
- **Example Request:**
-   Please see User Guide
