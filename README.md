Pipeline ETL com Python e IA Generativa 🚀

Este projeto foi desenvolvido como parte de um desafio da plataforma DIO, simulando um pipeline de dados (ETL - Extraction, Transformation and Loading) de um cenário bancário. O objetivo é extrair dados de clientes, utilizar Inteligência Artificial para gerar mensagens personalizadas e salvar os resultados.

📝 O Desafio
O objetivo principal é entender o fluxo de dados em um processo de Engenharia de Dados. Mesmo com a indisponibilidade de APIs externas de demonstração, o projeto foca na resiliência, utilizando fontes de dados locais (CSV) e integração com o Google Gemini para a camada de inteligência.

⚙️ Arquitetura do Projeto (ETL)
Extract (Extração): Leitura de um arquivo CSV (SDW2023.csv) contendo dados brutos de clientes (ID, Nome, Saldo).

Transform (Transformação): Utilização da API do Google Gemini (IA) para processar o nome e o saldo do cliente e gerar uma recomendação de investimento personalizada.

Resiliência: O sistema conta com um mecanismo de Fallback. Caso a API esteja indisponível ou ocorra um erro de autenticação, o sistema gera automaticamente uma mensagem padrão, garantindo que o pipeline não seja interrompido.

Load (Carregamento): Exportação dos dados processados para um novo arquivo CSV (SDW2023_FINAL.csv), pronto para ser consumido por outros sistemas.

🛠️ Tecnologias Utilizadas
Python 3.x

Pandas: Manipulação e análise de dados.

Google Generative AI: Integração com o modelo gemini-1.5-flash.

Git/GitHub: Versionamento e documentação.

🚀 Como Executar

Clone o repositório:

git clone https://github.com/GUSTAVO-GUILHEN/santander-dev-week-etl-python.git

Instale as dependências:

pip install pandas google-generativeai

Configuração da API (Opcional):

Configure sua API Key do Google AI Studio diretamente no código ou via variável de ambiente para habilitar a geração via IA.

Execute o script:

python main.py

Desenvolvido por Gustavo Guilhen durante o Bootcamp na DIO.
