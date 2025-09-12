# Projeto_de_estudo_crud

Este projeto é um CRUD simples desenvolvido para fins de estudo e aprendizado de desenvolvimento web com Python e Flask. O objetivo é praticar operações básicas de cadastro, listagem e remoção de usuários utilizando um banco de dados SQLite.

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para criar as rotas e renderizar os templates.
- **SQLite**: Banco de dados leve e integrado, utilizado para armazenar os dados dos usuários.
- **HTML e CSS**: Utilizados para estruturar e estilizar as páginas.
- **Bootstrap**: Biblioteca para estilização rápida e responsiva das interfaces.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `db/init_db.py`: Script responsável pela conexão e manipulação do banco de dados SQLite.
- `db/user_data.db`: Arquivo do banco de dados.
- `static/style.css`: Arquivo de estilos customizados.
- `templates/`: Pasta contendo os arquivos HTML dos templates.
  - `base.html`: Template base.
  - `index.html`: Página de cadastro de usuário.
  - `listar.html`: Página de listagem de usuários.
  - `delete.html`: Página de remoção de usuários.

## Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install flask
   ```
2. Navegue até o diretório do projeto.
3. Execute o aplicativo Flask:
   ```bash
   flask run
   ```
4. Acesse o aplicativo no seu navegador: `http://127.0.0.1:5000/`.

## Funcionalidades

- Cadastro de usuários com validação de formulário.
- Listagem de usuários cadastrados.
- Remoção de usuários. (Próximo passo)

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Faça um fork do repositório, implemente suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

