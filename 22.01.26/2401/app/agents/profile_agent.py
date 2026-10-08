from models.schemas import UserProfile, ResearchPolicy

def profile_agent(profile: UserProfile) -> ResearchPolicy:
    """
    Input: UserProfile
    Output: ResearchPolicy containing expected_pages, rigor_level, structure
    """
    degree = profile.degree.lower()
    
    if degree == "phd":
        pages = "120-180"
        rigor = "very_high"
        structure = [
            "Introduction",
            "Literature Review",
            "Problem Statement",
            "Methodology",
            "Experiments",
            "Results",
            "Discussion",
            "Conclusion",
            "References"
        ]
    elif degree in ["master", "pg"]:
        pages = "40-80"
        rigor = "high"
        structure = [
            "Abstract",
            "Introduction",
            "Related Work",
            "Methodology",
            "Results",
            "Conclusion",
            "References"
        ]
    else:  # UG / others
        pages = "10-20"
        rigor = "medium"
        structure = [
            "Abstract",
            "Introduction",
            "Related Work",
            "Methodology",
            "Results",
            "Conclusion",
            "References"
        ]
    
    return ResearchPolicy(
        expected_pages=pages,
        rigor_level=rigor,
        structure=structure
    )