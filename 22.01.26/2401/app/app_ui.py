import streamlit as st

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
from services.pdf_generator import generate_pdf
st.set_page_config(page_title="Adaptive Thesis Generator", layout="wide")
st.title("📘 Adaptive Thesis Generator")

# -------- User Input --------
with st.form(key="user_profile_form"):
    degree = st.selectbox("Degree", ["UG", "Master", "PhD"])
    university = st.text_input("University")
    discipline = st.text_input("Discipline")
    target_journal = st.text_input("Target Journal (optional)")
    topic = st.text_input("Research Topic")

    submit_button = st.form_submit_button(label="Generate Thesis")

if submit_button:

    with st.spinner("Generating Thesis... Please wait..."):

        # User Profile
        user = UserProfile(
            degree=degree,
            university=university,
            discipline=discipline,
            target_journal=target_journal if target_journal else None,
            topic=topic
        )

        # Agent 1
        policy = profile_agent(user)

        # Agent 2
        blueprint = blueprint_agent(policy)

        # Agent 3
        search_results = search_agent(user.topic)

        # Agent 4
        search_chunks = [
            result.get("title", "")
            for result in search_results
        ]

        rag_results = rag_agent(
            user.topic,
            search_chunks
        )

        # Agent 5
        rag_results_by_chapter = {}

        for chapter in blueprint.chapters:
            rag_results_by_chapter[
                chapter.chapter_title
            ] = rag_results

        drafts = drafting_agent(
            blueprint,
            rag_results_by_chapter,
            user.topic
        )

        # Agent 6
        thesis_draft = ThesisDraft(
            total_chapters=drafts["total_chapters"],
            topic=drafts["topic"],
            chapter_drafts=drafts["chapter_drafts"],
            status=drafts["status"]
        )

        validation_report = validation_agent(
            thesis_draft
        )

        # Agent 7
        ethics_report = ethics_agent(
            thesis_draft,
            validation_report
        )

        # Agent 8
        revision_report = revision_agent(
            thesis_draft,
            validation_report,
            ethics_report
        )

        # Agent 9
        output_report = output_agent(
            thesis_draft,
            validation_report,
            ethics_report,
            revision_report
        )

    # Final Output Only

    if output_report["status"] == "saved":

        st.success("✅ Thesis Generated Successfully")

        # TXT Download
        with open(
            output_report["generated_file"],
            "rb"
        ) as txt_file:

            st.download_button(
                label="📄 Download Thesis TXT",
                data=txt_file,
                file_name=f"{user.topic}.txt",
                mime="text/plain"
            )

        # PDF Generate
        pdf_path = generate_pdf(
            thesis_draft,
            output_report["generated_file"].replace(
                ".txt",
                ".pdf"
            )
        )

        # PDF Download
        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📕 Download Thesis PDF",
                data=pdf_file,
                file_name=f"{user.topic}.pdf",
                mime="application/pdf"
            )

    else:
        st.error(output_report["message"])