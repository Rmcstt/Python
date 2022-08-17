# lista de tareefas
# adicionar tarefa
# listar tarefas
# opção de desfazer (a cada vez que chamarmos, desfazer a ultima função)
# opção de refazer (a cada vez que chamarmos, refazer a ultima função) 



def show_op(todo_list):
  print()
  print('tarefas: ')
  print(todo_list)
  print()






def do_undo(todo_list, redo_list):
  if not todo_list:
    print('nao ha tarefas para desfazer')
    return

  last_todo = todo_list.pop()
  redo_list.append(last_todo)




def do_redo(todo_list, redo_list):
  if not redo_list:
    print('nada para refazer ')
    return

  last_redo = redo_list.pop()
  todo_list.append(todo)



def do_add(todo, todo_list):
  todo_list.append(todo)






  



if __name__ == '__main__':
  todo_list = []
  redo_list = []

  while True:
    todo = input('digiteuma tarefa, undo, redo, ls: ')

    if todo == 'ls':
      show_op(todo_list)
      continue
    
    elif todo == 'undo':
      do_undo(todo_list, redo_list)
      continue
    
    elif todo == 'redo':
      do_redo(todo_list, redo_list)
      continue

    do_add(todo, todo_list)