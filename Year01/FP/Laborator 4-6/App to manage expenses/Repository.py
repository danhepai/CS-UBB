import Domeniu


def adauga_cheltuiala_la_buget(cheltuiala, buget):
    buget.append(cheltuiala)


def actualizeaza_cheltuiala(cheltuiala, id, buget):
    buget[id] = cheltuiala


def sterge_cheltuiala_din_buget(cheltuiala, buget):
    buget.remove(cheltuiala)


def get_dimensiune_buget(buget):
    return len(buget)


def get_buget(buget):
    return buget


def get_cheltuiala(buget, index):
    return buget[index]


def printeaza_toate_cheltuielile(buget):
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        chelt_str = Domeniu.printeaza_o_cheltuiala(cheltuiala, "")
        toate_cheltuielile_str += "ID: " + str(buget.index(cheltuiala) + 1) + " " + chelt_str + "\n"
    return toate_cheltuielile_str


def creeaza_stare(buget, buget_secundar):
    return [buget, buget_secundar]


def adauga_stare_la_undo_list(stare, undo_list):
    undo_list.append(stare)


def get_buget_din_ultima_stare(undo_list):
    stare = undo_list[len(undo_list) - 1]
    return stare[0]


def get_buget_secundar_din_ultima_stare(undo_list):
    stare = undo_list[len(undo_list) - 1]
    return stare[1]
