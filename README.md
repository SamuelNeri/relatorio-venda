# Sistema Unificado de Relatórios de Vendas

## Descrição
O Sistema Unificado de Relatórios de Vendas é uma aplicação desktop que integra dois subsistemas: o Separador de Boletos e o Separador de Vendas. Esta ferramenta foi desenvolvida para facilitar a geração de relatórios de vendas e o processamento de comissões, oferecendo uma interface unificada para acessar ambas as funcionalidades.

## Características
- Interface gráfica intuitiva desenvolvida com Tkinter
- Integração de dois sistemas distintos em uma única aplicação
- Geração de relatórios de vendas
- Cálculo de comissões baseado em regras predefinidas
- Exportação de dados para arquivos Excel

## Requisitos do Sistema
- Python 3.7 ou superior
- Bibliotecas: tkinter, pandas, openpyxl

## Instalação

1. Clone o repositório ou faça o download dos arquivos do projeto.

2. Instale as dependências necessárias:
   ```
   pip install pandas openpyxl
   ```

3. Certifique-se de que todos os arquivos do projeto estão no mesmo diretório:
   - main.py
   - SeparadorBoletos.py
   - SeparadorDeVendas.py
   - comissoes.py

## Uso

1. Execute o arquivo principal:
   ```
   python main.py
   ```

2. Na interface principal, selecione o sistema que deseja utilizar:
   - "Separador de Boletos"
   - "Separador de Vendas"

3. Siga as instruções na interface de cada subsistema para carregar dados, gerar relatórios ou calcular comissões.

## Estrutura do Projeto
- `main.py`: Arquivo principal que inicia a interface unificada
- `SeparadorBoletos.py`: Módulo para processamento de boletos
- `SeparadorDeVendas.py`: Módulo para separação e análise de vendas
- `comissoes.py`: Contém as regras e cálculos de comissões

## Compilação
Para criar um executável standalone:

1. Instale o PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Compile o projeto:
   ```
   pyinstaller --name="SistemaUnificado" --windowed --onefile main.py
   ```

3. O executável será gerado na pasta `dist`.

## Suporte
Para relatar problemas ou sugerir melhorias, por favor, abra uma issue no repositório do projeto.

## Contribuindo
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar pull requests.

## Licença
[Inserir informações de licença aqui]

## Autores
[Seu nome ou o nome da sua equipe]

---

Desenvolvido com ❤️ para otimizar o processo de relatórios de vendas e comissões.
