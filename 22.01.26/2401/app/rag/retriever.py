import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List


class Retriever:
    def __init__(self, vector_store, model_name="all-MiniLM-L6-v2"):
        self.vector_store = vector_store
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.vector_store.index.search(
            query_embedding, top_k
        )

        results = []
        for idx in indices[0]:
            if idx < len(self.vector_store.text_chunks):
                results.append(self.vector_store.text_chunks[idx])

        return results
