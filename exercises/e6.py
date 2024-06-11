import FreeSimpleGUI as sg
from converter14 import convert

label1 = sg.Text('Enter Feet: ')
input1 = sg.Input(key='feet')
label2 = sg.Text('Enter inches: ')
input2 = sg.Input(key='inches')
convert_button = sg.Button('Convert')
output_label = sg.Text('', key='output')
exit_button = sg.Button('Exit')


window = sg.Window('Converter', layout=[[label1, input1], 
                                              [label2, input2],
                                              [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    
    feet = float(values['feet'])
    inches = float(values['inches'])

    result = convert(feet, inches)
    window['output'].update(value=f"{result} m", text_color = 'yellow')

window.close()

