# **Comprehensive Documentation — AI Medical Summary & Insights Assistant**

The architecture uses different models. It is easier to describe the two models separately. 

# A **Technical Documentation - Speech** 

## **1. Environment Setup**

**Languages & Versions**

* Python 3.10+
* Node.js 18+ ( React frontend)

**Core Libraries**

```
fastapi
uvicorn
python-multipart
ollama
pydantic
pypdf
pytesseract
opencv-python
whisper
torch / cuda (for local inference)
```


**Hardware Requirements**

* GPU recommended for Whisper (NVIDIA T4 / RTX 3060+)
* CPU inference works but slower
* RAM: 8GB+
* Storage: 2–10GB depending on logs + report uploads

---

## **2. Data Pipeline**

#### **Inputs**

* **Audio**: Recorded doctor-patient conversation
* **Reports**: Lab PDFs, scan reports, prescriptions, handwritten notes (images) - not implemented yet

#### **Preprocessing**

1. **Audio**

   * Resampled to 16kHz
   * Converted to WAV → Whisper inference

2. **Reports**

   * PDF → text extraction using `pypdf`
   * Images → OCR using `Tesseract`
   * Medical terms normalized
   * Final content chunked into embeddings (FAISS/Chroma)

#### **Licensing**

* Whisper: MIT

---

## **3. Model Architecture**

#### **Modules:**

1. **Speech-to-Text: Whisper Base **

   * Language: English supported
   * Output: Clean transcript

2. **Multimodal Document Parser**

   * OCR for images
   * PDF extract
   * Medical term matcher (via ontology)



#### **Hyperparameters**

(Example based on Whisper)

```
temperature: 0
beam_size: 5
max_new_tokens: 2048
context_window: 128k
```

---

## **4. Training Summary**

* Whisper: No retraining, used pretrained base
* Embedding model: bge-base-en-v1.5
* No custom training required
* Test audio set: 30 recordings
* Average STT WER: ~6%
* OCR accuracy: ~85% on printed text

---

## **5. Evaluation Summary**

* Patient Summary Quality: Rated “Clear & Understandable” by testers
* Doctor Insight Accuracy: Flagged 7/10 clinically relevant observations
* Latency:

  * Audio → text: ~8–12 sec (1 min audio)
  * Report parsing: 2–4 sec
  * LLM outputs: 30–50 sec   (this needs to be improved)

---

## **6. Inference Pipeline**

**Pseudocode**

```python
audio = save_upload(file)
transcript = whisper_model(audio)

report_text = extract_text_from_reports(uploaded_reports)
context = transcript + report_text

doctor_output = llm_doctor.generate(context) # actually done by a human, simulated by AutoSOAP model

patient_context = doctor_output['Assessmetnt'] + doctor_output['Plan']
patient_output = llm_patient.generate(patient_context)

return {
    "patient_summary": patient_output,
    "doctor_insights": doctor_output
}
```

**API Call Example**

(not implemented, placeholder)

```
POST /process
{
  "audio": <file>,
  "reports": [<file>]
}
```

---

## **7. Deployment Details**


* **Backend**: FastAPI 
* **Frontend**: Streamlit
* **Model Hosting**:

  * Whisper: Local GPU 
 
---

## **8. System Design Considerations**

* **Scalability**

  * STT + LLM inference separated into microservices
  * Async FastAPI for parallel requests

* **Modularity**

  * Each of the 3 modules (audio, reports, LLMs) independent

* **Data Flow**

  * Audio + Report → Structured Context →  LLM Pipeline

* **Security**

  * PHI not stored permanently
  * HTTPS enforced

---

## **9. Error Handling & Monitoring**

* Audio too noisy → return “Please re-upload clearer audio”
* Unsupported report file → return friendly message
* Timeout on LLM → automatic retry
* Logging:

  * STT durations
  * OCR accuracy issues
  

---

## **10. Reproducibility Checklist**

* `requirements.txt`
* `.env.example` with API keys
* Whisper model path
* Example test audio + test reports
* Seed values if any

---

# B **Technical Documentation - Text Summarization** 

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
- **Labels:** Generated from a 'Teacher' model
- **Preprocessing:** text normalization, structured EHR cleaning.
- **Feature Extraction:** Tokenization, context alignment.
- **Datasets:** `patient_summary_finetune_data_400records.jsonl` 
- **Data Location:** Attached to Kaggle project

## 3. Model Architecture

   * Capabilities:

     * Differential diagnosis generation
     * Symptom correlation
     * Detect missing tests
     * Red-flag alert system


 **LLM #1 — Doctor Assistance Model**

* Due to license issues, replaced with AutoSOAP model
* Combines patient text and doctor text to create SOAP format output
* Impementation reused with credits
 
 **LLM #2 — Patient Summary Model**

 (TODO - describer teacher summary)

   * Style: Simple explanation, no medical jargon

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

 * LLMs: TinyLlama Endpoint on HuggingFace Spaces

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



