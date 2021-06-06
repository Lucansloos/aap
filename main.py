print('Zin in galgje?')
words = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]
GeheimWoord = words[random.randrange(0, len(words))]
GeradenLetters = []
levens = 10

def checkWin():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('? ', end='')
        print('')
        print('" ' * len(GeheimWoord))

renderWoord()