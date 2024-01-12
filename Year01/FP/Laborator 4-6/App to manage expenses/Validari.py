import Domeniu


def valideaza_cheltuiala(cheltuiala):
    erori = ""
    if Domeniu.get_zi(cheltuiala) < 1 or Domeniu.get_zi(cheltuiala) > 31:
        erori += "Zi invalida!\n"
    if Domeniu.get_suma(cheltuiala) < 0:
        erori += "Suma invalida! Nu poate fi negativa!\n"
    if Domeniu.get_tip(cheltuiala) not in ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]:
        erori += "Tip invalid!\n"
    if len(erori) > 0:
        raise ValueError(erori)


def valideaza_zi(zi):
    erori = ""
    if zi < 1 or zi > 31:
        erori += "Zi invalida! \n"
    if len(erori) > 0:
        raise ValueError(erori)


def valideaza_interval_de_zile(zi_inceput, zi_sfarsit):
    erori = ""
    if zi_inceput >= zi_sfarsit:
        erori += "Interval de timp invalid! \n"
    if len(erori) > 0:
        raise ValueError(erori)


def valideaza_tip_de_cheltuiala(tip):
    erori = ""
    if tip not in ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]:
        erori += "Tip invalid! \n"
    if len(erori) > 0:
        raise ValueError(erori)


def valideaza_suma(suma):
    erori = ""
    if suma < 0:
        erori += "Tip invalid! \n"
    if len(erori) > 0:
        raise ValueError(erori)


def valideaza_zi_pentru_cheltuiala_maxima(zi):
    erori = ""
    if zi < 1 or zi > 31:
        erori += "Nu exista cheltuieli! \n"
    if len(erori) > 0:
        raise ValueError(erori)
