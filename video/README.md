# Video Modality

This folder completes the Video Analyst role.

## What it produces
`video_output.csv` with:

- `Incident_ID`
- `Timestamp`
- `Frame_ID`
- `Event_Detected`
- `Objects`
- `Confidence`
- `Source`
- `Event`
- `Location`
- `Time`
- `Severity`
- `Details`

## How to run

```bash
python video/01_video_modality.py
```

Optional: place `.mp4`, `.avi`, `.mov`, `.mkv`, `.mpg`, or `.mpeg` files inside `video/data/`. If OpenCV and YOLOv8 are installed, the script extracts frames and detects activity. If no videos are found, it creates demo rows so the full pipeline still works.
