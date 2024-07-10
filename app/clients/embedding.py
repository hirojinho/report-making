import os
import pytesseract
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from pdf2image import convert_from_path

class EmbeddingClient:
    def __init__(self, file_path: str) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        knowledge_string = self.convert_files(file_path)
        self.initiate_vector_store(knowledge_string)
        
    def search(self, question: str) -> list[str]:
        docs = self.vectorstore.similarity_search(question)
        return [doc.page_content for doc in docs]
    
    def initiate_vector_store(self, docs: str) -> None:
        all_splits = self.text_splitter.split_texts(docs)
        self.vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())
        
    def convert_files(self, folder_path: str) -> list[str]:
        pdf_texts = {}
        for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    file_path = os.path.join(folder_path, filename)
                    # Convert PDF to images
                    pages = convert_from_path(file_path, 300)
                    text = ""
                    for page in pages:
                        # Convert the image to text using OCR
                        text += pytesseract.image_to_string(page)
                    pdf_texts[filename] = text
        combined_text = ""
        for value in pdf_texts.values():
            combined_text += value + "\n"  # Adding a newline for separation between different PDF texts
        return combined_text