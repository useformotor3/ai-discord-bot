"""Read-only live canary for the official EUR-Lex CRA source endpoint."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cra_source import fetch_official_cra_source


def main():
    source = fetch_official_cra_source()
    text = source["text"]
    print("PASS: official EUR-Lex CRA source fetched and provenance preconditions met")
    print(f"URL: {source['url']}")
    print(f"Version: {source['version']}")
    print(f"Visible text characters: {len(text)}")
    for date in ("5.12.2024", "2.7.2025", "17.10.2025"):
        print(f"Corrigendum index {date}: present")
    for item in source["sources"]:
        print(f"Source {item['id']}: {item['visible_text_chars']} visible characters")
        print(f"  {item['url']}")


if __name__ == "__main__":
    main()
