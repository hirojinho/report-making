from concurrent.futures import ThreadPoolExecutor
import os
from PyPDF2 import PdfReader, PdfWriter
import pytesseract
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from pdf2image import convert_from_path
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

class EmbeddingClient:
    def __init__(self, folder_path: str) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        knowledge_string = self._convert_files(folder_path)
        self.initiate_vector_store(knowledge_string)
        
    def _split_pdf(self, file_path: str, max_pages_per_file: int = 10) -> list[str]:
        print(f'\n>>> Splitting PDF: {file_path}')
        reader = PdfReader(file_path)
        total_pages = len(reader.pages)
        split_files = []

        # Define the subfolder path
        base_folder = os.path.dirname(file_path)
        subfolder_path = os.path.join(base_folder, "split_pdfs")
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        for start_page in range(0, total_pages, max_pages_per_file):
            writer = PdfWriter()
            # Adjust the split_file_path to include the subfolder
            file_name = os.path.basename(file_path)
            split_file_name = f"{file_name}_part_{start_page // max_pages_per_file + 1}.pdf"
            split_file_path = os.path.join(subfolder_path, split_file_name)

            for page in range(start_page, min(start_page + max_pages_per_file, total_pages)):
                writer.add_page(reader.pages[page])
            with open(split_file_path, 'wb') as f:
                writer.write(f)
            split_files.append(split_file_path)

        print(f'\nPDF split into {len(split_files)} parts')
        return split_files
        
    def _convert_files(self, folder_path: str) -> str:
        print('\n>>> Converting files...')
        pdf_texts = {}
        def convert_pdf_to_text(file_path):
            text = ""
            # Convert PDF to images
            pages = convert_from_path(file_path, 100)
            for page in pages:
                # Convert the image to text using OCR
                text += pytesseract.image_to_string(page)
            os.remove(file_path)  # Clean up split PDFs after processing
            return text
        with ThreadPoolExecutor() as executor:
            future_to_file = {}
            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    file_path = os.path.join(folder_path, filename)
                    # Split PDF into smaller ones if needed
                    split_files = self._split_pdf(file_path, max_pages_per_file=10)
                    for split_file in split_files:
                        future = executor.submit(convert_pdf_to_text, split_file)
                        future_to_file[future] = filename
            for future in future_to_file:
                filename = future_to_file[future]
                text = future.result()
                if filename in pdf_texts:
                    pdf_texts[filename] += text
                else:
                    pdf_texts[filename] = text
        print(f'\n>>> Pages converted to text: {len(pdf_texts)}')
        combined_text = "\n".join(pdf_texts.values())  # Combine texts with newline separation
        return combined_text
        
    def search(self, question: str) -> list[str]:
        print('\n>>> Searching...')
        docs = self.vectorstore.similarity_search(question)
        return [doc.page_content for doc in docs]
    
    def initiate_vector_store(self, docs: str) -> None:
        print('\n>>> Initiating vector store...')
        all_splits = self.text_splitter.split_text(docs)
        # create the open-source embedding function
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")   
        self.vectorstore = Chroma.from_documents(documents=self.text_splitter.create_documents(all_splits), embedding=embedding_function)