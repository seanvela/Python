from functions import get_todos, write_todos
import time

# Use 'import functions' if there are a lot of functions.
# It is called modules, i.e. functions.get_todos()

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    # Get user input and strip space chars from it
    userAction = input("Type add, show, edit, complete, or exit: ")
    userAction = userAction.strip()


    if userAction.startswith('add'):
            todo = userAction[4:]

            todos = get_todos()
                
            todos.append(todo + '\n') #appends new todo on new line

            write_todos(todos)

    elif userAction.startswith('show'):

            todos = get_todos()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}: {item.title()}"
                print(row)

    elif userAction.startswith('edit'):
        try:
            number = int(userAction[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)
                    
        except ValueError:
            print('Your command is not valid.')
            continue

    elif userAction.startswith('complete'):
        try:
            number = int(userAction[9:])

            todos = get_todos()

            index = number - 1 
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f'Todo {todo_to_remove} was completed'
            print(message)

        except IndexError:
             print('There is no item with that number.')
             continue

    elif userAction.startswith('exit'):
            break
    
    else:
          print('Command is not valid.')


print('Goodbye!')


    