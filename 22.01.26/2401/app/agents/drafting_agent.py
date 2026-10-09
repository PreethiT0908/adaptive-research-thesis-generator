from typing import Dict, List, Any

from models.schemas import ResearchBlueprint, ThesisDraft
from services.llm_client import generate_text


def drafting_agent(
    blueprint,
    rag_results_by_chapter,
    topic
):
    """
    Generate actual academic thesis content for every chapter
    using the Groq LLM and available RAG evidence.
    """

    drafts = []

    print("\n" + "=" * 80)
    print("DRAFTING AGENT STARTED")
    print(f"Research Topic: {topic}")
    print(f"Total Chapters: {len(blueprint.chapters)}")
    print("=" * 80)

    for chapter in blueprint.chapters:

        chapter_title = chapter.chapter_title
        chapter_objective = chapter.objective
        chapter_subtopics = chapter.subtopics

        print("\n" + "-" * 80)
        print(f"GENERATING CHAPTER: {chapter_title}")
        print("-" * 80)

        # ---------------------------------------------------------
        # Get RAG evidence for this chapter
        # ---------------------------------------------------------

        content = rag_results_by_chapter.get(
            chapter_title,
            []
        )

        # ---------------------------------------------------------
        # Convert RAG evidence into text
        # ---------------------------------------------------------

        if isinstance(content, list):

            evidence_text = "\n\n".join(
                str(item)
                for item in content
            )

        elif content:

            evidence_text = str(content)

        else:

            evidence_text = (
                "No specific research evidence was retrieved "
                "for this chapter."
            )

        # ---------------------------------------------------------
        # Prevent extremely large prompts
        # ---------------------------------------------------------

        if len(evidence_text) > 12000:

            evidence_text = evidence_text[:12000]

            print(
                "RAG evidence truncated to 12000 characters."
            )

        # ---------------------------------------------------------
        # Build academic generation prompt
        # ---------------------------------------------------------

        prompt = f"""
You are an expert academic researcher and thesis writer.

You are writing a real academic thesis.

RESEARCH TOPIC:
{topic}

CHAPTER TITLE:
{chapter_title}

CHAPTER OBJECTIVE:
{chapter_objective}

CHAPTER SUBTOPICS:
{chapter_subtopics}

RESEARCH EVIDENCE:
{evidence_text}

YOUR TASK:

Write the actual academic content for the chapter:

"{chapter_title}"

IMPORTANT REQUIREMENTS:

1. The content must be directly related to the research topic:
   "{topic}"

2. Write genuine academic content, not an explanation of
   how to write a thesis.

3. Do not explain what an Introduction, Literature Review,
   Methodology, Results, Discussion, Conclusion, or Abstract is.

4. Write the actual material that belongs inside the chapter.

5. Use formal academic English.

6. Use appropriate academic headings and subheadings.

7. Maintain logical flow between sections.

8. Use the supplied research evidence whenever relevant.

9. Do not invent experimental results.

10. Do not invent numerical statistics.

11. Do not invent authors, papers, journals, DOI numbers,
    or references.

12. Do not create fake citations.

13. If the supplied evidence is insufficient, clearly discuss
    the topic using established general knowledge without
    pretending that unsupported claims came from a specific
    research source.

14. Every section must remain relevant to:
    "{topic}"

15. Avoid generic filler.

16. Do not use phrases such as:
    "Additional content generation is required."

17. Do not use placeholder text.

18. Do not say that you are an AI.

19. Do not mention these instructions.

20. Do not describe the generation process.

21. Produce detailed content suitable for an academic thesis.

22. Target approximately 800-1200 words when sufficient
    information is available.

23. Use clear academic paragraphs.

24. Make the content specific to the research topic rather
    than producing generic textbook content.

25. Return ONLY the thesis chapter content.

BEGIN CHAPTER CONTENT:
"""

        # ---------------------------------------------------------
        # Generate content using Groq
        # ---------------------------------------------------------

        try:

            draft_text = generate_text(prompt)

            # -----------------------------------------------------
            # Check empty response
            # -----------------------------------------------------

            if not draft_text:

                print(
                    f"WARNING: Empty LLM response for "
                    f"{chapter_title}"
                )

                draft_text = (
                    f"LLM returned empty content for chapter: "
                    f"{chapter_title}"
                )

            # -----------------------------------------------------
            # Preserve actual LLM errors
            # -----------------------------------------------------

            elif draft_text.startswith("LLM ERROR:"):

                print(
                    f"LLM ERROR for {chapter_title}:"
                )

                print(draft_text)

            # -----------------------------------------------------
            # Clean response
            # -----------------------------------------------------

            draft_text = draft_text.strip()

            # -----------------------------------------------------
            # Log generated content length
            # -----------------------------------------------------

            print(
                f"Generated content length: "
                f"{len(draft_text)} characters"
            )

            # -----------------------------------------------------
            # Show first part for debugging
            # -----------------------------------------------------

            print(
                "\nGenerated preview:"
            )

            print(
                draft_text[:500]
            )

        except Exception as e:

            print(
                f"ERROR generating chapter "
                f"{chapter_title}: {e}"
            )

            draft_text = (
                f"Generation Error for "
                f"{chapter_title}: {str(e)}"
            )

        # ---------------------------------------------------------
        # Store chapter draft
        # ---------------------------------------------------------

        drafts.append(
            {
                "chapter_title": chapter_title,
                "objective": chapter_objective,
                "subtopics": chapter_subtopics,
                "draft": draft_text,
                "evidence_sources": content
            }
        )

        print(
            f"FINISHED CHAPTER: {chapter_title}"
        )

    # -------------------------------------------------------------
    # Return complete thesis drafts
    # -------------------------------------------------------------

    result = {
        "topic": topic,
        "total_chapters": len(blueprint.chapters),
        "status": "generated",
        "chapter_drafts": drafts
    }

    print("\n" + "=" * 80)
    print("DRAFTING AGENT COMPLETED")
    print(f"Generated Chapters: {len(drafts)}")
    print("=" * 80)

    return result