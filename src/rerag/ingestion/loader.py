from pathlib import Path
import fitz

def load_pdf(file_path: str | Path) -> list[dict]:
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() != "pdf":
        raise ValueError(f"Unsupported file type: {file_path.suffix}")

    pages = []

    with fitz.open(file_path) as document:
        for page_index, page in enumerate(document):
            text = page.get_text("text")

            if not text.strip():
                continue

            pages.append(
                {
                    "text": text,
                    "metadata": {
                        "filename": file_path.name,
                        "source": str(file_path),
                        "page": page_index + 1
                    }
                }
            )

    return pages
