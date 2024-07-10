# from app import app

from app.clients.completion import CompletionClient
from app.knowledge.index import initiate_knowledge

if __name__ == '__main__':
    # app.run(debug=True)
    knowledge = initiate_knowledge()
    completion_client = CompletionClient(model="phi3")
    user_input = ''
    while user_input != "exit":
        user_input = input("Faça uma pergunta: ")
        if(user_input == "exit"):
            break
        found_knowledge = knowledge.search(user_input)
        formatted_knowledge = ''''''
        for i, info in enumerate(found_knowledge, start=1):
            formatted_knowledge += f"{i}. {info}\n"
        prompt=f'''
                Você é um assistente de tirar dúvidas de um estudante.
                Você procurou nos livros e encontrou a seguinte informação:
                {formatted_knowledge}
                '''
        print(prompt)
        print('>>>>')
        conversation = [{'role': 'system', 'content': prompt}]
        conversation.append({'role': 'user', 'content': user_input})
        answer = completion_client.generate_completion(user_input)
        print(answer)