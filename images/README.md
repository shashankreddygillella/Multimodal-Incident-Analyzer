# Image Modality

This folder completes the Image Analyst role.

## What it produces
`image_output.csv` with:

- `Incident_ID`
- `Image_ID`
- `Scene_Type`
- `Objects_Detected`
- `Text_Extracted`
- `Confidence_Score`
- `Source`
- `Event`
- `Location`
- `Time`
- `Severity`
- `Details`

## How to run

```bash
python images/01_image_modality.py
```

Optional: place image files inside `images/data/`. If YOLOv8 and pytesseract are installed, the script analyzes them. If no images are found, it creates demo rows so the full pipeline still works.
