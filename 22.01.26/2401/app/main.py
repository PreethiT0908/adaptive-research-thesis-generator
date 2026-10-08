from agents.profile_agent import profile_agent
from agents.blueprint_agent import blueprint_agent
from agents.search_agent import search_agent
from agents.rag_agent import rag_agent
from agents.drafting_agent import drafting_agent
from agents.validation_agent import validation_agent
from agents.ethics_agent import ethics_agent
from agents.revision_agent import revision_agent
from agents.output_agent import output_agent
from models.schemas import UserProfile, ResearchBlueprint, ThesisDraft


def get_user_input():
    print("Enter your academic details for thesis generation:\n")

    degree = input("Degree (PhD/Master/UG): ")
    university = input("University: ")
    discipline = input("Discipline: ")
    target_journal = input("Target Journal (optional): ")
    topic = input("Research Topic: ")

    return UserProfile(
        degree=degree,
        university=university,
        discipline=discipline,
        target_journal=target_journal if target_journal else None,
        topic=topic
    )


if __name__ == "__main__":
    # -------- Agent 1 --------
    user = get_user_input()
    policy = profile_agent(user)

    print("\n--- Research Policy (Agent 1) ---")
    print(f"Expected Pages: {policy.expected_pages}")
    print(f"Rigor Level: {policy.rigor_level}")
    print("Chapter Structure:")
    for ch in policy.structure:
        print(f"- {ch}")

    # -------- Agent 2 --------
    blueprint = blueprint_agent(policy)

    print("\n--- Research Blueprint (Agent 2) ---")
    for chapter in blueprint.chapters:
        print(f"\n{chapter.chapter_title}")
        print(f"Objective: {chapter.objective}")
        for sub in chapter.subtopics:
            print(f"  - {sub}")

    # -------- Agent 3 --------
    search_query = user.topic
    search_results = search_agent(search_query)

    print("\n--- Search Results (Agent 3) ---")
    for idx, result in enumerate(search_results, start=1):
        print(f"\nResult {idx}:")
        print(f"Title: {result.get('title')}")
        print(f"Authors: {', '.join(result.get('authors', []))}")
        print(f"Year: {result.get('year')}")
        print(f"Source: {result.get('source')}")
        print(f"URL: {result.get('pdf_url')}")

    # -------- Agent 4: RAG --------
    search_chunks = [result.get('title', '') for result in search_results]
    rag_results = rag_agent(search_query, search_chunks)

    print("\n--- RAG Agent Results (Agent 4) ---")
    if rag_results:
        for chunk in rag_results:
            print(f"- {chunk}")
    else:
        print("No relevant chunks found.")

    # -------- Agent 5: Drafting --------
    rag_results_by_chapter = {}
    for chapter in blueprint.chapters:
        rag_results_by_chapter[chapter.chapter_title] = rag_results

    drafts = drafting_agent(blueprint, rag_results_by_chapter, user.topic)

    print("\n--- Thesis Drafts (Agent 5) ---")
    print(f"Topic: {drafts['topic']}")
    print(f"Total Chapters: {drafts['total_chapters']}")
    print(f"Status: {drafts['status']}")
    
    for idx, chapter_draft in enumerate(drafts['chapter_drafts'], start=1):
        print(f"\n--- Chapter {idx}: {chapter_draft['chapter_title']} ---")
        print(f"Objective: {chapter_draft['objective']}")
        print("Subtopics:")
        for sub in chapter_draft['subtopics']:
            print(f"  - {sub}")
        print(f"\nDraft Preview:\n{chapter_draft['draft'][:200]}...")
        print(f"\nEvidence Sources: {len(chapter_draft['evidence_sources'])} items")

    # -------- Agent 6: Validation --------
    thesis_draft = ThesisDraft(
        total_chapters=drafts['total_chapters'],
        topic=drafts['topic'],
        chapter_drafts=drafts['chapter_drafts'],
        status=drafts['status']
    )

    validation_report = validation_agent(thesis_draft)

    print("\n--- Validation Report (Agent 6) ---")
    print(f"Topic: {validation_report['topic']}")
    print(f"Total Chapters: {validation_report['total_chapters']}")
    print(f"Chapters Passed: {validation_report['chapters_passed']}")
    print(f"Total Issues: {validation_report['total_issues']}")
    print(f"Overall Status: {validation_report['overall_status'].upper()}")
    
    print("\nChapter Validations:")
    for chapter_val in validation_report['chapter_validations']:
        print(f"\n  {chapter_val['chapter_title']}: {chapter_val['status'].upper()}")
        if chapter_val['issues']:
            for issue in chapter_val['issues']:
                print(f"    - {issue}")
        print(f"    Evidence: {chapter_val['evidence_count']} | Length: {chapter_val['draft_length']}")
    
    if validation_report['recommendations']:
        print("\nRecommendations:")
        for rec in validation_report['recommendations']:
            print(f"  - {rec}")

    # -------- Agent 7: Ethics --------
    ethics_report = ethics_agent(thesis_draft, validation_report)

    print("\n--- Ethics Report (Agent 7) ---")
    print(f"Topic: {ethics_report['topic']}")
    print(f"Total Chapters: {ethics_report['total_chapters']}")
    print(f"Chapters Approved: {ethics_report['chapters_approved']}")
    print(f"Ethical Score: {ethics_report['ethical_score']}/100")
    print(f"Overall Status: {ethics_report['overall_status'].upper()}")
    print(f"Clearance Status: {ethics_report['clearance_status'].upper()}")
    
    print("\nChapter Ethics:")
    for chapter_eth in ethics_report['chapter_ethics']:
        print(f"\n  {chapter_eth['chapter_title']}: {chapter_eth['status'].upper()} (Score: {chapter_eth['ethical_score']}/100)")
        if chapter_eth['issues']:
            for issue in chapter_eth['issues']:
                print(f"    - {issue}")
    
    if ethics_report['recommendations']:
        print("\nEthics Recommendations:")
        for rec in ethics_report['recommendations']:
            print(f"  - {rec}")

    # -------- Agent 8: Revision --------
    revision_report = revision_agent(thesis_draft, validation_report, ethics_report)

    print("\n--- Revision Report (Agent 8) ---")
    print(f"Topic: {revision_report['topic']}")
    print(f"Total Chapters: {revision_report['total_chapters']}")
    print(f"Chapters Requiring Revision: {revision_report['chapters_requiring_revision']}")
    print(f"Overall Status: {revision_report['overall_status'].upper()}")
    if revision_report['recommendations']:
        print("\nRevision Recommendations:")
        for rec in revision_report['recommendations']:
            print(f"  - {rec}")

    print("\nChapter Revision Plans:")
    for chapter_rev in revision_report['chapter_revisions']:
        print(f"\n  {chapter_rev['chapter_title']}: {'Needs revision' if chapter_rev['revision_needed'] else 'No revision needed'}")
        if chapter_rev['recommendations']:
            for rec in chapter_rev['recommendations']:
                print(f"    - {rec}")

    # -------- Agent 9: Output --------
    output_report = output_agent(thesis_draft, validation_report, ethics_report, revision_report)

    print("\n--- Output Report (Agent 9) ---")
    print(f"Status: {output_report['status'].upper()}")
    print(f"Message: {output_report['message']}")
    if output_report['generated_file']:
        print(f"Saved File: {output_report['generated_file']}")