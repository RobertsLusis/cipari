import fileinput # biblioteka datnju ievadisanai
with fileinput.FileInput(files=('11kl.txt', '10kl.txt')) as datne:
    
    for idx, line in enumerate(datne):
        if datne.isfirstline() == True:
            print('=== Lasa datni === ', datne.filename())
        
        print(idx, line,end='' )