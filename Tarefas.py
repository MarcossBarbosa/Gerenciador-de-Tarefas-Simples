# Aqui está um gerenciador de tarefas básico aonde é possivél adicionar, remover e exibir tarefas.

# A classe criada com nome de Tarefas.
class Tarefas:
    # Método construtor que recebe um dicionario vazio.
    def __init__(self):
        self.tarefa = {}

    # Método aonde adiciona as tarefas, esse método contém nome e tempo para realizar a tarefa.
    def adicionar_tarefas(self, nome_tarefa, tempo_tarefa):
        self.tarefa[nome_tarefa] = tempo_tarefa

    # Métod para remover as tarefas que o usuário desejar. Nele há um input para perguntar ao usuário
    #  e uma condição que verifica se a tarefa está no dicionario
    def remover_tarefas(self, tarefas):
        remover = input('Digite qual tarefa deseja remover? ')
        if remover in tarefas:
            del tarefas[remover]
            print('Tarefa removida com sucesso! ')
        else:
            print('Tarefa não encontrada')
    # Método para exibir as tarefas para o usuário. Nele há um estrutura de repetição que roda no dicionario e
    # o exibi com o print.
    def exibir_tarefas(self):
        print('Tarefas')
        for nome_tarefa, tempo_tarefa in self.tarefa.items():
            print(f'Nome da tarefa: {nome_tarefa}, tempo para realiza-lá: {tempo_tarefa}')

