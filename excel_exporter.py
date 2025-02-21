import pandas as pd
from config import EXPORT_COLUMNS  # Changed from relative import

class ExcelExporter:
    @staticmethod
    def export_excel(analyzer, filename):
        """Export sales data to Excel with formatting"""
        try:
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            workbook = writer.book
            
            # Define formats
            formats = ExcelExporter._create_formats(workbook)
            
            # Export main sales data
            ExcelExporter._export_sales_data(analyzer, writer, formats)
            
            # Export summary data
            ExcelExporter._export_summary_data(analyzer, writer, formats)
            
            # Export unified payments
            ExcelExporter._export_unified_payments(analyzer, writer, formats)
            
            # Export institution and course sales
            ExcelExporter._export_institution_course_sales(analyzer, writer, formats)
            
            writer.close()
            print("Relatório gerado com sucesso!")
            
        except Exception as e:
            print(f"Erro ao gerar relatório: {str(e)}")
            raise

    @staticmethod
    def _create_formats(workbook):
        """Create Excel formats"""
        return {
            'currency': workbook.add_format({'num_format': 'R$ #,##0.00'}),
            'percent': workbook.add_format({'num_format': '0.00%'}),
            'header': workbook.add_format({
                'bold': True,
                'bg_color': '#D9D9D9',
                'border': 1
            })
        }

    @staticmethod
    def _export_sales_data(analyzer, writer, formats):
        """Export main sales data"""
        export_df = analyzer.df[EXPORT_COLUMNS].copy()
        export_df.to_excel(writer, sheet_name='Vendas', index=False)
        worksheet = writer.sheets['Vendas']
        
        # Format headers
        for col_num, value in enumerate(export_df.columns.values):
            worksheet.write(0, col_num, value, formats['header'])
        
        # Set column formats
        for col_idx, col in enumerate(EXPORT_COLUMNS):
            width = 15
            if col in ['Valor do Pedido', 'Valor Pago', 'Comissao']:
                worksheet.set_column(col_idx, col_idx, width, formats['currency'])
            else:
                worksheet.set_column(col_idx, col_idx, width)

    @staticmethod
    def _export_summary_data(analyzer, writer, formats):
        """Export summary data"""
        metrics, vendor_metrics = analyzer.calculate_metrics()
        
        # Export summary
        summary_df = pd.DataFrame([metrics])
        summary_df.to_excel(writer, sheet_name='Resumo', index=False)
        summary_sheet = writer.sheets['Resumo']
        
        # Format headers
        for col_num, value in enumerate(summary_df.columns.values):
            summary_sheet.write(0, col_num, value, formats['header'])
        
        # Export vendor metrics
        vendor_metrics.to_excel(writer, sheet_name='Análise por Vendedor', index=False)
        vendor_sheet = writer.sheets['Análise por Vendedor']
        
        # Format headers
        for col_num, value in enumerate(vendor_metrics.columns.values):
            vendor_sheet.write(0, col_num, value, formats['header'])

    @staticmethod
    def _export_unified_payments(analyzer, writer, formats):
        """Export unified payment methods"""
        unified_payments_df = analyzer.generate_unified_payment_summary()
        
        unified_payments_df.to_excel(writer, sheet_name='Pagamentos Unificados', index=False)
        unified_sheet = writer.sheets['Pagamentos Unificados']
        
        # Format headers
        for col_num, value in enumerate(unified_payments_df.columns.values):
            unified_sheet.write(0, col_num, value, formats['header'])
            
        # Format currency and percentage values
        unified_sheet.set_column('B:B', 18, formats['currency'])
        unified_sheet.set_column('D:D', 18, formats['percent'])

    @staticmethod
    def _export_institution_course_sales(analyzer, writer, formats):
        """Export sales by institution and course"""
        # Calculate sales by institution and course
        institution_course_sales = analyzer.calculate_sales_by_institution_course()
        
        # Export to Excel with a shorter, simplified sheet name
        institution_course_sales.to_excel(writer, sheet_name='Vendas_Instituicao_Curso', index=False)
        institution_sheet = writer.sheets['Vendas_Instituicao_Curso']
        
        # Format headers
        for col_num, value in enumerate(institution_course_sales.columns.values):
            institution_sheet.write(0, col_num, value, formats['header'])
        
        # Set column formats
        institution_sheet.set_column('C:C', 18, formats['currency'])  # Total Sales
        institution_sheet.set_column('E:E', 18, formats['percent'])  # Sales Percentage