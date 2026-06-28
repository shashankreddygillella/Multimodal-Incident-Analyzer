"""
Final integration script for the Multimodal Incident Report Analyzer.

This fixes two common assignment issues:
1. It merges all modality CSVs with pandas.concat, not join.
2. It keeps modality-prefixed Incident_ID values like AUD-001, DOC-001, IMG-001, VID-001, TXT-001.

Run this from the repository root:
    python integration/04_merge_all_modalities.py
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "integration" / "master_incident_report_fixed.csv"

MODALITY_FILES = [
    ("Audio", ROOT / "audio" / "audio_output.csv", "AUD"),
    ("PDF", ROOT / "pdf" / "pdf_output.csv", "DOC"),
    ("Image", ROOT / "images" / "image_output.csv", "IMG"),
    ("Video", ROOT / "video" / "video_output.csv", "VID"),
    ("Text", ROOT / "text" / "text_output.csv", "TXT"),
]

COMMON_COLUMNS = ["Incident_ID", "Source", "Event", "Location", "Time", "Severity", "Details"]

EVENT_CANDIDATES = [
    "Event", "Extracted_Event", "Incident_Type", "Topic", "Scene_Type", "Event_Detected"
]
LOCATION_CANDIDATES = ["Location", "location", "Text_Extracted"]
TIME_CANDIDATES = ["Time", "Date", "Timestamp", "time"]
DETAIL_CANDIDATES = ["Details", "Summary", "Transcript", "Raw_Text", "Objects_Detected"]
SEVERITY_SCORE_CANDIDATES = ["Urgency_Score", "Confidence_Score", "Confidence", "Severity_Score"]


def first_available(row: pd.Series, candidates: list[str], default: str = "N/A") -> str:
    for column in candidates:
        if column in row.index and pd.notna(row[column]) and str(row[column]).strip():
            return str(row[column]).strip()
    return default


def severity_from_score(score) -> str:
    try:
        value = float(score)
    except Exception:
        return "Medium"
    if value > 1:
        value = value / 10
    if value >= 0.70:
        return "High"
    if value >= 0.40:
        return "Medium"
    return "Low"


def normalize_modality(source_name: str, path: Path, prefix: str) -> pd.DataFrame:
    if not path.exists():
        print(f"Missing file skipped: {path}")
        return pd.DataFrame(columns=COMMON_COLUMNS)

    df = pd.read_csv(path)
    rows = []
    for index, row in df.iterrows():
        incident_id = row.get("Incident_ID")
        if pd.isna(incident_id) or not str(incident_id).startswith(prefix + "-"):
            incident_id = f"{prefix}-{index + 1:03d}"

        severity = row.get("Severity")
        if pd.isna(severity) or not str(severity).strip():
            score = first_available(row, SEVERITY_SCORE_CANDIDATES, default="0.5")
            severity = severity_from_score(score)

        rows.append({
            "Incident_ID": str(incident_id),
            "Source": source_name,
            "Event": first_available(row, EVENT_CANDIDATES),
            "Location": first_available(row, LOCATION_CANDIDATES),
            "Time": first_available(row, TIME_CANDIDATES),
            "Severity": str(severity),
            "Details": first_available(row, DETAIL_CANDIDATES),
        })
    return pd.DataFrame(rows, columns=COMMON_COLUMNS)


def main() -> None:
    merged_parts = [normalize_modality(source, path, prefix) for source, path, prefix in MODALITY_FILES]
    master_df = pd.concat(merged_parts, ignore_index=True)
    master_df = master_df.fillna("N/A")
    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    master_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved fixed master dataset to {OUTPUT_PATH}")
    print(f"Total records: {len(master_df)}")
    print(master_df.head(10))


if __name__ == "__main__":
    main()
