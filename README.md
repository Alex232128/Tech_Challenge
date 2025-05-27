# API de Vitivinicultura – Embrapa

API pública para consulta de dados de vitivinicultura diretamente do site da Embrapa.

## 🚀 Como executar

```bash
git clone https://https://github.com/Alex232128/Tech_Challenge
cd vitivinicultura-api
pip install -r requirements.txt
uvicorn app.main:app --reload

# API de Vitivinicultura - Embrapa

Este projeto consiste em uma API pública desenvolvida em Python com FastAPI que consulta dados de vitivinicultura disponibilizados pela Embrapa. A API faz raspagem (web scraping) em tempo real dos dados no site oficial e oferece um fallback local para garantir disponibilidade mesmo em caso de instabilidade do site.

---

## Funcionalidades

- Consulta os dados de produção, processamento, comercialização, importação e exportação do site da Embrapa.
- Web scraping utilizando Requests e BeautifulSoup para extrair as tabelas da página.
- Retorno dos dados em formato JSON.
- Fallback automático para arquivo local `fallback.json` em caso de falha na raspagem.
- Endpoint RESTful disponível para consumo externo.
- Documentação automática via Swagger UI.

---

## Tecnologias utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Pytest (para testes automatizados)

---

## Estrutura do projeto

/
├── app/
│ ├── main.py # Arquivo principal da API
│ ├── scraping.py # Funções de raspagem do site
│ ├── fallback.py # Função para carregar fallback local
│
├── data/
│ └── fallback.json # Arquivo JSON com dados de fallback
│
├── test_scraping.py # Teste automatizado para raspagem e fallback
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo

yaml
Copy
Edit

---

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://https://github.com/Alex232128/Tech_Challenge
cd seu-repositorio
2. Crie e ative um ambiente virtual (recomendado)
No Windows:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
No Linux/Mac:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt
4. Rode a API
bash
Copy
Edit
uvicorn app.main:app --reload
5. Acesse a API no navegador
Abra:

bash
Copy
Edit
http://127.0.0.1:8000/api/v1/dados
Para acessar os dados raspados.

6. Documentação interativa
Swagger UI disponível em:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
Testes automatizados
Para rodar os testes, execute:

bash
Copy
Edit
pytest test_scraping.py
Isso garante que a raspagem e o fallback estejam funcionando corretamente.

Deploy
A API está disponível publicamente em:

bash
Copy
Edit
https://seu-deploy-url.com/api/v1/dados
(Altere para a URL do seu deploy)

Observações
A API tenta sempre trazer os dados ao vivo do site da Embrapa.

Caso o site esteja indisponível, ela retorna os dados do arquivo fallback.json.

É importante manter o fallback atualizado rodando localmente pelo menos uma vez com sucesso.

Contato
Para dúvidas, sugestões ou melhorias, entre em contato:

Alexandre - seu.email@exemplo.com

GitHub: https://https://github.com/Alex232128/Tech_Challenge

Licença
Este projeto está licenciado sob a MIT License.