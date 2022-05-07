import PySimpleGUI as sg
import csv

headings = ['Name', 'Address', 'Phone Number', 'City']
header = [
        sg.Text('Name', pad=(0, 0), size=(15,1), justification='c'),
        sg.Text('Address', pad=(0, 0), size=(30,1), justification='c'),
        sg.Text('Phone Number', pad=(0, 0), size=(30,1), justification='c'),
        sg.Text('City', pad=(0, 0), size=(15,1), justification='c')
    ]

layout = [header]


for row in range(0, 15):
    layout.append([
        sg.Input(size=(15, 1), pad=(0, 0), key=(row, 0)), 
        sg.Input(size=(30,1), pad=(0, 0), key=(row, 1)), 
        sg.Input(size=(30,1), pad=(0, 0), key=(row, 2)),
        sg.Input(size=(15,1), pad=(0, 0), key=(row, 3))
    ])

layout.append([sg.Button("Submit"), sg.Button("Generate CSV")])

window = sg.Window('Spreadsheet', layout, font='Courier 12')

def generate_csv(headings, values):
    headings = ['Name', 'Address', 'Phone Number']

    file = open('contacts.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    # write the header
    writer.writerow(headings)

    for row in range(15):
        current_row = []
        for column in range(4):
            current_row.append(values[row, column])
        writer.writerow(current_row)

    file.close()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit':
        print(values[0,0])
    elif event == 'Generate CSV':
        generate_csv(headings, values)