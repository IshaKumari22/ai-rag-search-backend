import random

def generate_embedding(text: str):
    # Fake embedding for demo (fixed length vector)
    random.seed(hash(text))
    return [random.random() for _ in range(384)]
