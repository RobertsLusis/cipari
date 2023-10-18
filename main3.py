import fileinput # biblioteka datnju ievadisanai
with fileinput.FileInput(files=('adminviesis.txt')) as datne:
    admin=[
        ["Roberts", "Lusis", "18"],
        ["Ivars", "Reinfelds", "18"],
        ["Juris", "Kalnins", "29"]
    ]
    viesis=[
        ["Verners", "Skrastins", "18"]
    ]
    for idx, line in enumerate(datne):
        if datne.isfirstline() == True:
            
            print('=== Lasa datni === ', datne.filename())
        
        print(idx, line,end='' )