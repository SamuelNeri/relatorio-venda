import json

COMISSOES_JSON = '''{
    "NG": {
        "A FATURAR": 0,
        "BOL": 12,
        "Boleto Negativado": 5,
        "Boleto Com Restrição": 5,
        "CC": 20,
        "CCRE": 20,
        "CD": 20,
        "CDEB": 20,
        "CTL": 0,
        "SGPAYFICTICIO": 20,
        "CSGP": 19,
        "CHQ": 23,
        "CHEMP": 23,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 20,
        "DEP": 23,
        "DEPONCONTA": 23,
        "DIN": 24,
        "DOC": 0,
        "PAGARME": 19,
        "PIX": 23,
        "PIXSGP2": 23,
        "RPAY": 19,
        "REP": 0,
        "STONEBSBCC": 20,
        "STCRED": 20,
        "STDEB": 20,
        "STONEEMPCC": 20,
        "TED": 23,
        "TRA": 23,
        "Desconhecido": 0
    },
    "Rebolo": {
        "A FATURAR": 0,
        "BOL": 8,
        "Boleto Negativado": 5,
        "Boleto Com Restrição": 8,
        "CC": 35,
        "CCRE": 35,
        "CD": 35,
        "CDEB": 35,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 34,
        "CHQ": 43,
        "CHEMP": 43,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 35,
        "DEP": 43,
        "DEPONCONTA": 23,
        "DIN": 44,
        "DOC": 0,
        "PAGARME": 35,
        "PIX": 43,
        "PIXSGP2": 43,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 35,
        "STCRED": 35,
        "STDEB": 35,
        "STONEEMPCC": 35,
        "TED": 43,
        "TRA": 43,
        "Desconhecido": 0
    },
    "Apaulista": {
        "A FATURAR": 0,
        "BOL": 8,
        "CC": 13,
        "CCRE": 13,
        "CD": 15,
        "CDEB": 15,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 12,
        "CHQ": 16,
        "CHEMP": 23,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 15,
        "DEP": 17,
        "DEPONCONTA": 17,
        "DIN": 20,
        "DOC": 0,
        "PAGARME": 13,
        "PIX": 17,
        "PIXSGP2": 17,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 13,
        "STCRED": 13,
        "STDEB": 15,
        "STONEEMPCC": 13,
        "TED": 17,
        "TRA": 17,
        "Desconhecido": 0
    },
    "LR Formaturas (Lucas)": {
        "A FATURAR": 0,
        "BOL": 7,
        "Boleto Com Restrição": 5,
        "CC": 11,
        "CCRE": 10,
        "CD": 12,
        "CDEB": 12,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 10,
        "CHQ": 14,
        "CHEMP": 14,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 12,
        "DEP": 22,
        "DEPONCONTA": 22,
        "DIN": 17,
        "DOC": 0,
        "PAGARME": 10,
        "PIX": 22,
        "PIXSGP2": 22,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 11,
        "STCRED": 11,
        "STDEB": 12,
        "STONEEMPCC": 11,
        "TED": 22,
        "TRA": 2,
        "Desconhecido": 0
    },
    "Linha de Frente (Virgem)": {
        "A FATURAR": 0,
        "BOL": 12,
        "SGPay": 12,
        "Boleto Negativado": 5,
        "Boleto Com Restrição": 8,
        "CC": 13,
        "CCRE": 13,
        "CD": 15,
        "CDEB": 15,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 12,
        "CHQ": 16,
        "CHEMP": 23,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 15,
        "DEP": 17,
        "DEPONCONTA": 17,
        "DIN": 20,
        "DOC": 0,
        "PAGARME": 13,
        "PIX": 17,
        "PIXSGP2": 17,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 13,
        "STCRED": 13,
        "STDEB": 15,
        "STONEEMPCC": 13,
        "TED": 17,
        "TRA": 17,
        "Desconhecido": 0
    },
    "Linha de Frente (5°Ano/Infantil)": {
        "A FATURAR": 0,
        "BOL": 7,
        "Boleto Negativado": 0,
        "Boleto Com Restrição": 5,
        "CC": 18,
        "CCRE": 18,
        "CD": 20,
        "CDEB": 20,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 17,
        "CHQ": 21,
        "CHEMP": 21,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 20,
        "DEP": 22,
        "DEPONCONTA": 22,
        "DIN": 25,
        "DOC": 0,
        "PAGARME": 18,
        "PIX": 25,
        "PIXSGP2": 25,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 18,
        "STCRED": 18,
        "STDEB": 18,
        "STONEEMPCC": 18,
        "TED": 22,
        "TRA": 22,
        "Desconhecido": 0
    },
    "Pacote Antecipado (Jailson)": {
        "A FATURAR": 0,
        "BOL": 4,
        "Boleto Negativado": 0,
        "Boleto Com Restrição": 3,
        "CC": 6,
        "CCRE": 6,
        "CD": 6,
        "CDEB": 6,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 6,
        "CHQ": 6,
        "CHEMP": 6,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 6,
        "DEP": 6,
        "DEPONCONTA": 7,
        "DIN": 8,
        "DOC": 0,
        "PAGARME": 6,
        "PIX": 8,
        "PIXSGP2": 8,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 6,
        "STCRED": 6,
        "STDEB": 6,
        "STONEEMPCC": 6,
        "TED": 7,
        "TRA": 7,
        "Desconhecido": 0
    }, 
    "Pacote Antecipado (Kleber)": {
        "A FATURAR": 0,
        "Boleto Negativado": 0,
        "Boleto Com Restrição": 3,
        "BOL": 4,
        "CC": 5,
        "CCRE": 5,
        "CD": 6,
        "CDEB": 6,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 5,
        "CHQ": 6,
        "CHEMP": 6,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 6,
        "DEP": 6,
        "DEPONCONTA": 7,
        "DIN": 8,
        "DOC": 0,
        "PAGARME": 6,
        "PIX": 8,
        "PIXSGP2": 8,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 6,
        "STCRED": 6,
        "STDEB": 6,
        "STONEEMPCC": 6,
        "TED": 7,
        "TRA": 7,
        "Desconhecido": 0
    },
    "Kleber Borges": {
        "A FATURAR": 0,
        "BOL": 4,
        "Boleto Negativado": 0,
        "Boleto Com Restrição": 3,
        "CC": 5,
        "CCRE": 5,
        "CD": 6,
        "CDEB": 6,
        "CTL": 0,
        "SGPAYFICTICIO": 0,
        "CSGP": 5,
        "CHQ": 6,
        "CHEMP": 6,
        "CMBA": 0,
        "DAUT": 0,
        "DEB": 6,
        "DEP": 6,
        "DEPONCONTA": 7,
        "DIN": 8,
        "DOC": 0,
        "PAGARME": 6,
        "PIX": 8,
        "PIXSGP2": 8,
        "RPAY": 0,
        "REP": 0,
        "STONEBSBCC": 6,
        "STCRED": 6,
        "STDEB": 6,
        "STONEEMPCC": 6,
        "TED": 7,
        "TRA": 7,
        "Desconhecido": 0
    }
}
'''

def carregar_comissoes():
    try:
        return json.loads(COMISSOES_JSON)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao identificar o JSON: {str(e)}")