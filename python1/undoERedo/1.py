# lista de tareefas
# adicionar tarefa
# listar tarefas
# opção de desfazer (a cada vez que chamarmos, desfazer a ultima função)
# opção de refazer (a cada vez que chamarmos, refazer a ultima função) 



def show_op(todo_list):  # mostra as tarefas
  print()  # pula linha
  print('tarefas: ')  # mostra o que esta escrito
  print(todo_list)  # mostra as tarefas
  print()






def do_undo(todo_list, redo_list):  # desfazer
  if not todo_list:
    print('nao ha tarefas para desfazer')
    return

  last_todo = todo_list.pop()
  redo_list.append(last_todo)




def do_redo(todo_list, redo_list):  # refazer
  if not redo_list:
    print('nada para refazer ')
    return

  last_redo = redo_list.pop()
  todo_list.append(todo)



def do_add(todo, todo_list):  # adicionar tarefa
  todo_list.append(todo)






  



if __name__ == '__main__':  # se for o principal
  todo_list = []  # lista de tarefas
  redo_list = []  # lista de tarefas desfeitas

  while True:
    todo = input('digiteuma tarefa, undo, redo, ls: ')  # digiteuma tarefa

    if todo == 'ls':  # se for ls
      show_op(todo_list)  # mostra as tarefas
      continue
    
    elif todo == 'undo':  # se for undo
      do_undo(todo_list, redo_list)  # desfazer
      continue
    
    elif todo == 'redo':  # se for redo
      do_redo(todo_list, redo_list)  # refazer
      continue

    do_add(todo, todo_list)  # adicionar tarefa