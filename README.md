# Migrador de Dados para MongoDB

Este script foi desenvolvido para migrar dados de um arquivo Excel para o MongoDB, com a possibilidade de transformar dados de acordo com um mapeamento fornecido. Além disso, o script também gera um arquivo CSV com os dados transformados.

## Funcionalidades

- Conexão com o MongoDB.
- Leitura e transformação de dados a partir de um arquivo Excel.
- Aplicação de mapeamento de valores para as colunas do Excel.
- Criação de um arquivo CSV com os dados transformados.
- Inserção dos dados no MongoDB.

## Pré-requisitos

Antes de rodar o script, você precisa ter o Python instalado e as seguintes dependências:

- `pandas`: Para manipulação de dados em tabelas.
- `pymongo`: Para interação com o MongoDB.
- `python-dotenv`: Para carregar variáveis de ambiente a partir de um arquivo `.env`.
- `openpyxl`: Para ler arquivos Excel (`.xlsx`).

Instale as dependências executando:

```bash
pip install pandas pymongo python-dotenv openpyxl


## Como Usar
1.Altere os caminhos das variáveis EXCEL_FILE_PATH e OUTPUT_CSV_PATH no script migrador.py para apontar para o arquivo Excel de origem e para o caminho desejado do arquivo CSV de saída.

2.Execute o script:
```bash
python migrador.py
