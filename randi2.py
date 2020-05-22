import PySimpleGUI as sg

col1=[
       [sg.Text('Név:') ],
       [sg.Text('Telefonszám:') ],
       [sg.Text('Életkor:') ],
       [sg.Button('Keres') ]
       
    ]
col2=[
       [sg.Input(key='Név') ],
       [sg.Input(key='Telefon') ],
       [sg.Input(key='Életkor') ],
       [sg.Button('Ment') ]
       
    ]

layout=[
       [sg.Column(col1),sg.Column(col2)]
    ]

window=sg.Window('Randi', layout)

while True:
    event, values = window.read()
    print(event,values)
    if event in (None, 'Exit'):
        break
    
    if event in ('Ment'):
        nev = values['Név']
        telefon = values['Telefon']
        eletkor = values['Életkor']
        
        with open('randi.csv', 'a') as f:
            print(f'{nev};{telefon};{eletkor}',file=f)
        
        
    if event in ('Keres'):
        nev = values['Név']
        telefon = values['Telefon']
        eletkor = values['Életkor']
        
        with open('randi.csv', 'r') as f:
            for sor in f:
                fnev,ftelefon,feletkor=sor.strip().split(';')
                if nev == fnev:
                    print('*********')
                    window['Telefon'].update(ftelefon)
                    window['Életkor'].update(feletkor)
        
        
        
      #  nev = eredmeny[0][0]
      #  telefon = eredmeny[0][1]
      #  eletkor = eredmeny[0][2]
       # window['Név'].update(nev)
       # window['Telefon'].update(telefon)
      #  window['Életkor'].update(eletkor)
        #print(eredmeny)
        
        
        