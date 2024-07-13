from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
import pickle
import conectarEmail

SCOPES = ['https://mail.google.com/']

def main():
    creds = None

    # O arquivo token.pickle armazena os tokens de usuário e os atualiza automaticamente quando necessário.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Se não houver credenciais válidas disponíveis, solicitará ao usuário fazer login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Salva as credenciais no arquivo token.pickle para a próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # creds para acessar as APIs do Gmail
if __name__ == '__main__':
    main()
#conectarEmail()