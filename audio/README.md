# Audio Modality

This folder completes the Audio Analyst role.

## What it produces
`audio_output.csv` with:

- `Incident_ID`
- `Call_ID`
- `Transcript`
- `Extracted_Event`
- `Location`
- `Sentiment`
- `Urgency_Score`
- `Source`
- `Event`
- `Time`
- `Severity`
- `Details`

## How to run

```bash
python audio/01_audio_modality.py
```

Optional: place `.wav`, `.mp3`, `.m4a`, `.flac`, or `.ogg` files inside `audio/data/`. If Whisper is installed, the script will transcribe them. If no audio files are found, it creates demo rows so the full pipeline still works.
