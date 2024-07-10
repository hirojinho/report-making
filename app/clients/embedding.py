from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings

class EmbeddingClient:
    def __init__(self, model: str) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        self.vectorstore = Chroma.from_documents(documents='all_splits', embedding=GPT4AllEmbeddings())
    def search(self, question: str) -> list[str]:
        docs = self.vectorstore.similarity_search(question)
        return [doc.page_content for doc in docs]