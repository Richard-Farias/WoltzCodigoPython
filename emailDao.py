import genericDAO


def salvarDadosAnexo(connect,txtAnexo):
    sql = "INSERT INTO TB_DADOS_ANEXOS (info_pdf_txt) VALUES (%s)"
    anexoTxt = [txtAnexo]
    connect.execute(sql,anexoTxt)
    genericDAO.connect.commit()
    print("Dados salvo com sucesso")

    connect.close()
    genericDAO.connect.close()