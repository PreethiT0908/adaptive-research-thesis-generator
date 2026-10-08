def save_output(text: str, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)