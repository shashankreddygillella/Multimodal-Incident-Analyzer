# Report Sections

## Final Dataset Quick Reference Link
https://github.com/shashankreddygillella/Multimodal-Incident-Analyzer/tree/main

`integration/master_incident_report_fixed.csv`

## Demo Video Link
https://drive.google.com/file/d/1ePsDW9hTlATfZoq0l6rSekTKV_IqYoaB/view?usp=drive_linkhttps://drive.google.com/file/d/1ePsDW9hTlATfZoq0l6rSekTKV_IqYoaB/view?usp=drive_link


## Individual Contributions

| Name | Role | Contributions |
|---|---|---|
| Meghansh| Audio Analyst | Transcribed emergency audio, extracted event type/location, calculated urgency and sentiment, created audio_output.csv. |
| Meghansh| PDF Analyst | Extracted text from police reports, identified incident fields, created pdf_output.csv. |
| Meghansh| Image Analyst | Detected objects/scenes from images, extracted visible text with OCR, created image_output.csv. |
| SHASHANK | Video Analyst | Extracted video frames, detected motion/events, created timestamped video_output.csv. |
| SHASHANK | Text Analyst | Cleaned crime text, performed NER, sentiment, and topic classification, created text_output.csv. |
| SHASHANK  | Integration Lead | Merged all modality outputs, standardized schema, created final dataset and dashboard. |

## Severity Rule
The project uses a 0 to 1 confidence/urgency scale. Severity is assigned as:

- 0.00 to 0.39 = Low
- 0.40 to 0.69 = Medium
- 0.70 to 1.00 = High

Each modality contributes its own confidence or urgency signal, and the integration script converts it into the final `Severity` field.
