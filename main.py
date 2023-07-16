# nesse arquivo main, estão a logica e as instâncias para chamar a classe e os métodos

# Importe do arquivo e a classe.
from Tarefas import Tarefas

# Chamando a classe
tarefa = Tarefas()

# Uma repetição infinita aonde só ira sair do lup se o usuário desejar, fazendo assim a possibilidade de criar
# várias tarefas
while True:
    print('Digite o nome da tarefa logo abaixo ou se preferir não adicionar digite "sair":')
    nome_tarefa = input('Digite: '.upper())
    if nome_tarefa in 'SAIRsair':
        break
    tempo_tarefa = input('Digite o tempo que você acha vai completar essa tarefa: ')
    tarefa.adicionar_tarefas(nome_tarefa, tempo_tarefa)
tarefa.exibir_tarefas()