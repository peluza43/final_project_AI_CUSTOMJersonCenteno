from backend.knowledge import retrieve_snippets


def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        return {
            "user_id": user_id,
            "answer": "No encontre informacion suficiente en la base de conocimiento del curso.",
            "sources": [],
            "context_used": [],
        }

    source_text = " ".join(item["content"] for item in snippets)
    answer = f"Segun la base de conocimiento del curso: {source_text}"

    return {
        "user_id": user_id,
        "answer": answer,
        "sources": [item["id"] for item in snippets],
        "context_used": [],
    }
