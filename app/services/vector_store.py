import numpy as np

# simple in-memory store for demo
VECTOR_STORE = {}

def add_vector(story_id: int, embedding: list):
    VECTOR_STORE[story_id] = np.array(embedding)

def search_vectors(query_embedding: list, top_k: int = 3):
    if not VECTOR_STORE:
        return []

    query_vec = np.array(query_embedding)

    scores = []
    for story_id, vec in VECTOR_STORE.items():
        score = np.dot(query_vec, vec) / (
            np.linalg.norm(query_vec) * np.linalg.norm(vec)
        )
        scores.append((story_id, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return [sid for sid, score in scores[:top_k] if score > 0.1]
