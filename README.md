# Sistema de Relatório de Vendas e Comissões

## Descrição
Este sistema é uma aplicação desktop desenvolvida em Python para gerar relatórios detalhados de vendas e calcular comissões com base em diferentes métodos de pagamento e tipos de vendedores. Ele processa dados de vendas a partir de arquivos Excel e produz relatórios abrangentes em formato Excel.

## Funcionalidades Principais
- Importação de dados de vendas de arquivos Excel (.xlsx, .xls)
- Cálculo automático de comissões baseado em regras predefinidas
- Geração de relatórios detalhados em três formatos:
  1. Resumo por Vendedor
  2. Detalhado por Pagamento
  3. Resumo por Forma de Pagamento
- Interface gráfica intuitiva para fácil operação
- Visualização prévia dos resultados antes da geração do relatório final

## Requisitos do Sistema
- Python 3.7 ou superior
- Bibliotecas Python:
  - tkinter
  - pandas
  - openpyxl
  - locale

## Instalação
1. Clone o repositório ou faça o download dos arquivos do projeto.
2. Instale as dependências necessárias:
   ```
   pip install pandas openpyxl
   ```
3. Certifique-se de que todos os arquivos do projeto estão no mesmo diretório.

## Uso
1. Execute o script principal:
   ```
   python SeparadorDeVendas.py
   ```
2. Na interface gráfica:
   - Clique em "Selecionar Arquivo" para escolher o arquivo Excel de entrada.
   - Clique em "Calcular Comissões" para processar os dados.
   - Use "Mostrar Resultados" para visualizar um resumo na interface.
   - Clique em "Salvar Relatório" para gerar o relatório Excel completo.

## Estrutura do Projeto
- `SeparadorDeVendas.py`: Arquivo principal contendo a lógica de negócios e a interface gráfica.
- `comissoes.py`: Módulo que define as regras de comissão (não incluído no snippet, deve ser criado separadamente).

## Detalhes Técnicos
### Classe `Comissao`
- Carrega e gerencia as regras de comissão.
- Calcula comissões com base no tipo de álbum, método de pagamento e valor da venda.

### Classe `SeparadorDeVendas`
- Responsável por carregar, processar e analisar os dados de vendas.
- Gera relatórios detalhados em diferentes formatos.

### Classe `App`
- Implementa a interface gráfica do usuário usando Tkinter.
- Gerencia a interação do usuário e a exibição de resultados.

## Formato do Relatório
O relatório final é um arquivo Excel contendo três planilhas:
1. **Resumo por Vendedor**: Total de vendas e comissões por vendedor.
2. **Detalhado por Pagamento**: Detalhes de cada venda, incluindo método de pagamento e comissão.
3. **Resumo por Forma de Pagamento**: Total de vendas e comissões agrupados por método de pagamento.

## Customização
- As regras de comissão podem ser ajustadas no arquivo `comissoes.py`.
- O layout da interface e os formatos de relatório podem ser modificados em `SeparadorDeVendas.py`.

## Suporte
Para relatar problemas ou sugerir melhorias, por favor, abra uma issue no repositório do projeto.

## Contribuindo
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar pull requests.

## Licença
[Inserir informações de licença aqui]

---

Desenvolvido com ❤️ para otimizar o processo de relatórios de vendas e cálculo de comissões.