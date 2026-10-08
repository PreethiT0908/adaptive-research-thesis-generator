from typing import Dict, List, Any
from models.schemas import ThesisDraft, ChapterDraft


def build_chapter_revision_plan(
    chapter_draft: ChapterDraft,
    validation: Dict[str, Any],
    ethics: Dict[str, Any],
) -> Dict[str, Any]:
    """Create a revision plan for a chapter based on validation and ethics feedback."""
    recommendations: List[str] = []
    draft_text = chapter_draft.draft or ""
    draft_lower = draft_text.lower()

    if validation.get("status") != "pass":
        if validation.get("issues"):
            recommendations.append(
                f"Fix validation issues: {'; '.join(validation['issues'])}"
            )
        if validation.get("evidence_count", 0) < 2:
            recommendations.append(
                "Add at least two strong evidence sources to support claims."
            )

    if ethics.get("status") != "approved":
        if ethics.get("issues"):
            recommendations.append(
                f"Resolve ethics issues: {'; '.join(ethics['issues'])}"
            )
        if ethics.get("ethical_score", 100) < 80:
            recommendations.append(
                "Improve neutrality and academic tone to increase the ethical score."
            )

    if not chapter_draft.evidence_sources:
        recommendations.append("Include evidence sources to strengthen academic integrity.")

    if chapter_draft.objective:
        objective_text = chapter_draft.objective.lower().strip()
        if objective_text and objective_text not in draft_lower:
            recommendations.append(
                "Align the chapter draft more closely with the stated objective."
            )

    if not draft_text.strip() or len(draft_text.strip()) < 200:
        recommendations.append(
            "Expand the chapter content with additional explanation, examples, and transitions."
        )

    revision_needed = bool(recommendations)
    proposed_revision = draft_text
    if revision_needed:
        note_block = "\n".join(f"- {item}" for item in recommendations)
        proposed_revision = (
            f"{draft_text}\n\n"
            "[Revision Guidance]" "\n"
            f"{note_block}\n\n"
            "[Suggested revision: address the issues above, cite evidence clearly, and preserve an objective academic tone.]"
        )

    return {
        "chapter_title": chapter_draft.chapter_title,
        "revision_needed": revision_needed,
        "recommendations": recommendations,
        "proposed_revision": proposed_revision,
    }


def compile_revision_recommendations(chapter_revisions: List[Dict[str, Any]]) -> List[str]:
    """Combine chapter-level revision suggestions into an overall revision plan."""
    recommendations: List[str] = []

    for chapter in chapter_revisions:
        if chapter["revision_needed"]:
            if chapter["recommendations"]:
                recommendations.append(
                    f"Revise {chapter['chapter_title']}: {chapter['recommendations'][0]}"
                )
            else:
                recommendations.append(
                    f"Review {chapter['chapter_title']} for additional improvements."
                )

    return recommendations or ["No revision required at this time."]


def revision_agent(
    thesis_draft: ThesisDraft,
    validation_report: Dict[str, Any],
    ethics_report: Dict[str, Any],
) -> Dict[str, Any]:
    """Generate a revision report for the thesis draft based on validation and ethics feedback."""
    validation_by_title = {
        validation["chapter_title"]: validation
        for validation in validation_report.get("chapter_validations", [])
    }
    ethics_by_title = {
        ethics["chapter_title"]: ethics
        for ethics in ethics_report.get("chapter_ethics", [])
    }

    chapter_revisions: List[Dict[str, Any]] = []
    total_revisions = 0

    for chapter in thesis_draft.chapter_drafts:
        validation = validation_by_title.get(chapter.chapter_title, {})
        ethics = ethics_by_title.get(chapter.chapter_title, {})
        revision = build_chapter_revision_plan(chapter, validation, ethics)
        chapter_revisions.append(revision)
        if revision["revision_needed"]:
            total_revisions += 1

    overall_status = "needs_revision" if total_revisions else "approved"

    return {
        "topic": thesis_draft.topic,
        "total_chapters": thesis_draft.total_chapters,
        "chapters_requiring_revision": total_revisions,
        "overall_status": overall_status,
        "chapter_revisions": chapter_revisions,
        "recommendations": compile_revision_recommendations(chapter_revisions),
    }
