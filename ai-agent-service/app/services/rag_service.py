from app.db.vector_db import (
    vector_store
)

async def search_policy_context(
    question: str
):

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    return "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )