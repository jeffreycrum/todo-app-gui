import os
import time

import FreeSimpleGUI as sg

import util

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source='files/add.png', mouseover_colors='LightBlue2', key='Add')
complete_button = sg.Button(size=2, image_source='files/complete.png', key='Complete')
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=util.read_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = util.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            util.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = util.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                util.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Complete":
            try:
                todos = util.read_todos()
                todo_to_remove = values['todos'][0]
                todos.remove(todo_to_remove)
                util.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(values['todos'])
        case sg.WINDOW_CLOSED:
            break

window.close()
