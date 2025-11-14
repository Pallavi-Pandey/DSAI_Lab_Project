# **Comprehensive Documentation — AI Medical Summary & Insights Assistant**

## A. **Overview**

### **Problem**

Doctors record patient conversations and receive scattered reports (labs, scans, prescriptions).
Currently, turning this into:

1. A **patient-friendly summary**, and
2. A **doctor-assisting clinical insight report**

…is slow, manual, and inconsistent.

### **Objective**

Build a system where medical staff can upload:

* **Patient audio recordings**
* **Attached medical reports (PDFs, images)**

And automatically generate:

1. **Patient-Friendly Summary**

   * Simplified, accurate explanation
   * Reviewed/edited by the medical team before sending to patient

2. **Doctor Insight Report**

   * A second LLM highlights potential risks, differential diagnoses, anomalies
   * Helps doctors avoid missing edge cases

### **Architecture Summary**

```
               ┌──────────────────────────┐
               │       Audio Upload       │
               └───────────┬──────────────┘
                           │
               ┌───────────▼───────────────┐
               │   Speech-to-Text Module   │
               │       (Whisper)           │
               └───────────┬───────────────┘
                           │  Transcript
        Reports Upload     │
   (PDFs, Images, Text)    │
           ┌───────────────▼───────────────┐
           │       Report Processing       │
           │ (OCR + LLM Processing Layer)  │
           └───────────────┬───────────────┘
                           │ Combined Context
               ┌───────────▼───────────────┐
               │     LLM #1 (Patient)      │
               │  Patient-Friendly Summary │
               └───────────┬───────────────┘
                           │
               ┌───────────▼───────────────┐
               │     LLM #2 (Doctor)       │
               │   Clinical Insight Engine │
               └───────────┬───────────────┘
                           │
        ┌──────────────────▼─────────────────────┐
        │            Frontend / Dashboard        │
        │ - Review summary                       │
        │ - Edit before sending to patient       │
        │ - Access doctor insights               │
        └────────────────────────────────────────┘
```

### **Deployed Components**

| Component                       | Platform                       | Status       |
| ------------------------------- | ------------------------------ | ----------   |
| Frontend (Streamlit)            | local                          | Not Deployed |
| Backend API (FastAPI)           | local                          | Not Deployed |
| Whisper STT Model               | Google colab                   | Integrated   |
| LLMs (Patient & Doctor)         | Google colab                   | Integrated   |

---

## B. **Technical Documentation**

### **1. Environment Setup**

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

### **2. Data Pipeline**

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

### **3. Model Architecture**

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

### **4. Training Summary**

* Whisper: No retraining, used pretrained base
* Embedding model: bge-base-en-v1.5
* No custom training required
* Test audio set: 30 recordings
* Average STT WER: ~6%
* OCR accuracy: ~85% on printed text

---

### **5. Evaluation Summary**

* Patient Summary Quality: Rated “Clear & Understandable” by testers
* Doctor Insight Accuracy: Flagged 7/10 clinically relevant observations
* Latency:

  * Audio → text: ~8–12 sec (1 min audio)
  * Report parsing: 2–4 sec
  * LLM outputs: 3–7 sec

---

### **6. Inference Pipeline**

**Pseudocode**

```python
audio = save_upload(file)
transcript = whisper_model(audio)

report_text = extract_text_from_reports(uploaded_reports)
context = transcript + report_text

patient_output = llm_patient.generate(context)
doctor_output = llm_doctor.generate(context)

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

### **7. Deployment Details**

* **Backend**: FastAPI 
* **Frontend**: Streamlit
* **Model Hosting**:

  * Whisper: Local GPU 
  * LLMs: Ollama API

---

### **8. System Design Considerations**

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

### **9. Error Handling & Monitoring**

* Audio too noisy → return “Please re-upload clearer audio”
* Unsupported report file → return friendly message
* Timeout on LLM → automatic retry
* Logging:

  * STT durations
  * OCR accuracy issues
  * LLM latency spikes

---

### **10. Reproducibility Checklist**

* `requirements.txt`
* `.env.example` with API keys
* Whisper model path
* Example test audio + test reports
* Seed values if any

---

## C. **User Documentation**

### **App Overview**

A tool for medical teams to convert raw patient conversations + reports into:

* A simple summary for patients
* A clinically intelligent insight report for doctors

### **How to Use the App**

#### **Step 1 — Upload**

* Upload the **audio recording**
* Upload all **patient reports** (PDF, images, prescriptions)

#### **Step 2 — Review Outputs**

You’ll see two results:

1. **Patient-Friendly Summary**

   * Editable
   * Meant to help patients understand their condition

2. **Doctor Insight Report**

   * Flags risks
   * Suggests tests
   * Highlights inconsistencies

#### **Step 3 — Approve/Send**

* Medical staff edits → Save → Send to patient

---

### **Troubleshooting**

| Issue                | Fix                                                      |
| -------------------- | -------------------------------------------------------- |
| Audio rejected       | Try uploading a WAV/MP3 ≤ 50MB                           |
| OCR failed           | Ensure PDF has selectable text or upload a clearer image |
| Summary doesn’t load | Reload → model auto-retries                              |
| App is slow          | Large reports or long audios increase processing time    |

---