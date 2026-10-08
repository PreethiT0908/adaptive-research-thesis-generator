import re
from typing import List


def rag_agent(query: str, retrieved_chunks: List[str]) -> List[str]:
    """
    Selects relevant chunks based on query.

    If no exact substring matches are found, we fall back to
    keyword overlap, and finally return all chunks instead of
    returning an empty result.
    """
    if not retrieved_chunks:
        return []

    normalized_query = query.lower().strip()
    if not normalized_query:
        return retrieved_chunks

    direct_matches = [
        chunk for chunk in retrieved_chunks
        if normalized_query in chunk.lower()
    ]
    if direct_matches:
        return direct_matches

    query_terms = set(re.findall(r"\w+", normalized_query))
    if not query_terms:
        return retrieved_chunks

    keyword_matches = []
    for chunk in retrieved_chunks:
        chunk_terms = set(re.findall(r"\w+", chunk.lower()))
        if query_terms & chunk_terms:
            keyword_matches.append(chunk)

    return keyword_matches or retrieved_chunks