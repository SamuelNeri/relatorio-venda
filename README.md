# Sistema de Análise de Vendas

Um sistema desktop para análise e geração de relatórios de vendas, desenvolvido em Python usando Tkinter.

## 📋 Funcionalidades

### Relatório de Valores
- Análise detalhada das vendas por vendedor
- Cálculo automático de comissões
- Análise de métodos de pagamento
- Métricas por instituição e curso
- Pré-visualização dos dados antes da exportação
- Exportação para Excel com formatação

### Relatório de Produtos
- [Em desenvolvimento]

## 🔧 Requisitos

- Python 3.7+
- pandas
- openpyxl
- ttkthemes
- xlsxwriter

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/relatorio-venda.git
cd relatorio-venda
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

1. Execute o programa:
```bash
python main.py
```

2. Na interface:
   - Clique em "Relatório de Valores"
   - Use "Carregar Dados" para selecionar seu arquivo Excel
   - Visualize os dados nas diferentes abas
   - Gere o relatório final em Excel

## 📁 Estrutura do Projeto

```
sistema-analise-vendas/
├── main.py              # Ponto de entrada do programa
├── gui.py              # Interface gráfica principal
├── analyzer.py         # Lógica de análise de dados
├── excel_exporter.py   # Exportação para Excel
├── config.py           # Configurações e constantes
└── requirements.txt    # Dependências do projeto
```

### Descrição dos Módulos

- **main.py**: Inicializa a aplicação e configura a janela principal
- **gui.py**: Interface gráfica com todas as views e controles
- **analyzer.py**: Processa os dados e calcula métricas
- **excel_exporter.py**: Gerencia a exportação de relatórios
- **config.py**: Armazena configurações como taxas de comissão

## 📊 Formato dos Dados de Entrada

O sistema espera um arquivo Excel (.xlsx) com as seguintes colunas obrigatórias:

- Data
- Num. Pedido
- Vendedor
- Cliente
- Valor do Pedido
- Tipo Pagamento
- Instituição
- Curso

## 💡 Recursos Adicionais

- Pré-visualização em tempo real dos dados
- Cálculo automático de comissões por vendedor
- Análise de métodos de pagamento
- Suporte a diferentes tipos de relatórios
- Interface moderna e intuitiva

## 🔍 Suporte

Para suporte técnico ou dúvidas:
- Acesse a documentação online
- Consulte as FAQs
- Entre em contato com o suporte técnico

## 🔄 Atualizações Futuras

- [ ] Implementação do Relatório de Produtos
- [ ] Exportação em outros formatos
- [ ] Gráficos e visualizações avançadas
- [ ] Customização de comissões via interface
- [ ] Backup automático dos dados

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).