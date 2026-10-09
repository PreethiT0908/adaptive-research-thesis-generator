import os
from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()

# ---------------------------------------------------------
# Groq configuration
# ---------------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

# ---------------------------------------------------------
# Validate API key
# ---------------------------------------------------------
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add GROQ_API_KEY to your .env file "
        "or Render Environment Variables."
    )

# ---------------------------------------------------------
# Create Groq client using OpenAI-compatible API
# ---------------------------------------------------------
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


# ---------------------------------------------------------
# Generate text using Groq
# ---------------------------------------------------------
def generate_text(prompt: str) -> str:

    try:

        # Validate prompt
        if not prompt or not prompt.strip():
            return "LLM ERROR: Empty prompt received."

        print("\n" + "=" * 70)
        print("GROQ LLM REQUEST")
        print("=" * 70)
        print(f"Model: {GROQ_MODEL}")
        print(f"Prompt length: {len(prompt)} characters")
        print("=" * 70)

        # -------------------------------------------------
        # Send request to Groq
        # -------------------------------------------------
        response = client.chat.completions.create(
            model=GROQ_MODEL,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert academic research assistant "
                        "specializing in thesis writing, scientific research, "
                        "and scholarly academic content. "
                        "Generate accurate, detailed, well-structured "
                        "academic content based on the provided research topic."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,

            # Allow longer thesis chapters
            max_tokens=4000
        )

        # -------------------------------------------------
        # Validate response
        # -------------------------------------------------
        if not response:
            return "LLM ERROR: Empty response received from Groq."

        if not response.choices:
            return "LLM ERROR: Groq returned no response choices."

        message = response.choices[0].message

        if not message:
            return "LLM ERROR: Groq returned an empty message."

        content = message.content

        if not content:
            return "LLM ERROR: Groq returned empty content."

        content = content.strip()

        # -------------------------------------------------
        # Print successful response information
        # -------------------------------------------------
        print("\n" + "=" * 70)
        print("GROQ LLM RESPONSE SUCCESS")
        print("=" * 70)
        print(f"Response length: {len(content)} characters")
        print("=" * 70)

        return content

    # -----------------------------------------------------
    # Handle API errors
    # -----------------------------------------------------
    except Exception as e:

        error_type = type(e).__name__
        error_message = str(e)

        print("\n" + "=" * 70)
        print("GROQ LLM ERROR")
        print("=" * 70)
        print(f"Error Type: {error_type}")
        print(f"Error Message: {error_message}")
        print("=" * 70)

        # IMPORTANT:
        # Return the actual error so the drafting agent
        # does not replace it with placeholder content.
        return f"LLM ERROR: {error_message}"