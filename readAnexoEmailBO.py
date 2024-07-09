import email
import PyPDF2

listaDoc = []
def lerAnexoEmail(objConnect):
    status, mensagens = objConnect.search(None, '(UNSEEN SUBJECT "Cemig")')
    if status == 'OK':
        for id in mensagens[0].split():   
            result,dates = objConnect.fetch(id,'RFC822')
            txt_email =  dates[0][1]
            txt_email = txt_email.decode('utf-8')
            txt_email = email.message_from_string(txt_email)
        
        #Percorre partes dos e-mails e verificando se há anexo 
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
         listaDoc.append(txt)