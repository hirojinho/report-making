from app.clients.embedding import EmbeddingClient

def initiate_knowledge() -> EmbeddingClient:
    knowledge = EmbeddingClient(file_path="app/knowledge/base")
    return knowledge