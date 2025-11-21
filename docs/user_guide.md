
# **User Documentation**

## **App Overview**

A tool for medical teams to convert raw patient conversations + reports into:

* A simple summary for patients
* A clinically intelligent insight report for doctors

## **How to Use the App**

### **Step 1 — Upload**

* Upload the **audio recording**
* Upload all **patient reports** (PDF, images, prescriptions)

### **Step 2 — Review Outputs**

You’ll see two results:

1. **Patient-Friendly Summary**

   * Editable
   * Meant to help patients understand their condition

2. **Doctor Insight Report**

   * Flags risks
   * Suggests tests
   * Highlights inconsistencies

### **Step 3 — Approve/Send**

* Medical staff edits → Save → Send to patient

---
## Specific User Guide - LLM Summary Model

### App Overview
Generate patient-friendly summaries from clinical notes.

### Input Description
Enter Assessment and Plan text.

### Output Description
Read a simple, clear summary.

### Step-by-Step Instructions
1. Launch/Access the app at https://huggingface.co/spaces/srsrini/DSAIL_endpoint
2. Enter the assessment and plan.
3. Click "Generate Summary."
4. The summary takes 25-40 seconds

   
### Troubleshooting - LLM
- If the app doesn’t load, refresh your browser.
- For errors, check input format (text only, no special characters).

### Screenshots
<img width="1356" height="724" alt="image" src="https://github.com/user-attachments/assets/46adfbc8-3f38-4426-b251-4e8c3fd1b63d" />




## **Troubleshooting**

| Issue                | Fix                                                      |
| -------------------- | -------------------------------------------------------- |
| Audio rejected       | Try uploading a WAV/MP3 ≤ 50MB                           |
| OCR failed           | Ensure PDF has selectable text or upload a clearer image |
| Summary doesn’t load | Reload → model auto-retries                              |
| App is slow          | Large reports or long audios increase processing time    |

---
