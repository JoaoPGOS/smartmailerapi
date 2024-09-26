import requests

# URL da API Flask que você criou
url = 'http://localhost:5000/send-emails'

# Dados da requisição
payload = {
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

# Fazendo a requisição POST
response = requests.post(url, json=payload)

# Exibindo a resposta da API
print(f'Status Code: {response.status_code}')
print('Response JSON:', response.json())
