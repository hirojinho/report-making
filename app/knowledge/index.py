import os
from app.clients.embedding import EmbeddingClient

def initiate_knowledge() -> EmbeddingClient:# Get the current file's directory path
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the 'data' folder inside the current directory
    data_folder_path = os.path.join(current_file_directory, 'base')
    knowledge = EmbeddingClient(folder_path=data_folder_path)
    return knowledge