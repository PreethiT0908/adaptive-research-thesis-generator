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
