# To-Do List

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

## Descrição

O **To-Do List** é um aplicativo de linha de comando desenvolvido em Python que permite aos usuários gerenciar suas tarefas de forma simples e eficiente. Com este aplicativo, é possível adicionar, remover e listar tarefas diretamente no terminal.

## Funcionalidades

- **Adicionar Tarefa:** Permite ao usuário adicionar uma nova tarefa à lista.
- **Remover Tarefa:** Possibilita a remoção de uma tarefa existente com base no seu número na lista.
- **Listar Tarefas:** Exibe todas as tarefas adicionadas com seus respectivos números.

## Tecnologias Utilizadas

- **Python 3:** Linguagem de programação principal utilizada no desenvolvimento do aplicativo.

## Estrutura do Código

O código é estruturado em funções para facilitar a manutenção e a leitura:

1. **`adicionar_tarefa(lista)`:** Solicita ao usuário uma descrição da tarefa e a adiciona à lista, caso não esteja vazia.
2. **`remover_tarefa(lista)`:** Exibe as tarefas atuais e solicita ao usuário o número da tarefa que deseja remover, realizando a remoção se o número for válido.
3. **`listar_tarefa(lista)`:** Lista todas as tarefas presentes na lista com seus respectivos números.
4. **Loop Principal:** Exibe um menu de opções e chama as funções correspondentes com base na escolha do usuário.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/to-do-list.git

2. **Navegue até o diretório do projeto:**

    ```bash
    cd to-do-list

3. **Execute o script Python:**

    ```bash
    python todo_list.py

---