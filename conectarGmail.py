import imaplib

def conectarServidorEmail():
  #Conectando servidor de serviço de email com o IMAP
  objConnect = imaplib.IMAP4_SSL("imap.outlook.com") 
    # Login e senha para entrada no email
  login = "sibliondesenv@gmail.com"
  password = "sib788005"

  objConnect.login(login,password)
  objConnect.list()
  objConnect.select(mailbox= 'inbox',readonly=True)
    # resposta,idEmail = objConnect.search(None,'All')
  return objConnect