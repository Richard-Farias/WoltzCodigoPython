from imap_tools import MailBox,AND

user = "sibliondesenv@outlook.com"
password = "sib788005"

email = MailBox("imap.outlook.com").login(user,password)

list_emails =  email.fetch(AND(new=True,subject= "CEMIG FATURA ONLINE"))

for email in list_emails:
    print(email.subject)
    print(email.text)
    email.attachments
    if len(email.attachments) > 0 :
        for anexo in email.attachments:
            if "TesteAnexo" in anexo.filename:
                info_anexo = anexo.payload
                with open("AnexoTesteWolts.pdf","wb") as anexo_email:
                    anexo_email.write(info_anexo)