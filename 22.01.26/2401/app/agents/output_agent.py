import os
from typing import Dict, Any
from models.schemas import ThesisDraft


def save_output(text: str, filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def build_thesis_text(
    thesis_draft: ThesisDraft,
    validation_report: Dict[str, Any],
    ethics_report: Dict[str, Any],
    revision_report: Dict[str, Any],
) -> str:

    lines = []

    lines.append(f"Thesis Topic: {thesis_draft.topic}")
    lines.append("")
    lines.append("=" * 80)
    lines.append("")

    for idx, chapter in enumerate(
        thesis_draft.chapter_drafts,
        start=1
    ):

        lines.append(
            f"CHAPTER {idx}: {chapter.chapter_title}"
        )
        lines.append("-" * 80)

        lines.append(
            f"Objective: {chapter.objective}"
        )

        lines.append("")
        lines.append("Subtopics:")

        for subtopic in chapter.subtopics:
            lines.append(f"• {subtopic}")

        lines.append("")
        lines.append("Content:")
        lines.append("")

        lines.append(str(chapter.draft))
        lines.append("")
        lines.append("=" * 80)
        lines.append("")

    lines.append("VALIDATION SUMMARY")
    lines.append(
        f"Status: {validation_report.get('overall_status', 'unknown')}"
    )
    lines.append(
        f"Total Issues: {validation_report.get('total_issues', 0)}"
    )

    lines.append("")
    lines.append("ETHICS SUMMARY")
    lines.append(
        f"Status: {ethics_report.get('overall_status', 'unknown')}"
    )
    lines.append(
        f"Ethical Score: {ethics_report.get('ethical_score', 0)}"
    )

    lines.append("")
    lines.append("REVISION SUMMARY")
    lines.append(
        f"Status: {revision_report.get('overall_status', 'unknown')}"
    )

    return "\n".join(lines)


def output_agent(
    thesis_draft: ThesisDraft,
    validation_report: Dict[str, Any],
    ethics_report: Dict[str, Any],
    revision_report: Dict[str, Any],
    filename: str = None,
) -> Dict[str, Any]:

    if not filename:

        safe_topic = (
            thesis_draft.topic
            .replace(" ", "_")
            .replace("/", "_")
        )

        filename = os.path.join(
            "outputs",
            f"{safe_topic}.txt"
        )

    output_text = build_thesis_text(
        thesis_draft,
        validation_report,
        ethics_report,
        revision_report
    )

    save_output(
        output_text,
        filename
    )

    return {
        "topic": thesis_draft.topic,
        "total_chapters": thesis_draft.total_chapters,
        "status": "saved",
        "message": f"Thesis output saved to {filename}",
        "generated_file": filename,
        "content_preview": output_text[:5000]
    }

