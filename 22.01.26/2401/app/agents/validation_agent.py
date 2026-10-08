from typing import Dict, List, Any
from models.schemas import ThesisDraft, ChapterDraft


def validate_section(chapter_draft: ChapterDraft) -> Dict[str, Any]:
    """
    Clean validation for thesis chapters (robust version)
    """

    issues = []

    draft = chapter_draft.draft or ""

    # 1. Length check
    if len(draft.strip()) < 150:
        issues.append("Draft content is too short")

    # 2. Evidence check
    if not chapter_draft.evidence_sources:
        issues.append("No evidence sources found for this chapter")

    # 3. Objective check (FIXED - no strict matching)
    if chapter_draft.objective:
        objective_keywords = chapter_draft.objective.lower().split()

        match_found = any(
            keyword in draft.lower()
            for keyword in objective_keywords
            if len(keyword) > 4
        )

        if not match_found:
            issues.append("Objective not clearly addressed in draft")

    # 4. Structure check
    if len(draft.split("\n")) < 3:
        issues.append("Poor paragraph structure")

    # Status logic (FIXED)
    if len(issues) == 0:
        status = "pass"
    elif len(issues) <= 2:
        status = "warning"
    else:
        status = "fail"

    return {
        "chapter_title": chapter_draft.chapter_title,
        "status": status,
        "issues": issues,
        "evidence_count": len(chapter_draft.evidence_sources),
        "draft_length": len(draft)
    }


def validation_agent(thesis_draft: ThesisDraft) -> Dict[str, Any]:

    chapter_validations = []
    total_issues = 0
    passed_chapters = 0

    for chapter_draft in thesis_draft.chapter_drafts:

        validation = validate_section(chapter_draft)
        chapter_validations.append(validation)

        if validation["status"] == "pass":
            passed_chapters += 1

        total_issues += len(validation["issues"])

    # FIXED overall logic
    if total_issues == 0:
        overall_status = "pass"
    elif total_issues <= 5:
        overall_status = "warning"
    else:
        overall_status = "fail"

    return {
        "topic": thesis_draft.topic,
        "total_chapters": thesis_draft.total_chapters,
        "chapters_passed": passed_chapters,
        "total_issues": total_issues,
        "overall_status": overall_status,
        "chapter_validations": chapter_validations,
        "recommendations": generate_recommendations(chapter_validations)
    }


def generate_recommendations(validations: List[Dict]) -> List[str]:

    recommendations = []

    for v in validations:

        if v["status"] == "fail":
            recommendations.append(
                f"Rewrite {v['chapter_title']} with clearer explanation and more content"
            )

        elif v["evidence_count"] < 2:
            recommendations.append(
                f"Add more research evidence in {v['chapter_title']}"
            )

    if not recommendations:
        recommendations.append("All chapters are well-structured and valid")

    return recommendations