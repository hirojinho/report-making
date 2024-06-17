from langchain_community.llms.ollama import Ollama

class CompletionService:
    def __init__(self, model: str) -> None:
        self.model = Ollama(
            model=model
        )
    def generate_completion(self, input: str) -> str:
        response: str = self.model.invoke(input)
        return response