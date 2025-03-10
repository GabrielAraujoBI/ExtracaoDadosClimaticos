# Extração de Dados Climáticos

Este projeto tem como objetivo a **extração de dados climáticos** da API pública [Visual Crossing](https://www.visualcrossing.com/). O foco principal é coletar dados climáticos da cidade de **Boston**, considerando um **intervalo de 7 dias** a partir da data atual. No entanto, o projeto é flexível e pode ser facilmente ajustado para coletar dados climáticos de qualquer cidade ao redor do mundo, bastando alterar o parâmetro da cidade na configuração.

Os dados extraídos incluem informações essenciais como **temperaturas mínimas, médias e máximas**, **condições meteorológicas** diárias (como ensolarado, nublado, chuvoso) e outras variáveis climáticas importantes. Essas informações são armazenadas em arquivos CSV, facilitando a análise e o uso posterior desses dados em diferentes contextos, como visualizações, relatórios ou estudos climáticos.

## Descrição do Projeto

O código realiza as seguintes etapas:

1. **Define um intervalo de 7 dias** começando pela data atual.
2. **Constrói a URL da API** utilizando a cidade e o intervalo de datas.
3. **Coleta dados climáticos** de temperatura e condições meteorológicas.
4. **Armazena os dados** em três arquivos CSV:
   - **dados_brutos.csv**: Contém todos os dados climáticos (como temperaturas, precipitação, etc.).
   - **temperaturas.csv**: Armazena as temperaturas mínimas, médias e máximas.
   - **condicoes.csv**: Contém as condições climáticas e ícones relacionados.
