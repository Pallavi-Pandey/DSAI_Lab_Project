# DSAI Lab Project

A multimodal AI system integrating **speech**, **vision**, and **text** processing capabilities for clinical documentation and analysis.

## Overview

This project implements a comprehensive multimodal AI pipeline that combines:
- **Speech Recognition**: Audio transcription using state-of-the-art models
- **Computer Vision**: OCR and visual analysis for medical documents
- **Natural Language Processing**: LLM-based clinical documentation and analysis
- **Multimodal Fusion**: Integration layer combining insights from all modalities

## Features

- Real-time speech-to-text transcription
- Medical document OCR and analysis
- AI-powered clinical documentation generation
- RESTful API for easy integration
- Modular architecture for extensibility

## Project Structure

```
.
├── README.md
├── Final_Project_Report.md
├── docs/                               # Milestone docs & PDFs
│   ├── Milestone-1.pdf
│   ├── Milestone 2 _ DS & AI-Lab-Project.pdf
│   ├── Milestone 3 _ DS & AI-Lab-Project.pdf
│   ├── Milestone 3_Architecture_Group1.md
│   ├── Milestone 4_Model_Group1.md
│   ├── Milestone 5_Evaluation_Group1.md
│   ├── Milestone 6_Deployment Deliverable.md
│   └── Comprehensive Technical Documentation.md
│
└── notebooks/                          # Jupyter notebooks
    ├── speech/
    │   ├── data-prep.ipynb
    │   ├── finetune_code.ipynb
    │   └── llama3_2.ipynb
    ├── text/
    │   ├── autosoap-ai-powered-clinical-documentation.ipynb
    │   ├── dsail-llm-inference.ipynb
    │   ├── dsail-llm-part_ver1.ipynb
    │   └── dsail-llm-part_ver2.ipynb
    └── vision/
        ├── OCR.ipynb
        └── readme.md
```

## Project Milestones

### Milestone 1: Problem Definition & Literature Review
**Due:** October 3  
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%201_Problem_Definition_Literature_Review_Group1.md)

### Milestone 2: Dataset Preparation
**Due:** October 10  
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%202_Dataset_Preparation_Group1.md)

### Milestone 3: Model Selection & Implementation
**Due:** October 17  
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%203_Architecture_Group1.md)

### Milestone 4: Model Architecture
**Due:** October 31  
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%204_Model_Group1.md)

### Milestone 5: Model Evaluation
**Due:** November 7
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%205_Evaluation_Group1.md)

### Milestone 6: Deployment Deliverable
**Due:** November 14
**Status:** Completed  
[Documentation](https://github.com/Pallavi-Pandey/DSAI_Lab_Project/blob/main/Milestone%206_Deployment_Deliverable.md)

## Installation

```bash
# Clone the repository
git clone https://github.com/Pallavi-Pandey/DSAI_Lab_Project.git
cd DSAI_Lab_Project

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
# Start the API server
python app/main.py
```

### API Endpoints

```bash
# Example API usage
curl -X POST http://localhost:8000/api/transcribe \
  -F "audio=@sample.wav"
```

## Development

### Running Notebooks

```bash
# Launch Jupyter
jupyter notebook notebooks/
```

### Module Testing

```bash
# Test individual modules
python -m modules.speech.transcribe
python -m modules.vision.model
python -m modules.text.llm_infer
```

## Documentation

Detailed documentation for each milestone is available in the PDF files:
- `Milestone-1.pdf` - Problem definition and literature review
- `Milestone 2 _ DS & AI-Lab-Project.pdf` - Dataset preparation
- `Milestone 3 _ DS & AI-Lab-Project.pdf` - Model selection
- `Milestone 4_Model_Group1.md` - Architecture details
- `Milestone 5_Evaluation_Group1.md` - Model Evaluation
- `Milestone 6_Deployment_Deliverable.md` - Deployment Deliverable

## Contributing

This is an academic project for the DSAI Lab course. For questions or contributions, please contact the project team.

## License

This project is part of academic coursework at IIT Madras.

---

**Project Team:** DSAI Lab  
**Institution:** Indian Institute of Technology Madras  
**Last Updated:** November 2024 
