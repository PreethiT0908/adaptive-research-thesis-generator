from typing import List


def rag_agent(query: str, retrieved_chunks: List[str]) -> List[str]:
    """
    Selects relevant chunks based on query
    """
    return [
        chunk for chunk in retrieved_chunks
        if query.lower() in chunk.lower()
    ]