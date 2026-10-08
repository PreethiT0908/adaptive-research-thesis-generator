from agents.profile_agent import profile_agent
from agents.blueprint_agent import blueprint_agent
from agents.search_agent import search_agent
from models.schemas import UserProfile
from app.agents.blueprint_agent import blueprint_agent
from app.models.schemas import ResearchBlueprint


def run_profile_to_search(user: UserProfile):
    """
    Agent Flow:
    Profile → Blueprint → Search
    """

    policy = profile_agent(user)
    blueprint = blueprint_agent(policy)
    search_results = search_agent(blueprint)

    return policy, blueprint, search_results
