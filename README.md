# Multimodal Incident Report Analyzer

A prototype AI pipeline that processes unstructured incident data from multiple sources and converts it into a structured incident report dataset.

## Group Info

* Course: Gen AI and Applications
* Project: Multimodal Crime / Incident Report Analyzer
* Modalities Covered: Audio, PDF Documents, Images, Video, Text / NLP, Integration & Dashboard

## Project Structure

```text
multimodal-incident-analyzer/
├── audio/
│   ├── 01_audio_modality.py
│   ├── audio_output.csv
│   └── README.md
├── pdf/
│   ├── 01_pdf_modality.ipynb
│   ├── police_report.pdf
│   └── pdf_output.csv
├── images/
│   ├── 01_image_modality.py
│   ├── image_output.csv
│   └── README.md
├── video/
│   ├── 01_video_modality.py
│   ├── video_output.csv
│   └── README.md
├── text/
│   ├── 02_text_modality.ipynb
│   ├── crimereport.csv
│   └── text_output.csv
├── integration/
│   ├── 03_integration_dashboard.ipynb
│   ├── 04_merge_all_modalities.py
│   ├── streamlit_dashboard.py
│   ├── master_incident_report.csv
│   └── master_incident_report_fixed.csv
├── docs/
│   ├── architecture_diagram.md
│   └── project_report_missing_sections.md
├── requirements.txt
└── README.md
```

## Final Dataset

The final merged structured dataset is available here:

`integration/master_incident_report_fixed.csv`

This file combines the outputs from all five modalities: audio, PDF, images, video, and text.

## AI Pipeline

```text
Audio Files      → Speech/Text Analysis       → audio_output.csv
PDF Reports      → PDF Extraction + NLP       → pdf_output.csv
Images           → Object/Scene Analysis      → image_output.csv
Videos           → Frame/Event Detection      → video_output.csv
Text Reports     → NLP + Sentiment Analysis   → text_output.csv
                                                ↓
                                Final Integration with pandas.concat
                                                ↓
                          master_incident_report_fixed.csv
                                                ↓
                                  Streamlit Dashboard / Query View
```

## Tools Used

| Modality    | Tools                                       |
| ----------- | ------------------------------------------- |
| Audio       | Speech-to-text logic, pandas                |
| PDF         | pdfplumber, spaCy, pandas                   |
| Images      | Object/scene detection logic, pandas        |
| Video       | OpenCV-style frame/event processing, pandas |
| Text / NLP  | spaCy, HuggingFace Transformers, pandas     |
| Integration | pandas, Streamlit                           |

## Output Schema

| Incident_ID | Source              | Event                    | Location     | Time       | Severity |
| ----------- | ------------------- | ------------------------ | ------------ | ---------- | -------- |
| AUD-001     | Audio               | Emergency / Fire         | Downtown Ave | 14:32      | High     |
| DOC-001     | PDF Document        | Police / Incident Report | Arkansas     | 2015-04-10 | Medium   |
| IMG-001     | Image               | Fire Scene               | Main St      | N/A        | High     |
| VID-001     | Video               | CCTV Motion Event        | N/A          | 00:00:12   | Medium   |
| TXT-001     | Text / Social Media | Theft / Robbery          | Oak Street   | Unknown    | High     |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run individual modality scripts/notebooks:

```bash
python audio/01_audio_modality.py
python images/01_image_modality.py
python video/01_video_modality.py
```

Run the final integration script:

```bash
python integration/04_merge_all_modalities.py
```

Run the dashboard:

```bash
streamlit run integration/streamlit_dashboard.py
```

## Deliverables

* Architecture Diagram: `docs/architecture_diagram.md`
* Final Dataset: `integration/master_incident_report_fixed.csv`
* Dashboard Code: `integration/streamlit_dashboard.py`
* Project Report Sections: `docs/project_report_missing_sections.md`
* Demo Video Link: Add Google Drive link here

## Summary

This project demonstrates how multimodal unstructured data can be processed using AI and data engineering techniques. Each modality produces a structured output, and the integration component merges all outputs into one final incident report dataset using modality-prefixed IDs such as AUD, DOC, IMG, VID, and TXT.
