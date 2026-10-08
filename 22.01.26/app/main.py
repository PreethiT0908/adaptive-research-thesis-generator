from agents.profile_agent import profile_agent
from agents.blueprint_agent import blueprint_agent
from models.schemas import UserProfile
from models.schemas import ResearchBlueprint


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
