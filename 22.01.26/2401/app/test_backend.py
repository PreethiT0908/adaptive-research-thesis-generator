from services.llm_client import generate_text

response = generate_text(
    "Write 100 words about Climate Change"
)

print(response)