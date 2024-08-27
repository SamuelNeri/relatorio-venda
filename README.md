# Sistema de Relatório de Vendas com Cálculo de Comissões

Este é um sistema de relatório de vendas com cálculo de comissões desenvolvido em Python. O sistema utiliza o Tkinter para a interface gráfica e o Pandas para manipulação de dados de vendas contidos em um arquivo Excel. Ele permite calcular comissões com base em diferentes tipos de vendas e métodos de pagamento, e também exibir ou salvar os resultados.

## Funcionalidades

- **Seleção de Arquivo:** Permite ao usuário selecionar um arquivo Excel contendo os dados de vendas.
- **Cálculo de Comissões:** Calcula automaticamente as comissões com base nas regras definidas no arquivo `comissoes.py`.
- **Mostrar Resultados:** Exibe os resultados calculados em uma janela pop-up sem a necessidade de salvar o arquivo.
- **Salvar Relatório:** Permite salvar o relatório de vendas por vendedor em um arquivo Excel.
- **Interface Intuitiva:** Interface gráfica amigável para fácil utilização.

## Pré-requisitos

Certifique-se de ter o Python instalado (recomendado: versão 3.7 ou superior) e as seguintes bibliotecas:

- `tkinter`: Biblioteca padrão do Python para a interface gráfica.
- `pandas`: Para manipulação e análise de dados.
- `openpyxl`: Para leitura e escrita de arquivos Excel.

Você pode instalar as bibliotecas necessárias usando o pip:

```bash
pip install pandas openpyxl
