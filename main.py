import conectarEmail
import readEmailBO
import readAnexoEmailBO

objConnect = conectarEmail.conectarServidorEmail()

readEmailBO.lerEmail(objConnect)

readAnexoEmailBO.lerAnexoEmail(objConnect)

objConnect.logout()

