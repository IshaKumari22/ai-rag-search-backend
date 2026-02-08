def generate_response(query: str, stories: list):
    """
    Fake RAG generation for demo.
    Uses retrieved content instead of LLM.
    """

    if not stories:
        return "No relevant content available."

    combined_text = " ".join(
        [story.transcript or story.description for story in stories]
    )

    return f"Based on retrieved content: {combined_text}"
