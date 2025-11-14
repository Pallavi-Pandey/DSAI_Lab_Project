### **Deployment Deliverable:**

* **Google Colab or Kaggle Demo Notebook** (fallback for GPU-heavy Whisper + Llama pipeline)
* **Local Demo + REST API** (FastAPI)

---

# **1. Clear Instructions to Run**

## **Option A — Run on Google Colab / Kaggle (Recommended for GPU models)**

1. Open the notebook:

   ```
   notebooks/deployment/colab_demo.ipynb
   ```
2. Set runtime to **GPU**
   *Runtime → Change runtime type → GPU (T4/P100/V100)*
3. Run all cells to:

   * Install dependencies
   * Load Whisper for ASR
   * Load Text Processing Pipeline (Milestone 4 + 5)
   * Load Llama 3.2 for final generation
4. Provide input (audio/text)
5. Select role (doctor/patient)
6. View final output

---

# **2. Inputs / Outputs (With Examples)**

## **Inputs Accepted**

| Input Type            | Description                        |
| --------------------- | ---------------------------------- |
| **Audio (.wav/.mp3)** | Whisper ASR converts to transcript |
| **Text**              | Direct user message                |
| **Role**              | doctor / patient                   |
| **Mixed Mode**        | audio + text combined              |

---

# **Output Types**

### **Doctor Mode Output**

```
S: Patient reports acute lower back pain...
O: No vitals provided...
A: Possible musculoskeletal strain...
P: Recommend NSAIDs and rest...
```

### **Patient Mode Output**

```
There are many possible reasons for severe headaches, and I'll try to break them down simply:

1. **Tension headaches**: These are the most common type of headache, often caused by muscle tension in the neck and scalp.
2. **Migraines**: These can be debilitating ....
```

---

# **3. Example Inputs & Outputs**

### **Example — Text Input (Doctor Mode)**

**Input Text:**
“Patient reports vomiting and headache for 2 hours.”

**System Output:**

```
S: Vomiting + headache for 2 hours.
O: No objective findings given.
A: Consider migraine, gastritis, dehydration.
P: Recommend fluids, anti-emetic, consider neuro exam.
```

---
