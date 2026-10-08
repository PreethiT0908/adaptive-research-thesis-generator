from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class GenerateRequest(BaseModel):
    degree: str
    university: str
    discipline: str
    target_journal: str
    topic: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(request: GenerateRequest):
    # Example backend response for the frontend to consume.
    return {
        "status": "success",
        "prompt": f"Generate a thesis for {request.degree} in {request.discipline} at {request.university} targeting {request.target_journal} on {request.topic}.",
        "result": {
            "title": f"{request.topic.capitalize()} for {request.degree}",
            "abstract": f"This adaptive thesis proposal explores {request.topic} within the field of {request.discipline}.",
            "target_journal": request.target_journal,
        },
    }
