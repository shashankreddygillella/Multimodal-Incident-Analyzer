# Integration Fix

This folder adds the missing final integration script.

## Files

- `04_merge_all_modalities.py` merges audio, PDF, image, video, and text outputs into `master_incident_report_fixed.csv`.
- `streamlit_dashboard.py` shows a simple dashboard/query interface.

## How to run

From the repository root:

```bash
python audio/01_audio_modality.py
python images/01_image_modality.py
python video/01_video_modality.py
python integration/04_merge_all_modalities.py
streamlit run integration/streamlit_dashboard.py
```

The final file will be:

```text
integration/master_incident_report_fixed.csv
```
