import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.profile_agent import profile_agent
from agents.blueprint_agent import blueprint_agent
from agents.search_agent import search_agent
from models.schemas import UserProfile

app = FastAPI()

# Allow local frontend dev servers (Vite/CRA)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Adaptive Thesis Generator API Running"}


@app.post("/generate")
def generate_thesis(data: UserProfile):
    try:
        policy = profile_agent(data)
        blueprint = blueprint_agent(policy)
        papers = search_agent(data.topic)

        # Convert results to serializable format
        policy_dict = policy.model_dump() if hasattr(policy, 'model_dump') else policy
        blueprint_dict = blueprint.model_dump() if hasattr(blueprint, 'model_dump') else blueprint
        papers_list = [p.model_dump() if hasattr(p, 'model_dump') else p for p in papers]

        return {
            "status": "success",
            "policy": policy_dict,
            "blueprint": blueprint_dict,
            "papers": papers_list
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "error_type": type(e).__name__
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

