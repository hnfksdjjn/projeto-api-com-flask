# projeto-api-com-flask

Este projeto é uma API construída com Flask que permite gerenciar notícias. Ele inclui operações CRUD (Create, Read, Update e Delete) para notícias e suporte para adicionar várias notícias de uma só vez. Aqui está uma explicação de cada parte:

---

### **Parte 1: Arquivo `routes.py`**
Este arquivo define as rotas da API. Cada rota realiza uma operação específica no banco de dados.

1. **`/news` (GET)**  
   Recupera todas as notícias armazenadas no banco de dados.  
   **Exemplo de resposta**:
   ```json
   [
       {"id": 1, "title": "Notícia 1", "content": "Conteúdo da notícia 1", "date_created": "2024-12-13T10:00:00"}
   ]
   ```

2. **`/news` (POST)**  
   Adiciona uma nova notícia ao banco de dados.  
   **Payload esperado**:
   ```json
   {"title": "Nova Notícia", "content": "Conteúdo da notícia"}
   ```

3. **`/news/<int:id>` (PUT)**  
   Atualiza uma notícia existente, identificada pelo `id`.  
   **Payload esperado** (pelo menos um campo é obrigatório):
   ```json
   {"title": "Título Atualizado", "content": "Conteúdo Atualizado"}
   ```

4. **`/news/<int:id>` (DELETE)**  
   Remove uma notícia do banco de dados usando o `id`.

5. **`/news/bulk` (POST)**  
   Adiciona múltiplas notícias de uma vez.  
   **Payload esperado**:
   ```json
   [
       {"title": "Notícia 1", "content": "Conteúdo 1"},
       {"title": "Notícia 2", "content": "Conteúdo 2"}
   ]
   ```

---

### **Parte 2: Arquivo `models.py`**
Define a estrutura do banco de dados com SQLAlchemy.

- **Classe `News`**:  
  Representa a tabela de notícias no banco de dados. Contém os seguintes campos:
  - `id`: Identificador único da notícia (chave primária).
  - `title`: Título da notícia (obrigatório, até 100 caracteres).
  - `content`: Conteúdo da notícia (obrigatório, sem limite definido).
  - `date_created`: Data e hora da criação (preenchido automaticamente).

---

### **Parte 3: Arquivo `config.py`**
Configura o Flask com os detalhes do banco de dados.

- **`SQLALCHEMY_DATABASE_URI`**:  
  Define o endereço do banco de dados MySQL.
  ```
  mysql+mysqlconnector://usuario:senha@host:porta/nome_banco
  ```
  Exemplo: `mysql+mysqlconnector://root:edson@localhost:3306/noticia`

- **`SQLALCHEMY_TRACK_MODIFICATIONS`**:  
  Desativa notificações de alterações no banco (melhor performance).

---

### **Parte 4: Arquivo principal**
Configura e inicia a aplicação Flask.

1. **`app.config.from_object(Config)`**  
   Aplica a configuração definida no `config.py`.

2. **`db.init_app(app)`**  
   Inicializa o SQLAlchemy com o app Flask.

3. **`db.create_all()`**  
   Cria as tabelas no banco de dados (executado na inicialização, útil para ambientes de desenvolvimento).

4. **`app.register_blueprint(routes)`**  
   Registra as rotas definidas no `routes.py`.

5. **`app.run(debug=True)`**  
   Inicia o servidor Flask em modo de depuração.

---

### **Fluxo de trabalho com Postman e Workbench**
1. **Workbench (Banco de Dados)**:
   - Configure a conexão com o MySQL no Workbench.
   - Use o nome do banco `noticia` para visualizar as tabelas criadas.
   - ![dados da api no banco de dados](https://github.com/user-attachments/assets/07b2823e-1d7b-40f1-9484-0fea9a63dc40)


2. **Postman (Testar Endpoints)**:
   - **GET `/news`**: Recupera todas as notícias.
   - ![postmam1](https://github.com/user-attachments/assets/bfbed994-54bd-4d59-bcc0-3745e90980ed)

   - **POST `/news`**: Envia um JSON para adicionar uma nova notícia.
   - **PUT `/news/<id>`**: Atualiza uma notícia específica.
   - ![postmam3](https://github.com/user-attachments/assets/335f6f18-fc5b-4879-9687-3333c05ffbca)

   - **DELETE `/news/<id>`**: Remove uma notícia.
   - ![postmam4](https://github.com/user-attachments/assets/dab545a2-7c99-4391-85dc-dfe49a31aee2)

   - **POST `/news/bulk`**: Adiciona várias notícias ao mesmo tempo.
   - ![postmam2](https://github.com/user-attachments/assets/b457c0e2-6fb3-4c5e-93dd-a9d2c4edae46)
