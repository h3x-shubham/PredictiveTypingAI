from pathlib import Path

CLEANED_PATH=Path(__file__).resolve().parents[1] / "Data" / "sherlock_cleaned.txt"

def load_cleaned_text(path: Path = CLEANED_PATH) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()
    
def tokenize(text: str) -> list[str]:
    return text.split()

def main():
    print("Loading cleaned text...")
    cleaned=load_cleaned_text()
    print("500 characters of cleaned text:",cleaned[:500])
    print(f"Cleaned Text Length: {len(cleaned)} characters")
    
    print("Tokenizing text...")
    words=tokenize(cleaned)
    print("First 50 tokens:",words[:50])
    print(f"Total number of tokens: {len(words)}")
    
if __name__=="__main__":
    main()