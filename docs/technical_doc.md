# **Comprehensive Documentation — AI Medical Summary & Insights Assistant**

#  **Technical Documentation**

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
* **Reports**: Lab PDFs, scan reports, prescriptions, handwritten notes (images)

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

3. **LLM #1 — Patient Summary Model**

   * Style: Simple explanation, no medical jargon

4. **LLM #2 — Doctor Assistance Model**

   * Capabilities:

     * Differential diagnosis generation
     * Symptom correlation
     * Detect missing tests
     * Red-flag alert system

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
  * LLMs: TinyLlama Endpoint on HuggingFace Spaces

---

## **8. System Design Considerations**

* **Scalability**

  * STT + LLM inference separated into microservices
  * Async FastAPI for parallel requests

* **Modularity**

  * Each of the 3 modules (audio, reports, LLMs) independent

* **Data Flow**

  * Audio + Report → Structured Context → Dual LLM Pipeline

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
  * LLM latency spikes

---

## **10. Reproducibility Checklist**

* `requirements.txt`
* `.env.example` with API keys
* Whisper model path
* Example test audio + test reports
* Seed values if any

---

