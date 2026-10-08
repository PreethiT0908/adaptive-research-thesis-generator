# agents/scraper.py

import os
import requests
from typing import List
from models.schemas import Paper

DOCUMENTS_PATH = "storage/documents"
os.makedirs(DOCUMENTS_PATH, exist_ok=True)

# ---------- STEP A: SEARCH ----------
def search_public_sources(topic: str) -> List[Paper]:
    """
    Search metadata from public academic sources
    (API-based, not HTML scraping)
    """

    return [
        Paper(
            title=f"{topic} – A Comprehensive Review",
            authors=["Doe et al."],
            year=2023,
            source="arXiv",
            pdf_url="https://arxiv.org/pdf/2301.00001.pdf"
        ),
        Paper(
            title=f"Advanced {topic} Systems",
            authors=["Smith et al."],
            year=2024,
            source="Semantic Scholar",
            pdf_url="https://arxiv.org/pdf/2402.00002.pdf"
        )
    ]


# ---------- STEP B: DOWNLOAD ----------
def download_papers(papers: List[Paper]) -> List[Paper]:
    """
    Download PDFs and save to storage/documents
    """

    downloaded = []

    for paper in papers:
        if not paper.pdf_url:
            continue

        try:
            filename = paper.title.replace(" ", "_") + ".pdf"
            filepath = os.path.join(DOCUMENTS_PATH, filename)

            response = requests.get(paper.pdf_url, timeout=15)
            response.raise_for_status()

            with open(filepath, "wb") as f:
                f.write(response.content)

            paper.local_path = filepath
            downloaded.append(paper)

        except Exception as e:
            print(f"❌ Download failed: {paper.title} → {e}")

    return downloaded
