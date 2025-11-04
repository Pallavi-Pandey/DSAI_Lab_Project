
## **Milestone 3 : MultiModalHealthcareModel - Architecture**

<img width="671" height="451" alt="image" src="https://github.com/user-attachments/assets/40dea8c9-e310-44c6-9bab-1f96adcae39a" />


(assume that the picture has been included)

## **Inputs**

-   **Left side:**  The system accepts  **multiple types of input**  related to the patient encounter:
    
    -   **Patient voice recordings**  (e.g., speech input from the patient).
        
    -   **Doctor voice recordings**  (e.g., speech from the doctor during consultation).
    - **Images** - Results of medical procedures like X-Ray, etc. and handwritten notes/diagnosis by the Doctor (aspirational)
        
    -  
        

## **Preprocessing**

-   Each input modality is preprocessed:
    
    -   **Speech inputs**  are transcribed using Automatic Speech Recognition (ASR).
        
    -   **Text/EHR data**  are tokenized and standardized for further use.
        
-   Outputs are ready-to-use transcripts or structured data for the doctor’s review.
    

## **Multimodal Presentation**

-   Encoded/transcribed data from all modalities are presented to the doctor, enabling comprehensive review:
    
    -   **Fusion strategies**  (e.g., synchronized display, topical alignment) help the doctor quickly grasp the full context.
        
    -   The combined view facilitates cross-modal analysis by the doctor. This fusion module is outside the scope of this version of the project.
        

## **Doctor (Human Core)**

-   The  **doctor is at the core**  of the model and uses the multimodal inputs to:
    
    -   **Review all patient data**  (speech, notes, images) in an integrated format.
    
     -   **Generate Notes/Diagnosis for further processing**  drawing on their expertise.

## **Summarization Model**
       
        
   -  **Generate clinical SOAP notes**  (Subjective, Objective, Assessment, Plan), based on the notes from the Doctor
        
    -   **Create patient-friendly summaries**  for sharing with the patient.
        

## **Outputs**

-   **SOAP Notes:**  The doctor produces a detailed clinical summary.
    
-   **Patient-Friendly Summaries:**  The doctor also creates a simplified version for the patient.
    
-   The outputs reflect the doctor’s judgment and professional insight.
    

## **Special Agents or Modules**

-   **Modules or agents**  may assist with:
    
    -   **Data preprocessing**  (ASR, normalization).
        
    -   **Multi-modal fusion/display**  (integrated timelines, highlight extraction).
        
-   These modules are  **supportive tools**—the doctor makes the final decision.
    

## **Data Flow**

-   Arrows show the sequential/parallel flow:
    
    -   From input → preprocessing → multimodal presentation → doctor review → outputs.
        
-   Modules may offer feedback or clarification upon request.
    

## **Technology**

-   Underlying the system is  **AI-assisted preprocessing**  and  **multimodal data integration**.
    
-   The  **final clinical reasoning and documentation remain with the doctor**.
    

----------

## **Summary**

This model is a  **multimodal AI-assisted system for healthcare**  that:

-   Integrates  **voice, text, and possibly medical images**.
    
-   Presents unified data to the  **doctor**  for comprehensive review.
    
-   Supports the doctor in generating  **SOAP notes and patient-friendly summaries**.
    

-   **The doctor is central to decision-making**; AI provides tools for efficiency and presentation.
