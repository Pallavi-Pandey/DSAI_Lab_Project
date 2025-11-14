

## Milestone 5: Model Evaluation & Analysis

---
# Text Processing Part

## Overview / Objective
This milestone covers the detailed evaluation  early performance analysis for the core modules responsible for clinical documentation and layperson-friendly summarization.

Link to previous milestone: Milestone 4 included a lot of the outputs expected in this milestone. They have been retained and edited for clarity.  Since the model was scalable, no re-training or fine tuning was done post Milestone 4.


## Evaluation Setup

- Follows the typical recommendation for LLM evaluation
- 50% of the available samples were used for training
- Trained model stored and reloaded for evaluation
- The loaded model can do on-demand inference
- Detailed metrics were collected both for train set and test set
- For extensibility, the predictions were stored along with references, and metrics were produced from the files

## Performance Metrics

The typical quantitative metrics for a Summarization module are ROUGE-L and BERT. 

- ROUGE-L (a variant of ROGUE) measures quality of the summaries by looking at the longest common subsequence between the prediction and reference. A strong model could produce a score in the range of 0.3 to 0.4
- BERTscore is produced by running a BERT model on the prediction and reference. It considers the *semantic similarity* between the reference and prediction. Of course, BERT considers the context of the words. A strong model could produce scores above 0.9

 - We also used the NaN percentage as a measure. These are the number of summaries which were basically a repetition of the prompt. 

- Some more qualitative metrics like Medical_Retain and Hallucination_Rate were also tried


## Training loss 
This was not shared in Milestone 4. With the chosen hyperparams, the loss stabilized around 0.5 after 3 epochs. More epochs did not reduce the loss significantly.

<img width="611" height="285" alt="image" src="https://github.com/user-attachments/assets/f2f10d5b-1b6c-4018-acc3-7fb86fb1df92" />



## Quantitative Results
A good practice in LLM is to compare the metrics with the train and test sets. The metrics are very similar for these two, suggesting the that fine tuning has not overfitted the model. 

- By using various batch sizes, the NaN rate was significantly reduced for the same finetuned model.  From about 43% in the initial run, it has come down to a negligible value.

- ROUGE-L and BERTscore are quite similar between train and test - a good thing. However they are a bit below 'strong model' numbers. For the scope of this project, this is acceptable. 

- Initial numbers reported in milestone 4

|Metric		| Train  	| 	Test |
| :---- | :---- | :---- |
| Total | 471.000000 |472.000000|
| Valid |279.000000 |265.000000 |
|NaN_rate| 0.407643 | 0.438559|
| ROUGE-L | 0.237754 | 0.232926 |
| BERTScore_F1 | 0.876159 | 0.875688 |
| Medical_Retain  | 0.434783 | 0.645161 |
| Hallucination_rate | 0.007168 | 0.007547 |
|  |  |    |


- Numbers after batch and inference tuning

|Metric		| Train  	| 	Test |
| :---- | :---- | :---- |
| Total | 471.000000 |472.000000|
| Valid |467.000000 |467.000000 |
|NaN_rate| 0.008493  |  0.0105939|
| ROUGE-L | 0.245156 |   0.239800 |
| BERTScore_F1 | 0.878474  |  0.877470 |
| Medical_Retain  | 0.487179  |    0.613636 |
| Hallucination_rate | 0.010707 |   0.010707 |
|  |  |  |


## Qualitative Results

- For this model, this was done manually
- For many samples, references and predictions are similar
- There are a few samples with a glaring difference 
- In the most colourful example, the term 'pull-out' was interpreted very differently in reference and prediction

## Error Analysis

To be further explored

## Limitations
- Long inputs and aggressive prompt stripping caused blank outputs
- Some missing assessment/plan fields in raw data necessitated better filtering
- GPU memory limits constrained batch size and context, impacting completeness



## Notes for Next Milestone

- Further tuning to optimize context size and batch handling
- Plan thorough error analysis, and other evaluation methods for final report

## Model Artifacts
- Model Inference Code available as separate notebook (uses finetuned model loaded to Kaggle)
- Predictions for train and test sets

---
---

# Speech Processing Part (ASR)

## Overview / Objective
This milestone reports the evaluation of the Speech (ASR) component that feeds the role-aware LLM pipeline. We assess Whisper Small performance on clinical-style audio using standard ASR metrics and summarize qualitative findings, limitations, and next steps.

## Evaluation Setup

- Data: Clinical-style conversational audio (doctor/patient). See: notebooks/speech/data-prep.ipynb
- Runtime: Single GPU (T4-class) or CPU for small batches
- Model: Whisper Small (openai/whisper-small) with WhisperProcessor
- Decoding: Greedy/beam search (timestamps disabled). Language: English; task="transcribe"
- Normalization for metrics: lowercasing, punctuation removal, whitespace normalization (consistent across refs/preds)

## Performance Metrics

- Word Error Rate (WER) — primary metric for ASR
- Character Error Rate (CER) — useful when words are short or domain terms are frequent
- Optional: Entity/term accuracy on a curated list of medical terms (manual/regex)

## Quantitative Results (Placeholder schema)

- Report WER/CER per split (Train/Val/Test) and by audio condition when available (clean vs noisy)
- Example table structure:

| Metric | Train | Val | Test |
| :-- | --: | --: | --: |
| WER | 0.21 | 0.24 | 0.26 |
| CER | 0.12 | 0.14 | 0.15 |

Notes:
- Insert actual numbers after running evaluation cells in notebooks/speech/data-prep.ipynb
- Keep normalization consistent for fair comparison

## Qualitative Results

- Clean audio: transcripts generally accurate and readable
- Challenging audio: frequent errors on drug names and diagnoses; rapid speech and overlaps degrade performance
- Common error types:
  - Substitutions near medical terminology
  - Dropped short words in fast speech
  - Mis-segmentation when long utterances are not chunked

## Error Analysis

- By category: environment (noise/reverb), speaker (rate/accent), content (domain vocabulary)
- Analyze per-utterance WER distribution to identify tail cases
- Check effect of decoding settings (greedy vs small beam) and chunk/stride for long audio

## Limitations

- No diarization/role attribution in ASR (role handled by UI selection in downstream LLM)
- Domain vocabulary not specialized (no lexicon biasing)
- Hardware constraints limit batch size and long-context decoding

## Notes for Next Iteration

- Explore light fine-tuning on in-domain clips to reduce WER on medical terms
- Add domain lexicon/pronunciation hints, improved text normalization
- Consider diarization or turn-taking detection for cleaner transcripts
- Evaluate augmentation (noise/time/freq masking) for robustness

## Artifacts

- Evaluation notebook: notebooks/speech/data-prep.ipynb
- Saved predictions and references (CSV/JSON) per split
- Decoding configs used for reported metrics

## Integration Reminder

- Downstream flow remains role-aware:
  - Input (speech/text) → (If speech) Whisper transcript → Role selection (Doctor/Patient) → LLM prompt → Output
- ASR quality directly affects both Doctor Assist (SOAP/counseling) and Patient Assist (plain-language guidance)
