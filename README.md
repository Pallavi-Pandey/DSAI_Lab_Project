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
├── app/                          # Application layer
│   ├── api.py                   # REST API endpoints
│   ├── main.py                  # Application entry point
│   └── utils.py                 # Utility functions
│
├── modules/                      # Core modules
│   ├── fusion/                  # Multimodal fusion
│   │   └── projector.py        # Cross-modal projection
│   ├── speech/                  # Speech processing
│   │   └── transcribe.py       # Audio transcription
│   ├── text/                    # Text processing
│   │   └── llm_infer.py        # LLM inference
│   └── vision/                  # Vision processing
│       └── model.py            # Visual models
│
├── notebooks/                    # Jupyter notebooks
│   ├── speech/                  # Speech experiments
│   │   └── data-prep.ipynb
│   ├── text/                    # Text/LLM experiments
│   │   ├── autosoap-ai-powered-clinical-documentation.ipynb
│   │   ├── data-prep.ipynb
│   │   ├── dsail-llm-part_ver1.ipynb
│   │   ├── dsail-llm-part_ver2.ipynb
│   │   └── DSAIL_M2_part1.ipynb
│   └── vision/                  # Vision experiments
│       ├── data-prep.ipynb
│       └── OCR.ipynb
│
└── *.pdf                         # Milestone documentation
```

## Project Milestones

### Milestone 1: Problem Definition & Literature Review
**Due:** October 3  
**Status:** Completed  
[Documentation](https://docs.google.com/document/d/1VsX2NAXAXOAsl_p9jUESoeWp5kDbawq9T37Xr6b8ezw/edit?usp=sharing)

### Milestone 2: Dataset Preparation
**Due:** October 10  
**Status:** Completed  
[Documentation](https://docs.google.com/document/d/1a-ehQkVcbYksfY3MIzB8zWLm-uEAKVIBHDbAvpE6YFw/edit?tab=t.0#heading=h.p1d6hyq4x2hd)

### Milestone 3: Model Selection & Implementation
**Due:** October 17  
**Status:** Completed  
[Documentation](https://docs.google.com/document/d/1VsX2NAXAXOAsl_p9jUESoeWp5kDbawq9T37Xr6b8ezw/edit?usp=sharing)

### Milestone 4: Model Architecture
**Due:** October 31  
**Status:** Completed  
[Documentation](https://docs.google.com/document/d/1cBM4N6kZj-NeLVg-1GqQKxlXfz0wBAkD7524KoNWy7U/edit?tab=t.0#heading=h.p1d6hyq4x2hd)

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
- `Milestone 4 _ DS & AI-Lab-Project - LLM Part.pdf` - Architecture details

## Contributing

This is an academic project for the DSAI Lab course. For questions or contributions, please contact the project team.

## License

This project is part of academic coursework at IIT Madras.

---

**Project Team:** DSAI Lab  
**Institution:** Indian Institute of Technology Madras  
**Last Updated:** November 2024 