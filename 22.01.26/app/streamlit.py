import streamlit as st

from agents.profile_agent import profile_agent
from agents.blueprint_agent import blueprint_agent
from agents.search_agent import search_agent
from models.schemas import UserProfile
from models.schemas import ResearchBlueprint


st.set_page_config(page_title="Adaptive Thesis Generator", layout="wide")
st.title("📘 Adaptive Thesis Generator")

# -------- User Input --------
with st.form(key="user_profile_form"):
    degree = st.selectbox("Degree", ["UG", "Master", "PhD"])
    university = st.text_input("University")
    discipline = st.text_input("Discipline")
    target_journal = st.text_input("Target Journal (optional)")
    topic = st.text_input("Research Topic")

    submit_button = st.form_submit_button(label="Run Profile → Blueprint → Search")

if submit_button:
    user = UserProfile(
        degree=degree,
        university=university,
        discipline=discipline,
        target_journal=target_journal if target_journal else None,
        topic=topic
    )

    # -------- Agent 1: Profile --------
    policy = profile_agent(user)

    st.subheader("🔹 Step 1: Research Policy")
    st.write(f"**Expected Pages:** {policy.expected_pages}")
    st.write(f"**Rigor Level:** {policy.rigor_level}")
    st.write("**Chapter Structure:**")
    for chapter in policy.structure:
        st.write(f"- {chapter}")

    # -------- Agent 2: Blueprint --------
    blueprint = blueprint_agent(policy)

    st.subheader("🔹 Step 2: Research Blueprint")
    for chapter in blueprint.chapters:
        with st.expander(chapter.chapter_title):
            st.write(f"**Objective:** {chapter.objective}")
            for sub in chapter.subtopics:
                st.write(f"- {sub}")

    # -------- Agent 3: Search --------
    search_results = search_agent(blueprint)

    st.subheader("🔹 Step 3: Academic Search Plan")
    for result in search_results:
        with st.expander(f"📄 {result.chapter}"):
            st.write(f"**Search Query:** {result.query}")
            st.write("**Target Sources:**")
            for src in result.sources:
                st.write(f"- {src}")
