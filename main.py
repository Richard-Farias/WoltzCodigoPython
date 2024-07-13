import conectarEmail
import readEmailBO
import readAnexoEmailBO
import conectarGmail

objConnect = conectarEmail.conectarServidorEmail()


readEmailBO.lerEmail(objConnect)

readAnexoEmailBO.lerAnexoEmail(objConnect)

objConnect.logout()

