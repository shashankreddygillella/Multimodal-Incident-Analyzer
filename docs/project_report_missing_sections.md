# Missing Report Sections to Add

## Final Dataset Quick Reference Link
Add a direct GitHub link to:

`integration/master_incident_report_fixed.csv`

## Demo Video Link
Add your Google Drive viewable link here:

`Demo Video: <paste Google Drive link>`

## Individual Contributions

| Name | Role | Contributions |
|---|---|---|
| Student 1 | Audio Analyst | Transcribed emergency audio, extracted event type/location, calculated urgency and sentiment, created audio_output.csv. |
| Student 2 | PDF Analyst | Extracted text from police reports, identified incident fields, created pdf_output.csv. |
| Student 3 | Image Analyst | Detected objects/scenes from images, extracted visible text with OCR, created image_output.csv. |
| Student 4 | Video Analyst | Extracted video frames, detected motion/events, created timestamped video_output.csv. |
| Student 5 | Text Analyst | Cleaned crime text, performed NER, sentiment, and topic classification, created text_output.csv. |
| Student 6 | Integration Lead | Merged all modality outputs, standardized schema, created final dataset and dashboard. |

## Severity Rule
The project uses a 0 to 1 confidence/urgency scale. Severity is assigned as:

- 0.00 to 0.39 = Low
- 0.40 to 0.69 = Medium
- 0.70 to 1.00 = High

Each modality contributes its own confidence or urgency signal, and the integration script converts it into the final `Severity` field.
