from typing import Dict, List, Any
from models.schemas import ResearchBlueprint
from models.schemas import ThesisDraft
from services.llm_client import generate_text

def drafting_agent(blueprint, rag_results_by_chapter, topic):
    drafts = []

    for chapter in blueprint.chapters:
        chapter_title = chapter.chapter_title

        content = rag_results_by_chapter.get(chapter_title, [])

        prompt = f"""
You are an expert thesis writer.

Research Topic:
{topic}

Current Chapter:
{chapter_title}

Chapter Objective:
{chapter.objective}

Available Research Evidence:
{content}

IMPORTANT RULES:

1. Focus ONLY on the topic "{topic}".
2. Do NOT explain what an abstract, introduction, methodology, or conclusion is.
3. Write the actual chapter content for the thesis.
4. Use formal academic writing.
5. Include headings and subheadings.
6. Minimum 500 words.
7. Relate every paragraph to "{topic}".
8. Ignore unrelated research titles if they do not match the topic.

Generate a complete thesis chapter.
"""

        try:
            draft_text = generate_text(prompt)

            if not draft_text or len(draft_text.strip()) < 100:
                draft_text = f"""
# {chapter_title}

This chapter discusses {topic}.
Additional content generation is required.
"""

        except Exception as e:
            draft_text = f"Generation Error: {str(e)}"

        drafts.append({
            "chapter_title": chapter_title,
            "objective": chapter.objective,
            "subtopics": chapter.subtopics,
            "draft": draft_text,
            "evidence_sources": content
        })

    return {
        "topic": topic,
        "total_chapters": len(blueprint.chapters),
        "status": "generated",
        "chapter_drafts": drafts
    }