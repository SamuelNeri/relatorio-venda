import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
from ttkthemes import ThemedTk
import pandas as pd
import webbrowser
from PIL import Image, ImageTk
import os
from analyzer import SalesAnalyzer
from excel_exporter import ExcelExporter

class SalesAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Análise de Vendas")
        
        # Initialize analyzer
        self.analyzer = SalesAnalyzer()
        
        # Apply theme configuration
        self.style = ttk.Style()
        self.style.configure("Preview.Treeview", rowheight=25)
        self.style.configure("TNotebook.Tab", padding=[12, 8])
        self.style.configure("Menu.TFrame", background='#f0f0f0')
        self.style.configure("MenuButton.TButton", padding=10)
        self.style.configure("Developer.TLabel", font=('Helvetica', 8), foreground='#666666')
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(expand=True, fill='both')
        
        # Setup GUI elements
        self.setup_menu()
        self.setup_content_area()
        
    def setup_menu(self):
        # Create menu frame
        menu_frame = ttk.Frame(self.main_container, style="Menu.TFrame")
        menu_frame.pack(side='left', fill='y', padx=10, pady=10)
        
        # Load and display icon
        try:
            # Carrega o ícone SVG usando PIL
            icon_path = os.path.join('assets', 'icon.svg')
            if os.path.exists(icon_path):
                # Converte SVG para PhotoImage
                from cairosvg import svg2png
                from io import BytesIO
                
                png_data = BytesIO()
                svg2png(url=icon_path, write_to=png_data, output_width=64, output_height=64)
                png_data.seek(0)
                
                icon_image = Image.open(png_data)
                photo = ImageTk.PhotoImage(icon_image)
                
                icon_label = ttk.Label(menu_frame, image=photo)
                icon_label.image = photo  # Keep a reference!
                icon_label.pack(pady=(0, 10))
        except Exception as e:
            print(f"Erro ao carregar ícone: {str(e)}")
        
        # Add company logo/name placeholder
        logo_label = ttk.Label(menu_frame, text="Sistema de\nAnálise de Vendas", justify='center')
        logo_label.pack(pady=(0, 20))
        
        # Relatórios section
        reports_label = ttk.Label(menu_frame, text="RELATÓRIOS", font=('Helvetica', 10, 'bold'))
        reports_label.pack(pady=(0, 10))
        
        # Relatório de Valores button
        self.valores_btn = ttk.Button(
            menu_frame,
            text="Relatório de Valores",
            command=self.show_valores_report,
            style="MenuButton.TButton",
            width=25
        )
        self.valores_btn.pack(pady=5)
        
        # Relatório de Produtos button
        self.produtos_btn = ttk.Button(
            menu_frame,
            text="Relatório de Produtos",
            command=self.show_produtos_report,
            style="MenuButton.TButton",
            width=25
        )
        self.produtos_btn.pack(pady=5)
        
        # Separator
        ttk.Separator(menu_frame, orient='horizontal').pack(fill='x', pady=20)
        
        # Suporte section
        support_label = ttk.Label(menu_frame, text="SUPORTE", font=('Helvetica', 10, 'bold'))
        support_label.pack(pady=(0, 10))
        
        # Suporte Técnico button
        self.support_btn = ttk.Button(
            menu_frame,
            text="Dúvidas e Suporte",
            command=self.show_support,
            style="MenuButton.TButton",
            width=25
        )
        self.support_btn.pack(pady=5)
        
        # Add developer credits at the bottom
        # Create a frame for the developer info to push it to the bottom
        dev_frame = ttk.Frame(menu_frame)
        dev_frame.pack(side='bottom', pady=20)
        
        dev_label = ttk.Label(
            dev_frame,
            text="Desenvolvido por Samuel Neri",
            style="Developer.TLabel",
            justify='center'
        )
        dev_label.pack()
        
    def setup_content_area(self):
        # Create content frame
        self.content_frame = ttk.Frame(self.main_container)
        self.content_frame.pack(side='right', expand=True, fill='both', padx=10, pady=10)
        
        # Create card frames for different sections
        self.welcome_frame = self.create_welcome_frame()
        self.valores_frame = self.create_valores_frame()
        self.produtos_frame = self.create_produtos_frame()
        self.support_frame = self.create_support_frame()
        
        # Show welcome frame by default
        self.show_welcome()
        
    def create_welcome_frame(self):
        frame = ttk.Frame(self.content_frame)
        
        # Welcome message
        welcome_label = ttk.Label(
            frame,
            text="Bem-vindo ao Sistema de Análise de Vendas",
            font=('Helvetica', 16, 'bold')
        )
        welcome_label.pack(pady=20)
        
        # Instructions
        instructions = """
        Selecione uma opção no menu lateral para começar:
        
        • Relatório de Valores - Análise financeira detalhada das vendas
        • Relatório de Produtos - Análise detalhada dos produtos vendidos
        • Dúvidas e Suporte - Acesso ao suporte técnico e documentação
        """
        
        inst_label = ttk.Label(frame, text=instructions, justify='left')
        inst_label.pack(pady=20)
        
        return frame
        
    def create_valores_frame(self):
        frame = ttk.Frame(self.content_frame)
        
        # Create notebook for operations and preview
        self.main_notebook = ttk.Notebook(frame)
        self.main_notebook.pack(expand=True, fill='both', pady=(0, 10))
        
        # Operations tab
        operations_frame = ttk.Frame(self.main_notebook, padding="10")
        self.main_notebook.add(operations_frame, text="Operações")
        
        # Report Preview tab
        report_preview_frame = ttk.Frame(self.main_notebook, padding="10")
        self.main_notebook.add(report_preview_frame, text="Pré-visualização do Relatório")
        
        # Setup operations tab
        self.setup_operations_tab(operations_frame)
        self.setup_report_preview_tab(report_preview_frame)
        
        return frame
        
    def create_produtos_frame(self):
        frame = ttk.Frame(self.content_frame)
        
        # Em desenvolvimento message
        dev_label = ttk.Label(
            frame,
            text="Relatório de Produtos\n\nEm desenvolvimento...",
            font=('Helvetica', 14),
            justify='center'
        )
        dev_label.pack(expand=True)
        
        return frame
        
    def create_support_frame(self):
        frame = ttk.Frame(self.content_frame)
        
        # Support title
        support_title = ttk.Label(
            frame,
            text="Suporte Técnico",
            font=('Helvetica', 16, 'bold')
        )
        support_title.pack(pady=20)
        
        # Support options frame
        options_frame = ttk.Frame(frame)
        options_frame.pack(expand=True, fill='both', padx=20)
        
        # Documentation button
        doc_btn = ttk.Button(
            options_frame,
            text="Acessar Documentação",
            command=lambda: webbrowser.open("https://docs.example.com"),
            width=30
        )
        doc_btn.pack(pady=10)
        
        # FAQ button
        faq_btn = ttk.Button(
            options_frame,
            text="Perguntas Frequentes (FAQ)",
            command=lambda: webbrowser.open("https://faq.example.com"),
            width=30
        )
        faq_btn.pack(pady=10)
        
        # Contact support button
        contact_btn = ttk.Button(
            options_frame,
            text="Contatar Suporte",
            command=lambda: webbrowser.open("mailto:support@example.com"),
            width=30
        )
        contact_btn.pack(pady=10)
        
        return frame
        
    def setup_operations_tab(self, parent):
        # Load Data Button
        load_btn = ttk.Button(
            parent, 
            text="Carregar Dados", 
            command=self.load_data,
            style="Accent.TButton"
        )
        load_btn.pack(pady=5, fill='x')
        
        # Generate Report Button
        report_btn = ttk.Button(
            parent, 
            text="Gerar Relatório", 
            command=self.generate_report,
            style="Accent.TButton"
        )
        report_btn.pack(pady=5, fill='x')
        
        # Status frame
        self.status_frame = ttk.LabelFrame(parent, text="Status", padding="10")
        self.status_frame.pack(pady=10, fill='x')
        
        self.status_label = ttk.Label(self.status_frame, text="Aguardando carregamento de dados...")
        self.status_label.pack()

    def setup_report_preview_tab(self, parent):
        # Create notebook for report sections
        self.preview_notebook = ttk.Notebook(parent)
        self.preview_notebook.pack(expand=True, fill='both')
        
        # Create frames for each preview section
        self.vendas_frame = ttk.Frame(self.preview_notebook)
        self.resumo_frame = ttk.Frame(self.preview_notebook)
        self.vendedor_frame = ttk.Frame(self.preview_notebook)
        self.pagamentos_frame = ttk.Frame(self.preview_notebook)
        self.instituicao_frame = ttk.Frame(self.preview_notebook)
        
        # Add frames to notebook
        self.preview_notebook.add(self.vendas_frame, text="Vendas")
        self.preview_notebook.add(self.resumo_frame, text="Resumo")
        self.preview_notebook.add(self.vendedor_frame, text="Análise por Vendedor")
        self.preview_notebook.add(self.pagamentos_frame, text="Pagamentos")
        self.preview_notebook.add(self.instituicao_frame, text="Instituição/Curso")
        
        # Setup each preview section
        self._setup_vendas_preview(self.vendas_frame)
        self._setup_resumo_preview(self.resumo_frame)
        self._setup_vendedor_preview(self.vendedor_frame)
        self._setup_pagamentos_preview(self.pagamentos_frame)
        self._setup_instituicao_preview(self.instituicao_frame)
        
        # Add refresh button at the top
        refresh_btn = ttk.Button(
            parent,
            text="Atualizar Visualização",
            command=self.refresh_all_previews,
            style="Accent.TButton"
        )
        refresh_btn.pack(pady=(0, 10))

    def _create_treeview(self, parent, columns):
        """Helper method to create a consistent treeview"""
        tree = ttk.Treeview(
            parent,
            columns=columns,
            show='headings',
            style="Preview.Treeview"
        )
        
        # Configure scrollbars
        y_scroll = ttk.Scrollbar(parent, orient='vertical', command=tree.yview)
        x_scroll = ttk.Scrollbar(parent, orient='horizontal', command=tree.xview)
        
        # Configure treeview
        tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        # Setup grid
        tree.grid(row=0, column=0, sticky='nsew')
        y_scroll.grid(row=0, column=1, sticky='ns')
        x_scroll.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, minwidth=50)
            
        return tree

    def _setup_vendas_preview(self, parent):
        columns = ['Num. Pedido', 'Cliente', 'Vendedor', 'Valor do Pedido', 'Tipo Pagamento', 'Comissao']
        self.vendas_tree = self._create_treeview(parent, columns)

    def _setup_resumo_preview(self, parent):
        columns = ['Métrica', 'Valor']
        self.resumo_tree = self._create_treeview(parent, columns)

    def _setup_vendedor_preview(self, parent):
        columns = ['Vendedor', 'Total Vendas', 'Número de Pedidos', 'Total Comissões', 'Média por Pedido']
        self.vendedor_tree = self._create_treeview(parent, columns)

    def _setup_pagamentos_preview(self, parent):
        columns = ['Método de Pagamento', 'Valor Total', 'Número de Pedidos', 'Percentual']
        self.pagamentos_tree = self._create_treeview(parent, columns)

    def _setup_instituicao_preview(self, parent):
        columns = ['Instituição', 'Curso', 'Total Vendas', 'Número de Pedidos', 'Percentual de Vendas']
        self.instituicao_tree = self._create_treeview(parent, columns)

    def refresh_all_previews(self):
        """Update all preview sections"""
        if self.analyzer.df is None:
            messagebox.showwarning("Aviso", "Nenhum dado carregado para visualizar!")
            return
            
        self._refresh_vendas_preview()
        self._refresh_resumo_preview()
        self._refresh_vendedor_preview()
        self._refresh_pagamentos_preview()
        self._refresh_instituicao_preview()

    def _refresh_vendas_preview(self):
        """Update vendas preview"""
        for item in self.vendas_tree.get_children():
            self.vendas_tree.delete(item)
            
        preview_data = self.analyzer.df.head(100)  # Show first 100 rows
        for idx, row in preview_data.iterrows():
            values = [
                str(row['Num. Pedido']),
                str(row['Cliente']),
                str(row['Vendedor']),
                f"R$ {row['Valor do Pedido']:,.2f}",
                str(row['Tipo Pagamento']),
                f"R$ {row['Comissao']:,.2f}"
            ]
            self.vendas_tree.insert('', 'end', values=values)

    def _refresh_resumo_preview(self):
        """Update resumo preview"""
        for item in self.resumo_tree.get_children():
            self.resumo_tree.delete(item)
            
        metrics, _ = self.analyzer.calculate_metrics()
        for metric, value in metrics.items():
            if isinstance(value, (int, float)):
                formatted_value = f"R$ {value:,.2f}" if "Total" in metric or "Média" in metric else f"{value:,.0f}"
                self.resumo_tree.insert('', 'end', values=[metric, formatted_value])
    
    def _refresh_vendedor_preview(self):
        """Update vendedor preview"""
        for item in self.vendedor_tree.get_children():
            self.vendedor_tree.delete(item)
            
        _, vendor_metrics = self.analyzer.calculate_metrics()
        for _, row in vendor_metrics.iterrows():
            values = [
                str(row['Vendedor']),
                f"R$ {row['Total Vendas']:,.2f}",
                str(row['Número de Pedidos']),
                f"R$ {row['Total Comissões']:,.2f}",
                f"R$ {row['Média por Pedido']:,.2f}"
            ]
            self.vendedor_tree.insert('', 'end', values=values)

    def _refresh_pagamentos_preview(self):
        """Update pagamentos preview"""
        for item in self.pagamentos_tree.get_children():
            self.pagamentos_tree.delete(item)
            
        payment_summary = self.analyzer.generate_unified_payment_summary()
        for _, row in payment_summary.iterrows():
            values = [
                str(row['Método de Pagamento']),
                f"R$ {row['Valor Total']:,.2f}",
                str(row['Número de Pedidos']),
                f"{row['Percentual']*100:.2f}%"
            ]
            self.pagamentos_tree.insert('', 'end', values=values)

    def _refresh_instituicao_preview(self):
        """Update instituição/curso preview"""
        for item in self.instituicao_tree.get_children():
            self.instituicao_tree.delete(item)
            
        inst_course_sales = self.analyzer.calculate_sales_by_institution_course()
        for _, row in inst_course_sales.iterrows():
            values = [
                str(row['Instituição']),
                str(row['Curso']),
                f"R$ {row['Total Vendas']:,.2f}",
                str(row['Número de Pedidos']),
                f"{row['Percentual de Vendas']:.2f}%"
            ]
            self.instituicao_tree.insert('', 'end', values=values)

    def show_welcome(self):
        """Show welcome screen"""
        self.hide_all_frames()
        self.welcome_frame.pack(expand=True, fill='both')
        
    def show_valores_report(self):
        """Show valores report section"""
        self.hide_all_frames()
        self.valores_frame.pack(expand=True, fill='both')
        self.valores_btn.state(['pressed'])
        
    def show_produtos_report(self):
        """Show produtos report section"""
        self.hide_all_frames()
        self.produtos_frame.pack(expand=True, fill='both')
        self.produtos_btn.state(['pressed'])
        
    def show_support(self):
        """Show support section"""
        self.hide_all_frames()
        self.support_frame.pack(expand=True, fill='both')
        self.support_btn.state(['pressed'])
        
    def hide_all_frames(self):
        """Hide all content frames and reset button states"""
        self.welcome_frame.pack_forget()
        self.valores_frame.pack_forget()
        self.produtos_frame.pack_forget()
        self.support_frame.pack_forget()
        
        # Reset button states
        self.valores_btn.state(['!pressed'])
        self.produtos_btn.state(['!pressed'])
        self.support_btn.state(['!pressed'])

    def load_data(self):
        """Handle data loading process"""
        excel_file = filedialog.askopenfilename(
            title="Selecione o arquivo Excel",
            filetypes=[("Excel files", "*.xlsx")]
        )
        
        if not excel_file:
            return
            
        try:
            self.analyzer.load_data(excel_file)
            self.status_label.config(
                text=f"Dados carregados com sucesso! Total de registros: {len(self.analyzer.df)}"
            )
            self.refresh_all_previews()
            self.main_notebook.select(1)  # Switch to preview tab
            messagebox.showinfo(
                "Sucesso", 
                f"Dados carregados com sucesso!\nTotal de registros: {len(self.analyzer.df)}"
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {str(e)}")
            
    def generate_report(self):
        """Handle report generation process"""
        if self.analyzer.df is None:
            messagebox.showwarning("Aviso", "Por favor, carregue os dados primeiro!")
            return
            
        filename = f"relatorio_completo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            initialfile=filename,
            filetypes=[("Excel files", "*.xlsx")]
        )
        
        if save_path:
            try:
                ExcelExporter.export_excel(self.analyzer, save_path)
                messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao gerar relatório: {str(e)}")