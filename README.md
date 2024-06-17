# Projeto de Geração de Relatórios com LLMs

## Descrição

Este é um projeto open source criado como um hobby, que utiliza modelos de linguagem natural (LLMs) para escrever relatórios de práticas experimentais para faculdade. O sistema é baseado em Flask e utiliza a biblioteca do Ollama com o modelo PHI3 Vision. Além disso, emprega uma base de conhecimento armazenada em um banco de dados vetorial do Marqo.

Embora o foco principal seja a criação de relatórios de práticas experimentais, o projeto pode ser testado e adaptado para outros tipos de relatórios.

## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para criar a aplicação.
- **Ollama**: Biblioteca utilizada para integrar modelos de linguagem natural.
- **PHI3 Vision**: Modelo de linguagem utilizado para geração de texto.
- **Marqo**: Banco de dados vetorial utilizado para armazenar e consultar a base de conhecimento.

## Funcionalidades

- Geração de relatórios de práticas experimentais automatizada.
- Possibilidade de adaptação para outros tipos de relatórios.
- Integração com uma base de conhecimento para enriquecer o conteúdo dos relatórios.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
## Uso

1. Inicie o servidor Flask:
    ```bash
    flask run
2. Acesse a aplicação em seu navegador:
    ```bash
    http://127.0.0.1:5000
3. Siga as instruções na interface para gerar seu relatório.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no GitHub.
Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
Report Generation Project with LLMs

## Description

This is an open source project created as a hobby, which uses natural language models (LLMs) to write experimental practice reports for college. The system is based on Flask and uses the Ollama library with the PHI3 Vision model. Additionally, it employs a knowledge base stored in a Marqo vector database.

Although the main focus is on creating experimental practice reports, the project can be tested and adapted for other types of reports.
Technologies Used
    Flask: Web framework used to create the application.
    Ollama: Library used to integrate natural language models.
    PHI3 Vision: Language model used for text generation.
    Marqo: Vector database used to store and query the knowledge base.

## Features
    Automated generation of experimental practice reports.
    Adaptability for other types of reports.
    Integration with a knowledge base to enrich report content.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
## Usage
1. Start the Flask server:
    ```bash
    flask run
2. Access the application in your browser:
    ```bash
    http://127.0.0.1:5000
3. Follow the instructions in the interface to generate your report.

## Contribution

Contributions are welcome! Feel free to open issues and pull requests on GitHub.
License

This project is licensed under the MIT License. See the LICENSE file for more details.