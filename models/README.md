## Description of two models

### whisper-app
* Finetuned model for Speech Recognition
* First part of the oveall architecture
* Currently takes patient speech and converts to text

## distilled-student-peft-adapter
* Final part of the model architecture
* Finetune Ollama model
* 'Student' model trained using teacher created summaries
* Hosted as HF Spaces
* Inference speed needs improvement
