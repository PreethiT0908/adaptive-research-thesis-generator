from models.schemas import ResearchPolicy, ResearchBlueprint, ChapterBlueprint


def blueprint_agent(policy: ResearchPolicy) -> ResearchBlueprint:
    chapters = []

    for chapter in policy.structure:
        if chapter.lower() == "introduction":
            subtopics = [
                "Background and Motivation",
                "Problem Definition",
                "Research Objectives",
                "Contributions"
            ]
        elif chapter.lower() == "literature review":
            subtopics = [
                "Classical Approaches",
                "Recent Advances",
                "Critical Analysis",
                "Research Gaps"
            ]
        elif chapter.lower() == "methodology":
            subtopics = [
                "System Architecture",
                "Algorithms and Models",
                "Data Collection",
                "Experimental Design"
            ]
        elif chapter.lower() == "results":
            subtopics = [
                "Experimental Setup",
                "Quantitative Results",
                "Qualitative Analysis"
            ]
        elif chapter.lower() == "discussion":
            subtopics = [
                "Interpretation of Results",
                "Comparison with Existing Work",
                "Limitations"
            ]
        elif chapter.lower() == "conclusion":
            subtopics = [
                "Summary of Findings",
                "Future Research Directions"
            ]
        elif chapter.lower() == "references":
            subtopics = [
                "APA / IEEE formatted citations"
            ]
        else:
            subtopics = ["To be defined"]

        chapters.append(
            ChapterBlueprint(
                chapter_title=chapter,
                objective=f"Explain and analyze {chapter.lower()} in context of the research topic",
                subtopics=subtopics
            )
        )

    return ResearchBlueprint(
        total_chapters=len(chapters),
        chapters=chapters
    )
