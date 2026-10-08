# Adaptive Thesis Generator

## Overview

Adaptive Thesis Generator is a multi-agent AI system designed to automate the research thesis generation workflow.

The system uses specialized agents that collaborate to:

* Understand the user's research profile
* Create a thesis structure
* Search for relevant research sources
* Build a knowledge base using RAG (Retrieval-Augmented Generation)
* Generate thesis content
* Validate research quality
* Check ethical compliance
* Revise and improve drafts
* Export the final thesis

---

## Current Agent Pipeline

```text
User Input
    ↓
Profile Agent
    ↓
Blueprint Agent
    ↓
Search Agent
    ↓
RAG Agent
    ↓
Drafting Agent (Upcoming)
    ↓
Validation Agent (Upcoming)
    ↓
Ethics Agent (Upcoming)
    ↓
Revision Agent (Upcoming)
    ↓
Output Agent (Upcoming)
```

---

## Project Structure

```text
adaptive-thesis-generator/

├── app/
│
├── agents/
│   ├── profile_agent.py
│   ├── blueprint_agent.py
│   ├── search_agent.py
│   ├── rag_agent.py
│   ├── drafting_agent.py
│   ├── validation_agent.py
│   ├── ethics_agent.py
│   ├── revision_agent.py
│   └── output_agent.py
│
├── graph/
│   └── thesis_graph.py
│
├── rag/
│   ├── ingest.py
│   ├── chunker.py
│   ├── vector_store.py
│   └── retriever.py
│
├── models/
│   └── schemas.py
│
├── config/
│   └── public_sources.py
│
├── storage/
│   ├── documents/
│   ├── vectors/
│   └── outputs/
│
├── main.py
├── streamlit.py
├── requirements.txt
└── README.md
```

---

## Agent Descriptions

### Agent 1: Profile Agent

Collects research information from the user.

Input:

* Degree
* University
* Discipline
* Topic
* Target Journal

Output:

* Research Policy

---

### Agent 2: Blueprint Agent

Generates thesis structure.

Output:

* Chapters
* Objectives
* Subtopics

Example:

* Abstract
* Introduction
* Related Work
* Methodology
* Results
* Conclusion
* References

---

### Agent 3: Search Agent

Responsible for finding knowledge sources.

Search strategy:

#### Internal Documents

Searches:

```text
storage/documents/
```

for uploaded PDFs.

#### Public Sources

Uses academic repositories:

* Google Scholar
* arXiv
* Semantic Scholar
* CORE
* DOAJ
* PubMed Central
* SSRN
* Zenodo
* NDLI
* IEEE Xplore
* DU e-Journal

Output:

* Research papers
* URLs
* Metadata

---

### Agent 4: RAG Agent

Creates the knowledge base.

Workflow:

```text
PDF Documents
      ↓
Load PDFs
      ↓
Chunk Documents
      ↓
Generate Embeddings
      ↓
FAISS Vector Database
      ↓
Retrieve Relevant Chunks
```

Output:

* Relevant context for thesis generation

---

## Internal Knowledge Base

Place PDFs inside:

```text
app/storage/documents/
```

Example:

```text
climate_change.pdf
fuel_cells.pdf
machine_learning.pdf
computer_science.pdf
```

These PDFs will be processed by the RAG pipeline.

---

## Public Knowledge Sources

Configured in:

```python
app/config/public_sources.py
```

Example:

```python
PUBLIC_SOURCES = {
    "google_scholar": "https://scholar.google.com",
    "arxiv": "https://arxiv.org",
    "semantic_scholar": "https://api.semanticscholar.org",
    "core": "https://core.ac.uk",
    "doaj": "https://doaj.org",
    "pubmed_central": "https://www.ncbi.nlm.nih.gov/pmc",
    "ssrn": "https://www.ssrn.com",
    "zenodo": "https://zenodo.org",
    "ndli": "https://ndl.iitkgp.ac.in",
    "ieee": "https://ieeexplore.ieee.org",
    "du_ejournal": "https://journals.du.ac.in"
}
```

---

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Command-Line Version

```bash
python main.py
```

---

## Running Streamlit UI

```bash
streamlit run streamlit.py
```

Application URL:

```text
http://localhost:8501
```

---

## Example Workflow

User Input:

```text
Degree: UG
University: Anna University
Discipline: Fuel Cells
Topic: Fuel Cells
Target Journal: IEEE
```

System Process:

```text
Profile Agent
    ↓
Blueprint Agent
    ↓
Search Agent
    ↓
RAG Agent
```

Output:

```text
Research Policy
Research Blueprint
Research Sources
Knowledge Base Chunks
```

---

## Future Enhancements

* Semantic Scholar API Integration
* Google Scholar Integration
* Automatic PDF Downloading
* Hybrid Search
* LangGraph Agent Orchestration
* LLM-Based Draft Generation
* Automatic Citation Generation
* Thesis PDF Export
* Multi-language Support
* Research Gap Detection

---

## Current Status

Completed:

* Profile Agent
* Blueprint Agent
* Search Agent
* Initial RAG Agent

In Progress:

* FAISS Integration
* Retrieval Pipeline

Upcoming:

* Drafting Agent
* Validation Agent
* Ethics Agent
* Revision Agent
* Output Agent

```
```
