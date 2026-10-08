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


def run_profile_to_search(user: UserProfile):
    """
    Agent Flow:
    Profile → Blueprint → Search → RAG → Drafting → Validation → Ethics → Revision
    """

    policy = profile_agent(user)
    blueprint = blueprint_agent(policy)

    search_query = user.topic
    search_results = search_agent(search_query)

    search_chunks = [result["title"] for result in search_results]
    rag_results = rag_agent(search_query, search_chunks)

    # Map RAG results to chapters
    rag_results_by_chapter = {}
    for chapter in blueprint.chapters:
        rag_results_by_chapter[chapter.chapter_title] = rag_results

    # Draft all chapters
    drafts = drafting_agent(blueprint, rag_results_by_chapter, user.topic)

    # Convert drafts to ThesisDraft schema for validation
    thesis_draft = ThesisDraft(
        total_chapters=drafts['total_chapters'],
        topic=drafts['topic'],
        chapter_drafts=drafts['chapter_drafts'],
        status=drafts['status']
    )

    # Validate all drafts
    validation_report = validation_agent(thesis_draft)

    # Ethics check
    ethics_report = ethics_agent(thesis_draft, validation_report)

    # Revision planning
    revision_report = revision_agent(thesis_draft, validation_report, ethics_report)

    # Output generation
    output_report = output_agent(thesis_draft, validation_report, ethics_report, revision_report)

    return (
        policy,
        blueprint,
        search_results,
        rag_results,
        thesis_draft,
        validation_report,
        ethics_report,
        revision_report,
        output_report,
    )

