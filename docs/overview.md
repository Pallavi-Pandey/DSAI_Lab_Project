# **Comprehensive Documentation — AI Medical Summary & Insights Assistant**

## **Overview**

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
                           │  Patient Transcript
        Reports Upload     │
   (PDFs, Images, Text)    │
           ┌───────────────▼───────────────┐
           │       Report Processing       │
           │ (OCR + LLM Processing Layer)  |
           │  (not implemented)            |
           └───────────────┬───────────────┘
                           │ Combined Context, Human Doctor provided
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

#### For Text Part
- **Frontend/UI:** Streamlit app running on Hugging Face Spaces.
- **Model:** PEFT LoRA adapter for patient summary generation.



| Component                       | Platform                       | Status       |
| ------------------------------- | ------------------------------ | ----------   |
| Frontend (Streamlit)            | HF Spaces                      | To be done   |
| Backend API (FastAPI)           | local                          | Not used     |
| Whisper STT Model               | Google colab                   | Integrated   |
| LLMs (Patient & Doctor)         | Kaggle, HF Spaces Gradio       | Integrated   |
| End to end model                | Zapier integration             | To be dobe   |

---

