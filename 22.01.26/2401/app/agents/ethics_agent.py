from typing import Dict, Any
from models.schemas import ThesisDraft, ValidationReport


def check_chapter_ethics(chapter_draft) -> Dict[str, Any]:
    """
    Check individual chapter for ethical issues.
    """

    issues = []

    draft_text = (
        str(chapter_draft.draft).lower()
        if hasattr(chapter_draft, "draft")
        else ""
    )

    # Check plagiarism indicators
    plagiarism_indicators = [
        "copied from",
        "taken from",
        "directly from",
        "verbatim",
        "word for word"
    ]

    for indicator in plagiarism_indicators:
        if indicator in draft_text:
            issues.append("Potential plagiarism detected")
            break

    # Check content length
    if len(draft_text.strip()) < 300:
        issues.append("Draft content is too short")

    status = "approved" if len(issues) == 0 else "flagged"

    return {
        "chapter_title": chapter_draft.chapter_title,
        "status": status,
        "issues": issues,
        "ethical_score": max(0, 100 - (len(issues) * 20))
    }


def generate_ethics_recommendations(
    chapter_ethics,
    validation_report
):
    recommendations = []

    for chapter in chapter_ethics:
        if chapter["issues"]:
            recommendations.extend(chapter["issues"])

    if not recommendations:
        recommendations.append(
            "No ethical concerns detected."
        )

    return recommendations


def ethics_agent(
    thesis_draft: ThesisDraft,
    validation_report: ValidationReport
) -> Dict[str, Any]:

    chapter_ethics = []

    approved_chapters = 0
    total_issues = 0

    for chapter_draft in thesis_draft.chapter_drafts:

        result = check_chapter_ethics(
            chapter_draft
        )

        chapter_ethics.append(result)

        if result["status"] == "approved":
            approved_chapters += 1

        total_issues += len(result["issues"])

    avg_ethical_score = (
        sum(
            item["ethical_score"]
            for item in chapter_ethics
        ) / len(chapter_ethics)
        if chapter_ethics
        else 100
    )

    if avg_ethical_score >= 80:
        overall_status = "approved"
    elif avg_ethical_score >= 60:
        overall_status = "flagged"
    else:
        overall_status = "rejected"

    return {
        "topic": thesis_draft.topic,
        "total_chapters": thesis_draft.total_chapters,
        "chapters_approved": approved_chapters,
        "total_issues": total_issues,
        "overall_status": overall_status,
        "ethical_score": round(avg_ethical_score, 2),
        "chapter_ethics": chapter_ethics,
        "recommendations": generate_ethics_recommendations(
            chapter_ethics,
            validation_report
        ),
        "clearance_status": (
            "ready_for_output"
            if avg_ethical_score >= 80
            else "needs_revision"
        )
    }

