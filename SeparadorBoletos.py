import logging
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import json
from typing import Dict, Any
from comissoes import carregar_comissoes
logging.basicConfig(level=logging.WARNING)

class Comissao:
    def __init__(self):
        self.comissoes = carregar_comissoes()

    def calcular_comissao(self, vendedor, carteira, valor):
        if vendedor not in self.comissoes:
            logging.warning(f"Vendedor desconhecido: {vendedor}")
            return 0

        if carteira not in self.comissoes[vendedor]:
            logging.warning(f"Carteira desconhecida para {vendedor}: {carteira}")
            return 0

        porcentagem_comissao = self.comissoes[vendedor][carteira]
        comissao = (porcentagem_comissao / 100) * valor
        return comissao

def gerar_relatorio(arquivo_xlsx: str) -> pd.DataFrame:
    df = pd.read_excel(arquivo_xlsx, engine='openpyxl')
    comissao_calculator = Comissao()
    
    # Inicializar a coluna de Comissão com zeros
    df['Comissão'] = 0

    # Calcular comissões
    for idx, row in df.iterrows():
        vendedor = row['Vendedor']
        carteira = row['Carteira']
        valor = row['Valor']
        comissao = comissao_calculator.calcular_comissao(vendedor, carteira, valor)
        df.at[idx, 'Comissão'] = comissao

    df['Valor do Crédito'] = df['Valor'] - df['Comissão']
    
    # Agrupando por Vendedor e Carteira
    colunas_agg = {
        'Valor': 'sum',
        'Comissão': 'sum',
        'Valor do Crédito': 'sum'
    }

    relatorio = df.groupby(['Vendedor', 'Carteira']).agg(colunas_agg).reset_index()
    
    relatorio['Taxa de Comissão Média (%)'] = (relatorio['Comissão'] / relatorio['Valor']) * 100
    
    return relatorio

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gerador de Relatório de Vendas e Comissões")
        self.geometry("1200x700")
        self.configure(bg='#f0f0f0')
        
        self.create_widgets()
    
    def create_widgets(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        
        # Configurações de estilo
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('TLabel', font=('Arial', 10), background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')

        # Frame principal
        main_frame = ttk.Frame(self, padding="10 10 10 10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        ttk.Label(main_frame, text="Gerador de Relatório de Vendas e Comissões", style='Header.TLabel').pack(pady=10)

        # Frame para seleção de arquivo
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=10)
        
        self.file_path = tk.StringVar()
        ttk.Label(file_frame, text="Arquivo XLSX:").pack(side='left', padx=(0, 10))
        ttk.Entry(file_frame, textvariable=self.file_path, width=50).pack(side='left', padx=(0, 10))
        ttk.Button(file_frame, text="Selecionar Arquivo", command=self.select_file).pack(side='left')
        
        # Frame para botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Gerar Relatório", command=self.generate_report).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Salvar Relatório", command=self.save_report).pack(side='left', padx=5)
        
        # Frame para a Treeview
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Treeview para exibir o relatório
        self.tree = ttk.Treeview(tree_frame, show='headings', style='Treeview')
        self.tree.pack(side='left', fill=tk.BOTH, expand=True)
        
        # Scrollbars para o Treeview
        y_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        y_scrollbar.pack(side='right', fill='y')
        x_scrollbar = ttk.Scrollbar(main_frame, orient='horizontal', command=self.tree.xview)
        x_scrollbar.pack(side='bottom', fill='x')
        self.tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        
        # Barra de status
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if filename:
            self.file_path.set(filename)
            self.status_var.set(f"Arquivo selecionado: {filename}")
    
    def generate_report(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo XLSX.")
            return
        
        try:
            relatorio = gerar_relatorio(file_path)
            self.display_report(relatorio)
            self.status_var.set("Relatório gerado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o relatório: {str(e)}")
            self.status_var.set("Erro ao gerar relatório.")
    
    def display_report(self, relatorio):
        # Configurar as colunas do Treeview
        colunas = list(relatorio.columns)
        self.tree["columns"] = colunas
        for col in colunas:
            self.tree.heading(col, text=col, anchor=tk.W)
            self.tree.column(col, width=100, anchor=tk.W)  # Ajuste a largura conforme necessário
        
        # Limpar a Treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Inserir os dados na Treeview
        for _, row in relatorio.iterrows():
            values = []
            for col in colunas:
                if col == 'Taxa de Comissão (%)':
                    values.append(f"{row[col]:.2f}%")
                elif 'Valor' in col or 'Comissão' in col:
                    values.append(f"R$ {row[col]:.2f}")
                else:
                    values.append(str(row[col]))
            self.tree.insert("", "end", values=values)
    
    def save_report(self):
        if not self.tree.get_children():
            messagebox.showerror("Erro", "Não há relatório para salvar. Por favor, gere um relatório primeiro.")
            return
        
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if filename:
            data = []
            for item in self.tree.get_children():
                data.append(self.tree.item(item)['values'])
            
            df = pd.DataFrame(data, columns=self.tree["columns"])
            df.to_excel(filename, index=False, engine='openpyxl')
            messagebox.showinfo("Sucesso", f"Relatório salvo com sucesso em {filename}")
            self.status_var.set(f"Relatório salvo em {filename}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()