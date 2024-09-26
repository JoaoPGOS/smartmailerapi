from flask import Flask, request, jsonify
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Função para validar o formato básico do e-mail
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(regex, email):
        return False
    return True

# Função para corrigir domínios comuns (exemplo: gnail -> gmail)
def correct_common_typos(email):
    corrections = {
        'gnail.com': 'gmail.com',
        'hotmial.com': 'hotmail.com',
        'yaho.com': 'yahoo.com',
    }
    user, domain = email.split('@')
    if domain in corrections:
        return f'{user}@{corrections[domain]}'
    return email

# Função para enviar o e-mail usando SMTP
def send_email(sender_email, sender_password, recipient_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conectando ao servidor SMTP e enviando o e-mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar TLS para segurança
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

@app.route('/send-emails', methods=['POST'])
def send_emails():
    data = request.json

    # Verifica se os parâmetros necessários estão presentes
    required_fields = ['sender_email', 'sender_password', 'emails', 'subject', 'body']
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"The request must contain {', '.join(required_fields)}"}), 400

    sender_email = data['sender_email']
    sender_password = data['sender_password']
    emails = data['emails']
    subject = data['subject']
    body = data['body']

    invalid_emails = []
    valid_emails = []
    failed_emails = []

    for email in emails:
        if not is_valid_email(email):
            invalid_emails.append(email)
        else:
            corrected_email = correct_common_typos(email)
            if send_email(sender_email, sender_password, corrected_email, subject, body):
                valid_emails.append(corrected_email)
            else:
                failed_emails.append(corrected_email)

    return jsonify({
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails,
        "failed_emails": failed_emails
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
