# nao esquecer de habilitar a senha no google


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>bom diaaa renato</p>
    <p>como voce esta?</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'renato.mota.costa@gmail.com'
    msg['To'] = 'renato.mota.costa@gmail.com'
    password = '' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')



enviar_email()
