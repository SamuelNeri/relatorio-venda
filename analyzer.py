import pandas as pd
import json
from datetime import datetime
from config import (
    COMISSOES_JSON, PAYMENT_GROUPS, EXCEL_COLUMNS,
    PAYMENT_COLUMNS, EXPORT_COLUMNS
)

class SalesAnalyzer:
    def __init__(self):
        self.df = None
        self.commissions = self.load_commission_rates()
        
    def load_commission_rates(self):
        """Load predefined commission rates"""
        try:
            return json.loads(COMISSOES_JSON)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing commission rates: {str(e)}")
            
    def load_data(self, excel_file):
        """Load sales data from the product items report"""
        try:
            # Read the Excel file with specified columns
            self.df = pd.read_excel(excel_file, usecols=EXCEL_COLUMNS)
            
            # Clean and prepare data
            self.df['Vendedor'] = self.df['Vendedor'].astype(str).str.strip()
            
            # Process payment data
            self._process_payment_data()
            
            print(f"Dados carregados com sucesso. Total de registros: {len(self.df)}")
            
        except Exception as e:
            raise ValueError(f"Erro ao carregar e processar dados: {str(e)}")
            
    def _process_payment_data(self):
        """Process payment data and calculate commissions"""
        # Convert non-numeric values to 0
        for col in PAYMENT_COLUMNS:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').fillna(0)

        # Identify predominant payment type
        payment_type_df = self.df[PAYMENT_COLUMNS]
        self.df['Tipo Pagamento'] = payment_type_df.idxmax(axis=1)
        
        # Clean payment types
        self.df['Tipo Pagamento'] = self.df['Tipo Pagamento'].replace({
            'BOLRES': 'Boleto Com Restrição',
            'BOLNEG': 'Boleto Negativado',
            'PIXSGPAYFCTICIO': 'PIX'
        })

        # Remove invalid orders
        self.df = self.df[self.df['Valor do Pedido'].notna() & (self.df['Valor do Pedido'] != 0)]
        
        # Calculate commissions
        print("Calculando comissões...")
        self.df['Comissao'] = self.df.apply(self.calculate_commission, axis=1)
        
        # Format currency values
        self._format_currency_values()

    def _format_currency_values(self):
        """Format currency values in the DataFrame"""
        def format_currency(value):
            try:
                if pd.isna(value):
                    return 'R$ 0,00'
                return f'R$ {float(value):,.2f}'
            except:
                return 'R$ 0,00'
                
        self.df['Valor_Formatado'] = self.df['Valor do Pedido'].apply(format_currency)
        self.df['Comissao_Formatada'] = self.df['Comissao'].apply(format_currency)

    def calculate_commission(self, row):
        """Calculate commission for a single sale"""
        try:
            vendor = str(row['Vendedor']).strip()
            payment_type = str(row['Tipo Pagamento']).strip()
            value = float(row['Valor do Pedido'])
            
            if pd.isna(value) or value == 0:
                return 0.0
                
            if vendor not in self.commissions:
                print(f"Vendedor não encontrado nas comissões: '{vendor}'")
                return 0.0
            
            # Try exact match first
            if payment_type in self.commissions[vendor]:
                commission_rate = self.commissions[vendor][payment_type]
            else:
                # Try case-insensitive match
                payment_type_upper = payment_type.upper()
                for known_type, rate in self.commissions[vendor].items():
                    if known_type.upper() == payment_type_upper:
                        commission_rate = rate
                        break
                else:
                    print(f"Tipo de pagamento não encontrado: '{payment_type}' para vendedor '{vendor}'")
                    commission_rate = self.commissions[vendor].get('Desconhecido', 0)
            
            commission_value = (value * commission_rate) / 100
            return commission_value
            
        except Exception as e:
            print(f"Erro ao calcular comissão: {str(e)} para vendedor '{vendor}' e pagamento '{payment_type}'")
            return 0.0

    def calculate_metrics(self):
        """Calculate overall and vendor-specific sales metrics"""
        if self.df is None:
            raise ValueError("Dados não carregados. Por favor, carregue os dados primeiro.")
        
        # Overall metrics
        metrics = {
            'Total Vendas': self.df['Valor do Pedido'].sum(),
            'Total Comissões': self.df['Comissao'].sum(),
            'Número de Pedidos': len(self.df),
            'Média de Valor por Pedido': self.df['Valor do Pedido'].mean()
        }
        
        # Vendor-specific metrics
        vendor_metrics = self.df.groupby('Vendedor').agg({
            'Valor do Pedido': ['sum', 'count'],
            'Comissao': 'sum'
        }).reset_index()
        
        # Rename columns for clarity
        vendor_metrics.columns = ['Vendedor', 'Total Vendas', 'Número de Pedidos', 'Total Comissões']
        
        # Calculate average sale per vendor
        vendor_metrics['Média por Pedido'] = vendor_metrics['Total Vendas'] / vendor_metrics['Número de Pedidos']
        
        return metrics, vendor_metrics

    def generate_unified_payment_summary(self):
        """Generate a summary of unified payment methods"""
        if self.df is None:
            raise ValueError("Dados não carregados. Por favor, carregue os dados primeiro.")
        
        # Group payments by type and calculate total
        payment_summary = self.df.groupby('Tipo Pagamento').agg({
            'Valor do Pedido': 'sum',
            'Num. Pedido': 'count'
        }).reset_index()
        
        # Rename columns
        payment_summary.columns = ['Método de Pagamento', 'Valor Total', 'Número de Pedidos']
        
        # Calculate percentage
        total_sales = payment_summary['Valor Total'].sum()
        payment_summary['Percentual'] = payment_summary['Valor Total'] / total_sales
        
        return payment_summary
    
    def calculate_sales_by_institution_course(self):
        """
        Calculate sales value for each institution and course combination
        
        Returns:
        - DataFrame with columns: Instituição, Curso, Total Vendas, Número de Pedidos, Percentual de Vendas
        """
        if self.df is None:
            raise ValueError("Dados não carregados. Por favor, carregue os dados primeiro.")
        
        # Group by Institution and Course
        institution_course_sales = self.df.groupby(['Instituição', 'Curso']).agg({
            'Valor do Pedido': ['sum', 'count']
        }).reset_index()
        
        # Rename columns for clarity
        institution_course_sales.columns = ['Instituição', 'Curso', 'Total Vendas', 'Número de Pedidos']
        
        # Sort by Total Sales in descending order
        institution_course_sales = institution_course_sales.sort_values('Total Vendas', ascending=False)
        
        # Calculate percentage of total sales
        total_sales = institution_course_sales['Total Vendas'].sum()
        institution_course_sales['Percentual de Vendas'] = institution_course_sales['Total Vendas'] / total_sales * 100
        
        return institution_course_sales