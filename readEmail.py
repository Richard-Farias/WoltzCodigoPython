import imaplib
import email
import PyPDF2
import genericDAO
import emailDao


#Conectando servidor de serviço de email com o IMAP
objConnect = imaplib.IMAP4_SSL("imap.outlook.com") 
# Login e senha para entrada no email
login = "sibliondesenv@outlook.com"
password = "sib788005"

objConnect.login(login,password)
objConnect.list()
objConnect.select(mailbox= 'inbox',readonly=True)
resposta,idEmail = objConnect.search(None,'All')

#Percorre e-mails na caixa de entrada e decodifca linhas:16 a 20
for id in idEmail[0].split():   
    result,dates = objConnect.fetch(id,'RFC822')
    txt_email =  dates[0][1]
    txt_email = txt_email.decode('utf-8')
    txt_email = email.message_from_string(txt_email)
    
#Percorre partes dos e-mails e verificando se há anexo linhas 22 a 23
    for part in txt_email.walk():
      if part.get_content_maintype == 'multipart':
         continue
      if part.get('content-Disposition') is None:
         continue
      fileName = part.get_filename()

    # criando uma arquivo com mesmo nome do anexo na pasta local
      file = open(fileName,'wb')

    # Escrevendo  bináriio do anexo no arquivo
    dateAnx = file.write(part.get_payload(decode=True))
  

readPdf =  PyPDF2.PdfReader(fileName)
txt = "" 

for page in readPdf.pages:
   txt += page.extract_text()
 
connect = genericDAO.connectDao(txt)
emailDao.salvarDadosAnexo(connect,txt)

#print(txt)
