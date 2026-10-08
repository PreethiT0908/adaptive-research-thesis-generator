from agents.rag_agent import rag_agent


def main():
    # Minimal demo chunks so this runs without external deps
    sample_chunks = [
        "Retrieval augmented generation (RAG) combines retrieval with generation.",
        "This chunk discusses embeddings and FAISS vector stores.",
        "Another section about thesis generation and academic search strategies.",
        "Details on evaluation metrics and experimental setup."
    ]

    query = input("Query (default 'retrieval'): ").strip()
    if not query:
        query = "retrieval"

    results = rag_agent(query, sample_chunks)

    print("\n--- RAG Agent Results ---")
    if results:
        for r in results:
            print(f"- {r}")
    else:
        print("No relevant chunks found.")


if __name__ == "__main__":
    main()
