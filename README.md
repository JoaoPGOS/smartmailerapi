# API de Envio de E-mails

Esta API Flask permite o envio de e-mails para múltiplos destinatários. Ela realiza validação de e-mails, corrige erros comuns (como "gnail.com" para "gmail.com") e envia e-mails usando um servidor SMTP. O remetente e a senha são fornecidos diretamente na requisição.

## **Instalação**

### **Requisitos**
- Python 3.x
- Bibliotecas Python:
    - Flask
    - requests
    - smtplib
    - email (padrão no Python)

### **Passos para Instalação**
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-repositorio/email-api.git
    cd email-api
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install Flask requests
    ```

4. Execute o servidor Flask:
    ```bash
    python app.py
    ```

5. Acesse a API em `http://localhost:5000/`.

## **Endpoint**

### **1. POST /send-emails**

Esse endpoint permite enviar um e-mail para múltiplos destinatários após validar e corrigir erros comuns de digitação.

#### **Requisição**

- **URL:** `/send-emails`
- **Método:** `POST`
- **Cabeçalhos:**
    - `Content-Type: application/json`

- **Body (JSON):**

```json
{
    "sender_email": "seuemail@gmail.com",
    "sender_password": "sua_senha_de_aplicativo",
    "emails": [
        "joao@gnail.com",
        "maria@hotmial.com",
        "invalido.com",
        "ana@yahoo.com"
    ],
    "subject": "Assunto do E-mail",
    "body": "Corpo do e-mail"
}
