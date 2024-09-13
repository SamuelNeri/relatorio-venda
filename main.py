import tkinter as tk
from tkinter import ttk
import SeparadorBoletos
import SeparadorDeVendas

class SistemaUnificado(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema Unificado de Relatórios de Vendas")
        self.geometry("300x200")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Estilo
        style = ttk.Style(self)
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Escolha um Sistema", font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Botões
        ttk.Button(main_frame, text="Separador de Boletos", command=self.open_separador_boleto).pack(fill=tk.X, pady=5)
        ttk.Button(main_frame, text="Separador de Vendas", command=self.open_separador_vendas).pack(fill=tk.X, pady=5)
    
    def find_main_class(self, module):
        # Encontra a primeira classe no módulo que herda de tk.Tk
        return next(obj for name, obj in vars(module).items() 
                    if isinstance(obj, type) and issubclass(obj, tk.Tk))
    
    def open_separador_boleto(self):
        self.withdraw()  # Esconde a janela principal
        app_class = self.find_main_class(SeparadorBoletos)
        app = app_class()
        app.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(app))
        app.mainloop()
    
    def open_separador_vendas(self):
        self.withdraw()  # Esconde a janela principal
        app_class = self.find_main_class(SeparadorDeVendas)
        app = app_class()
        app.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(app))
        app.mainloop()
    
    def on_closing(self, app):
        app.destroy()
        self.deiconify()  # Mostra a janela principal novamente

if __name__ == "__main__":
    app = SistemaUnificado()
    app.mainloop()