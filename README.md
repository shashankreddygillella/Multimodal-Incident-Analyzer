# Multimodal Incident Report Analyzer

A prototype AI pipeline that processes unstructured data from multiple sources and converts it into a structured incident report dataset.

## Group Info
- **Course:** Gen AI and Applications
- **Modalities Covered:** PDF Documents, Text / NLP, Integration & Dashboard

## Project Structure

```
multimodal-incident-analyzer/
├── pdf/
│   ├── 01_pdf_modality.ipynb       # PDF extraction notebook
│   ├── police_report.pdf           # Input dataset (download from MuckRock)
│   └── pdf_output.csv              # Generated output
├── text/
│   ├── 02_text_modality.ipynb      # NLP analysis notebook
│   ├── crimereport.csv             # Input dataset (download from Kaggle)
│   └── text_output.csv             # Generated output
├── integration/
│   ├── 03_integration_dashboard.ipynb  # Merge + dashboard notebook
│   ├── master_incident_report.csv      # Final merged dataset
│   └── dashboard.png                   # Dashboard visualization
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download datasets:
   - **PDF:** https://www.muckrock.com (Arkansas Police 1033 PDF) → save as `pdf/police_report.pdf`
   - **Text:** https://www.kaggle.com/datasets/cameliasiadat/crimereport → save as `text/crimereport.csv`

3. Run notebooks **in order:**
   - `01_pdf_modality.ipynb`
   - `02_text_modality.ipynb`
   - `03_integration_dashboard.ipynb`

## AI Pipeline

```
[PDF Input]      → pdfplumber + spaCy NER  → pdf_output.csv  ─┐
                                                                ├─→ master_incident_report.csv → Dashboard
[Text CSV Input] → spaCy + HuggingFace     → text_output.csv ─┘
```

## Tools Used

| Modality    | Tools                                      |
|-------------|--------------------------------------------|
| PDF         | pdfplumber, spaCy (NER)                    |
| Text / NLP  | spaCy, HuggingFace Transformers (DistilBERT)|
| Integration | pandas, matplotlib                          |

## Output Schema

| Incident_ID | Source | Event | Location | Time | Severity |
|-------------|--------|-------|----------|------|----------|
| INC_001     | PDF Document | Training / Equipment | Arkansas | 2015-04-10 | Low |
| INC_002     | Text / Social Media | Theft / Robbery | Oak Street | Unknown | High |
