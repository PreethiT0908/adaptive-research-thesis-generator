from pydantic import BaseModel
from typing import List, Optional




# =============================
# Agent 1: User Profile
# =============================
class UserProfile(BaseModel):
    degree: str
    university: str
    discipline: str
    topic: str
    target_journal: Optional[str] = None


# =============================
# Agent 1 Output: Research Policy
# =============================
class ResearchPolicy(BaseModel):
    expected_pages: str
    rigor_level: str
    structure: List[str]


# =============================
# Agent 2: Blueprint
# =============================
class ChapterBlueprint(BaseModel):
    chapter_title: str
    objective: str
    subtopics: List[str]


class ResearchBlueprint(BaseModel):
    total_chapters: int
    chapters: List[ChapterBlueprint]


# =============================
# Agent 3: Search Agent Schemas
# =============================
class SearchQuery(BaseModel):
    query_text: str
    chapter: str
    intent: str


class SearchResult(BaseModel):
    chapter: str
    query: str
    sources: List[str]


# =============================
# Agent 4: RAG Agent Schemas
# =============================
class RagMatch(BaseModel):
    chunk_text: str
    relevance_score: Optional[float] = None


class RagResult(BaseModel):
    query_text: str
    matched_chunks: List[RagMatch]


# =============================
# Search / Paper Schema
# =============================
class Paper(BaseModel):
    title: str
    authors: List[str]
    year: Optional[int] = None
    source: Optional[str] = None
    pdf_url: Optional[str] = None
    local_path: Optional[str] = None


# =============================
# Agent 5: Drafting Agent Schemas
# =============================
class ChapterDraft(BaseModel):
    chapter_title: str
    objective: str
    subtopics: List[str]
    draft: str
    evidence_sources: List[str]


class ThesisDraft(BaseModel):
    total_chapters: int
    topic: str
    chapter_drafts: List[ChapterDraft]
    status: str


# =============================
# Agent 6: Validation Agent Schemas
# =============================
class ChapterValidation(BaseModel):
    chapter_title: str
    status: str
    issues: List[str]
    evidence_count: int
    draft_length: int


class ValidationReport(BaseModel):
    topic: str
    total_chapters: int
    chapters_passed: int
    total_issues: int
    overall_status: str
    chapter_validations: List[ChapterValidation]
    recommendations: List[str]


# =============================
# Agent 7: Ethics Agent Schemas
# =============================
class ChapterEthics(BaseModel):
    chapter_title: str
    status: str
    issues: List[str]
    ethical_score: float


class EthicsReport(BaseModel):
    topic: str
    total_chapters: int
    chapters_approved: int
    total_issues: int
    overall_status: str
    ethical_score: float
    chapter_ethics: List[ChapterEthics]
    recommendations: List[str]
    clearance_status: str


# =============================
# Agent 8: Revision Agent Schemas
# =============================
class ChapterRevision(BaseModel):
    chapter_title: str
    revision_needed: bool
    recommendations: List[str]
    proposed_revision: str


class RevisionReport(BaseModel):
    topic: str
    total_chapters: int
    chapters_requiring_revision: int
    overall_status: str
    chapter_revisions: List[ChapterRevision]
    recommendations: List[str]


# =============================
# Agent 9: Output Agent Schemas
# =============================
class OutputReport(BaseModel):
    topic: str
    total_chapters: int
    status: str
    message: str
    generated_file: Optional[str] = None
    content_preview: Optional[str] = None