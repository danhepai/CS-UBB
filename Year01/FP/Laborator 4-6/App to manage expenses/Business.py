import Domeniu
import Validari
import Repository


def creeaza_cheltuiala_si_adauga_la_buget(zi, suma, tip, buget):
    cheltuiala = Domeniu.creeaza_cheltuiala(zi, suma, tip)  # domeniu
    Validari.valideaza_cheltuiala(cheltuiala)  # validare
    Repository.adauga_cheltuiala_la_buget(cheltuiala, buget)  # functionalitati


def actualizeaza_cheltuiala_la_buget(zi, suma, tip, buget, id):
    cheltuiala = Domeniu.creeaza_cheltuiala(zi, suma, tip)  # domeniu
    Validari.valideaza_cheltuiala(cheltuiala)  # validare
    Repository.actualizeaza_cheltuiala(cheltuiala, id, buget)


def sterge_cheltuiala_la_zi_la_buget(buget, zi):
    Validari.valideaza_zi(zi)
    for cheltuiala in buget:
        if Domeniu.get_zi(cheltuiala) == zi:
            Repository.sterge_cheltuiala_din_buget(cheltuiala, buget)


def sterge_cheltuieli_pentru_un_interval_de_timp_la_buget(buget, zi_inceput, zi_sfarsit):
    Validari.valideaza_interval_de_zile(zi_inceput, zi_sfarsit)
    for cheltuiala in buget:
        if zi_inceput <= Domeniu.get_zi(cheltuiala) <= zi_sfarsit:
            Repository.sterge_cheltuiala_din_buget(cheltuiala, buget)


def sterge_cheltuieli_pentru_un_anumit_tip_la_buget(buget, tip):
    Validari.valideaza_tip_de_cheltuiala(tip)
    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == tip:
            Repository.sterge_cheltuiala_din_buget(cheltuiala, buget)


def tipareste_toate_cheltuielile_mai_mari_ca_o_suma(buget, suma):
    Validari.valideaza_suma(suma)
    index = 1
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        if Domeniu.get_suma(cheltuiala) >= suma:
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ")
            index += 1

    return toate_cheltuielile_str


def tipareste_cheltuieli_efectuate_inainte_de_zi_si_mai_mici_decat_o_suma(buget, zi, suma):
    Validari.valideaza_suma(suma)
    Validari.valideaza_zi(zi)
    index = 1
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        if Domeniu.get_suma(cheltuiala) < suma and Domeniu.get_zi(cheltuiala) < zi:
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ")
            index += 1

    return toate_cheltuielile_str


def tipareste_cheltuieli_de_un_anumit_tip(buget, tip):
    Validari.valideaza_tip_de_cheltuiala(tip)
    index = 1
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == tip:
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ")
            index += 1

    return toate_cheltuielile_str


def tipareste_suma_totala_pentru_un_tip_de_cheltuiala(buget, tip):
    Validari.valideaza_tip_de_cheltuiala(tip)
    suma = 0
    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == tip:
            suma += Domeniu.get_suma(cheltuiala)

    return suma


def gaseste_ziua_cu_cheltuiala_maxima(buget):
    suma_max = 0
    ziua = 0
    for cheltuiala in buget:
        if Domeniu.get_suma(cheltuiala) >= suma_max:
            suma_max = Domeniu.get_suma(cheltuiala)
            ziua = Domeniu.get_zi(cheltuiala)

    Validari.valideaza_zi_pentru_cheltuiala_maxima(ziua)
    return ziua


def tipareste_cheltuieli_de_o_anumita_suma(buget, suma):
    index = 1
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        if Domeniu.get_suma(cheltuiala) == suma:
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    return toate_cheltuielile_str


def tipareste_cheltuieli_sortate_dupa_tip(buget):
    index = 1
    toate_cheltuielile_str = ""
    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == "mancare":
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == "intretinere":
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == "imbracaminte":
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == "telefon":
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == "altele":
            toate_cheltuielile_str += Domeniu.printeaza_o_cheltuiala(cheltuiala, f"{index} -> ") + "\n"
            index += 1

    return toate_cheltuielile_str


def filtreaza_toate_cheltuielile_de_un_tip(buget, buget_secundar, tip):
    for cheltuiala in buget:
        if Domeniu.get_tip(cheltuiala) == tip:
            Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_secundar)
            Repository.sterge_cheltuiala_din_buget(cheltuiala, buget)


def filtreaza_toate_cheltuielile_mai_mici_decat_o_suma(buget, buget_secundar, suma):
    for cheltuiala in buget:
        if Domeniu.get_suma(cheltuiala) < suma:
            Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_secundar)
            Repository.sterge_cheltuiala_din_buget(cheltuiala, buget)


def adauga_stare_la_undo_list(buget, buget_secundar, undo_list):
    stare = Repository.creeaza_stare(buget, buget_secundar)
    Repository.adauga_stare_la_undo_list(stare, undo_list)


def undo_buget(undo_list):
    return Repository.get_buget_din_ultima_stare(undo_list)


def undo_buget_secundar(undo_list):
    return Repository.get_buget_secundar_din_ultima_stare(undo_list)
