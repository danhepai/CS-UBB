
def creeaza_cheltuiala(zi, suma, tip):
    cheltuiala = [zi, suma, tip]
    return cheltuiala


def get_zi(cheltuiala):
    return cheltuiala[0]


def get_suma(cheltuiala):
    return cheltuiala[1]


def get_tip(cheltuiala):
    return cheltuiala[2]


def printeaza_o_cheltuiala(cheltuiala, index):
    return str(index) + "ZIUA: " + str(cheltuiala[0]) + " SUMA: " + str(cheltuiala[1]) + " TIP: " + str(cheltuiala[2])


#Tot ce e cu buget in repository



