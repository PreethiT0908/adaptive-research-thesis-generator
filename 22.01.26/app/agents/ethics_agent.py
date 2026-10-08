def ethics_agent(text: str) -> dict:
    if "copied from" in text.lower():
        return {
            "ethical": False,
            "reason": "Potential plagiarism detected"
        }

    return {
        "ethical": True,
        "reason": "Content is original and compliant"
    }