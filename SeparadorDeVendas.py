import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import logging
import locale
import os

# Importa a função carregar_comissoes do arquivo comissoes.py
from comissoes import carregar_comissoes

# Definindo a configuração regional para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Configuração de log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Comissao:
    def __init__(self):
        self.comissoes = carregar_comissoes()

    def calcular_comissao(self, tipo_album, metodo_pagamento, valor_venda):
        if tipo_album not in self.comissoes:
            logging.warning(f"Tipo de álbum desconhecido: {tipo_album}")
            return 0

        if metodo_pagamento not in self.comissoes[tipo_album]:
            logging.warning(f"Método de pagamento desconhecido: {metodo_pagamento}")
            return 0

        porcentagem_comissao = self.comissoes[tipo_album][metodo_pagamento]
        comissao = (porcentagem_comissao / 100) * valor_venda
        return comissao


class SeparadorDeVendas:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.df = None
        self.comissao = Comissao()

    def carregar_dados(self):
        # Carrega os dados da planilha
        self.df = pd.read_excel(self.nome_arquivo)

    def tratar_nans(self):
        # Substitui valores NaN na coluna 'Tipo Venda' por 'Desconhecido'
        self.df.fillna({'Tipo Venda': 'Desconhecido'}, inplace=True)

    def calcular_comissoes(self):
        if self.df is None:
            raise Exception("Dados não carregados. Execute 'carregar_dados()' primeiro.")

        # Trata valores NaN
        self.tratar_nans()

        # Inicializa a coluna de Comissão
        self.df['Comissão'] = 0

        # Lista de colunas para calcular as comissões
        colunas_pagamento = ['A FATURAR', 'BOL', 'CC', 'CCRE', 'CD', 'CDEB', 'CTL', 'SGPAYFICTICIO', 'CSGP', 'CHQ',
                             'CHEMP', 'CMBA', 'DAUT', 'DEB', 'DEP', 'DEPONCONTA', 'DIN', 'DOC', 'PAGARME', 'PIX', 'PIXSGP2',
                             'RPAY', 'REP', 'STONEBSBCC', 'STCRED', 'STDEB', 'STONEEMPCC', 'TED', 'TRA']

        # Calcula a comissão para cada linha
        for idx, row in self.df.iterrows():
            tipo_album = row['Vendedor']
            for metodo_pagamento in colunas_pagamento:
                if metodo_pagamento in row and pd.notna(row[metodo_pagamento]) and row[metodo_pagamento] > 0:
                    valor_venda = row[metodo_pagamento]
                    comissao = self.comissao.calcular_comissao(tipo_album, metodo_pagamento, valor_venda)
                    self.df.at[idx, 'Comissão'] += comissao

    def separar_por_vendedor(self):
        if self.df is None:
            raise Exception("Dados não carregados. Execute 'carregar_dados()' primeiro.")

        # Agrupa os dados por Vendedor e calcula a soma dos Valores do Pedido e das Comissões
        vendas_por_vendedor = self.df.groupby('Vendedor').agg({
            'Valor do Pedido': 'sum',
            'Comissão': 'sum'
        }).reset_index()

        return vendas_por_vendedor

    def gerar_relatorio(self, nome_arquivo_saida):
        # Gera o relatório separado por vendedor e salva em uma nova planilha
        vendas_por_vendedor = self.separar_por_vendedor()
        vendas_por_vendedor.to_excel(nome_arquivo_saida, index=False)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Relatório de Vendas")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Selecione o arquivo de vendas:")
        self.label.pack(pady=10)

        self.button_select = tk.Button(self, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.button_select.pack(pady=5)

        self.button_calculate = tk.Button(self, text="Calcular Comissões", command=self.calcular_comissoes)
        self.button_calculate.pack(pady=5)

        self.button_show = tk.Button(self, text="Mostrar Resultados", command=self.mostrar_resultados)
        self.button_show.pack(pady=5)

        self.button_save = tk.Button(self, text="Salvar Relatório", command=self.salvar_relatorio)
        self.button_save.pack(pady=5)

        self.nome_arquivo = None
        self.separador = None

    def selecionar_arquivo(self):
        self.nome_arquivo = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if self.nome_arquivo:
            messagebox.showinfo("Arquivo Selecionado", f"Arquivo {os.path.basename(self.nome_arquivo)} selecionado com sucesso.")

    def calcular_comissoes(self):
        if not self.nome_arquivo:
            messagebox.showwarning("Nenhum arquivo selecionado", "Por favor, selecione um arquivo primeiro.")
            return

        self.separador = SeparadorDeVendas(self.nome_arquivo)
        self.separador.carregar_dados()
        self.separador.calcular_comissoes()
        messagebox.showinfo("Cálculo Concluído", "As comissões foram calculadas com sucesso!")

    def mostrar_resultados(self):
        if not self.separador:
            messagebox.showwarning("Dados não calculados", "Por favor, calcule as comissões primeiro.")
            return

        vendas_por_vendedor = self.separador.separar_por_vendedor()
        resultados_texto = "Vendas por Vendedor:\n\n"

        for _, row in vendas_por_vendedor.iterrows():
            vendedor = row['Vendedor']
            valor_vendas = locale.currency(row['Valor do Pedido'], grouping=True)
            comissao = locale.currency(row['Comissão'], grouping=True)
            resultados_texto += f"Vendedor: {vendedor}\nValor das Vendas: {valor_vendas}\nComissão: {comissao}\n\n"

        messagebox.showinfo("Resultados", resultados_texto)

    def salvar_relatorio(self):
        if not self.separador:
            messagebox.showwarning("Dados não calculados", "Por favor, calcule as comissões primeiro.")
            return

        nome_arquivo_saida = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if nome_arquivo_saida:
            self.separador.gerar_relatorio(nome_arquivo_saida)
            messagebox.showinfo("Relatório Salvo", f"Relatório salvo em {nome_arquivo_saida}.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
