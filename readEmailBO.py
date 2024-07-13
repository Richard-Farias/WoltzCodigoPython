from datetime import datetime
from email.header import decode_header
import email

def lerEmail(objConnect):
    status, mensagens = objConnect.search(None, '(UNSEEN SUBJECT "CEMIG FATURA ONLINE")')

    if status == 'OK':
        for num in mensagens[0].split():    
            status, dados = objConnect.fetch(num, '(RFC822)')
            if status == 'OK':
                mensagem_raw = dados[0][1]
                mensagem = email.message_from_bytes(mensagem_raw)
                
                # Ler a data de envio do e-mail
                dataEnvioEmail = mensagem.get('Date')
                if dataEnvioEmail:
                    dataEnvioEmail = datetime.strptime(dataEnvioEmail, '%a, %d %b %Y %H:%M:%S %z')
                    print(f'Data de envio do e-mail: {dataEnvioEmail}')
                else:
                    print('Data de envio não encontrada no cabeçalho do e-mail.')
                    
                # Ler o assunto do e-mail
                assuntoEmail = decode_header(mensagem['Subject'])[0][0]
                if isinstance(assuntoEmail, bytes):
                    assuntoEmail = assuntoEmail.decode()
                print(f'Assunto: {assuntoEmail}')

                # Ler o corpo texto do e-mail
                if mensagem.is_multipart():
                    for parte in mensagem.walk():
                        conteudo_type = parte.get_content_type()
                        if conteudo_type == 'text/plain':
                            corpo = parte.get_payload(decode=True).decode()
                            print(f'Corpo do e-mail:\n{corpo}')
    else:
        print('Não foi possível acessar a caixa de entrada.')

   
   