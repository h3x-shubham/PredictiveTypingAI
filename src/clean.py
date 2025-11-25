import re
from pathlib import Path


DATA_PATH=Path(__file__).resolve().parents[1] / "Data" / "sherlock.txt"
CLEANED_PATH=Path(__file__).resolve().parents[1] / "Data" / "sherlock_cleaned.txt"

def load_raw_text(path: Path = DATA_PATH)-> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()
    
def clean_text(text: str) -> str:
    text=text.lower()
    text=re.sub(r"[^a-zA-Z0-9\s\.,;:'\"!?()-]", " ", text)
    text=re.sub(r"\s+", " ", text).strip()
    return text
    
    
def save_cleaned_text(text: str, path: Path = CLEANED_PATH):
    with path.open("w", encoding="utf-8") as f:
        f.write(text)

def main():
    print("Loading raw text...")
    raw=load_raw_text()
    print("500 characters of raw text:",raw[:500])
    print(f"Raw Text Length: {len(raw)} characters")
    
    print("Cleaning text...")
    cleaned=clean_text(raw)
    print("500 characters of cleaned text:",cleaned[:500])
    print(f"Cleaned Text Length: {len(cleaned)} characters")
    
    print("saving cleaned text...")
    save_cleaned_text(cleaned)
    
if __name__ == "__main__":
    main()
    
        