# Calculadora de Idade do Bebê

Uma ferramenta simples e eficiente para calcular a idade cronológica e a idade corrigida de bebês prematuros, desenvolvida para facilitar a rotina de profissionais de saúde.

## Sobre o Projeto

Este projeto surgiu da necessidade prática de nutricionistas em hospitais que precisavam de uma maneira rápida e confiável de calcular a idade corrigida de bebês prematuros. Diferentemente da idade cronológica (contada a partir da data de nascimento), a idade corrigida considera a idade gestacional do bebê no nascimento, o que é um parâmetro fundamental para avaliações de crescimento e desenvolvimento.

Inicialmente concebida como uma calculadora web em HTML, CSS e JavaScript, a ferramenta foi posteriormente convertida para um aplicativo de desktop em Python. A transição para um programa executável permite que os profissionais de saúde a utilizem em ambientes hospitalares, sem a necessidade de acesso à internet ou de um navegador, garantindo praticidade e agilidade.

## Funcionalidades

A calculadora de idade do bebê oferece dois tipos de cálculo:

1.  **Idade Cronológica:** A idade real do bebê, calculada desde a data de nascimento até o dia atual.
2.  **Idade Corrigida:** A idade do bebê ajustada para a idade gestacional. Este cálculo usa a seguinte fórmula: `Idade Corrigida (semanas) = Idade Cronológica (semanas) - (40 - Idade Gestacional) + Dias na Semana de Nascimento`.

O programa é intuitivo e fácil de usar, com uma interface gráfica simples que espelha a versão web original.

## Como Utilizar

### Requisitos

Para executar o código-fonte em Python, você precisará ter o Python 3 instalado em seu computador. As bibliotecas `tkinter` e `datetime` são usadas, e ambas vêm por padrão com a instalação do Python.

### Executando o Código

1.  **Clone o repositório:**
    ```bash
    git clone https://docs.github.com/articles/referencing-and-citing-content
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd [nome da pasta]
    ```
3.  **Execute o script Python:**
    ```bash
    python calculadora_gestacional.py
    ```

A janela da calculadora será aberta, permitindo que você insira as informações e obtenha os resultados.

### Usando o Executável

Se você preferir usar a versão compilada, o arquivo executável (`.exe` para Windows) pode ser encontrado na pasta `dist` do projeto (após a compilação).

1.  **Baixe o arquivo executável** da página de Releases do repositório.
2.  **Execute o arquivo** diretamente no seu computador.

## Estrutura do Projeto

O projeto é composto por um único script Python, `calculadora_gestacional.py`, que contém:

  - **Interface Gráfica:** Construída com a biblioteca `tkinter`. Define a janela principal, os campos de entrada, os botões e a área de exibição dos resultados.
  - **Funções de Cálculo:** As funções `calculate_age()`, `calculate_chronological_age()` e `calculate_corrected_age()` são responsáveis pela lógica do programa, utilizando o módulo `datetime` para manipular as datas e realizar os cálculos de forma precisa.
  - **Manipulação de Erros:** O código inclui um bloco `try-except` para garantir que o programa lide corretamente com entradas de dados incorretas, fornecendo uma mensagem de erro clara ao usuário.

## Contribuição

Contribuições são sempre bem-vindas\! Se você tiver sugestões, ideias de melhoria ou quiser reportar um bug, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
