"""
Audio Analyst module for the Multimodal Incident Report Analyzer.

What it does:
1. Loads audio files from audio/data/ if available.
2. Transcribes audio with Whisper when installed.
3. Extracts incident type, location, sentiment, and urgency score.
4. Writes audio/audio_output.csv.

If no audio files are found, it creates a small demo output so the pipeline can run.
"""

from pathlib import Path
import re
import pandas as pd

AUDIO_DIR = Path(__file__).resolve().parent
DATA_DIR = AUDIO_DIR / "data"
OUTPUT_PATH = AUDIO_DIR / "audio_output.csv"

AUDIO_EXTENSIONS = {".wav", ".mp3", ".m4a", ".flac", ".ogg"}

EVENT_KEYWORDS = {
    "Building Fire": ["fire", "smoke", "burning", "flames"],
    "Road Accident": ["accident", "crash", "collision", "hit", "vehicle"],
    "Theft / Robbery": ["robbery", "theft", "stolen", "steal", "burglar"],
    "Medical Emergency": ["injured", "bleeding", "collapsed", "unconscious", "ambulance"],
    "Public Disturbance": ["fight", "fighting", "disturbance", "crowd", "shouting"],
}

URGENCY_TERMS = [
    "help", "urgent", "emergency", "trapped", "bleeding", "fire", "gun", "weapon",
    "unconscious", "critical", "danger", "please", "quick", "hurry"
]

LOCATION_PATTERN = re.compile(
    r"(?:at|on|near|around|by)\s+([A-Z][A-Za-z0-9 .'-]*(?:Street|St\.?|Road|Rd\.?|Avenue|Ave\.?|Drive|Dr\.?|Lane|Ln\.?|Boulevard|Blvd\.?|Park|Mall|School|Hospital|Downtown|Highway|Hwy)?)",
    re.IGNORECASE,
)


def transcribe_audio_file(audio_path: Path) -> str:
    """Transcribe one audio file with Whisper. Returns a fallback message if Whisper is unavailable."""
    try:
        import whisper  # type: ignore
        model = whisper.load_model("base")
        result = model.transcribe(str(audio_path))
        return result.get("text", "").strip()
    except Exception as exc:
        return f"Transcription unavailable for {audio_path.name}. Error: {exc}"


def detect_event(text: str) -> str:
    lower_text = text.lower()
    for event, keywords in EVENT_KEYWORDS.items():
        if any(keyword in lower_text for keyword in keywords):
            return event
    return "Other / Unknown"


def extract_location(text: str) -> str:
    match = LOCATION_PATTERN.search(text)
    if match:
        return match.group(1).strip().rstrip(".,")
    return "N/A"


def score_urgency(text: str) -> float:
    lower_text = text.lower()
    hits = sum(1 for term in URGENCY_TERMS if term in lower_text)
    exclamation_bonus = min(text.count("!"), 3) * 0.08
    score = min(1.0, 0.25 + hits * 0.09 + exclamation_bonus)
    return round(score, 2)


def label_sentiment(urgency_score: float) -> str:
    if urgency_score >= 0.75:
        return "Distressed"
    if urgency_score >= 0.45:
        return "Concerned"
    return "Calm"


def severity_from_score(score: float) -> str:
    if score >= 0.70:
        return "High"
    if score >= 0.40:
        return "Medium"
    return "Low"


def build_rows() -> list[dict]:
    DATA_DIR.mkdir(exist_ok=True)
    audio_files = sorted([p for p in DATA_DIR.iterdir() if p.suffix.lower() in AUDIO_EXTENSIONS])

    if audio_files:
        transcripts = [(f"C{i:03d}", transcribe_audio_file(path)) for i, path in enumerate(audio_files, start=1)]
    else:
        transcripts = [
            ("C001", "There is a fire and people are trapped on the second floor near Downtown Avenue."),
            ("C002", "A car crash happened on Main Street. One person is injured and needs help."),
            ("C003", "Someone stole a wallet near Oak Road. The suspect ran toward the park."),
        ]

    rows = []
    for index, (call_id, transcript) in enumerate(transcripts, start=1):
        event = detect_event(transcript)
        location = extract_location(transcript)
        urgency = score_urgency(transcript)
        sentiment = label_sentiment(urgency)
        rows.append({
            "Incident_ID": f"AUD-{index:03d}",
            "Call_ID": call_id,
            "Transcript": transcript,
            "Extracted_Event": event,
            "Location": location,
            "Sentiment": sentiment,
            "Urgency_Score": urgency,
            "Source": "Audio",
            "Event": event,
            "Time": "N/A",
            "Severity": severity_from_score(urgency),
            "Details": transcript[:200],
        })
    return rows


def main() -> None:
    rows = build_rows()
    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} audio records to {OUTPUT_PATH}")
    print(df[["Incident_ID", "Source", "Event", "Location", "Severity"]].head())


if __name__ == "__main__":
    main()
