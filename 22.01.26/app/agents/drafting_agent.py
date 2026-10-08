def draft_section(chapter: ChapterBlueprint, evidence: List[str], topic: str) -> Dict[str, Any]:
    """Create a draft for a single chapter using blueprint guidance and retrieved evidence."""

    evidence_text = "\n".join(f"- {chunk}" for chunk in evidence) if evidence else "No evidence available."

    draft_content = f"""
{chapter.chapter_title}

Objective:
{chapter.objective}

Introduction

This chapter discusses {topic}. The objective of this chapter is to
{chapter.objective.lower()}.

Subtopics Covered

{chr(10).join(f'- {sub}' for sub in chapter.subtopics)}

Research Evidence

{evidence_text}

Discussion

{topic} is an important research area with significant academic,
industrial, and societal applications. Based on the available
research evidence, several developments have been reported in
this field. Researchers continue to investigate innovative
approaches, challenges, and opportunities associated with
{topic}.

The evidence collected through the retrieval process indicates
that ongoing studies are focused on improving performance,
efficiency, reliability, and practical implementation.

Conclusion

This chapter presented an overview of {chapter.chapter_title}
for the topic {topic}. The collected evidence supports the
research objectives and provides a foundation for further
analysis in subsequent chapters.
"""

    return {
        "chapter_title": chapter.chapter_title,
        "objective": chapter.objective,
        "subtopics": chapter.subtopics,
        "draft": draft_content.strip(),
        "evidence_sources": evidence,
    }
print("DRAFTING AGENT VERSION 2 LOADED")