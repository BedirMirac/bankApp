import library

dil = 1
def getlangnumber():
    global dil
    return dil
def set_dil(lang):
    global dil
    dil = lang


def get_dil():
    global dil
    if dil == 1:
        return library.Turkish
    elif dil == 2:
        return library.English
    elif dil == 3:
        return library.Italian
    elif dil == 4:
        return library.German

