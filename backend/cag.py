"""Implementacion CAG: aplica contexto del usuario a la respuesta base."""


def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer

    context_summary = ", ".join(
        f"{item['key']}: {item['value']}" for item in context_items
    )

    return (
        f"{base_answer} "
        f"[Contexto del usuario - {context_summary}]"
    )