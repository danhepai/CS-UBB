import Business
import Domeniu


def printeaza_meniu():
    """
    Printeaza in consola utilizatorului meniul.
    :return: none
    """
    print("Salut, aceasta este aplicatia ta pentru gestiunea cheltuielilor.")
    print("Ce doresti sa faci?")
    print("Alegeti optiunea prin a mentiona numarul optiunii si numarul suboptiunii (daca este cazul)")
    print("Adaugă:")
    print("1.1 Adaugă o nouă cheltuială")
    print("1.2 Actualizează cheltuială")
    print("Șterge:")
    print("2.1 Șterge toate cheltuielile pentru ziua dată")
    print("2.2 Șterge cheltuielile pentru un interval de timp")
    print("2.3 Șterge toate cheltuielile de un anumit tip")
    print("Căutări:")
    print("3.1 Tipărește toate cheltuielile mai mari decât o sumă dată")
    print("3.2 Tipărește toate cheltuielile efectuate înainte de o zi dată și mai mici decât o sumă")
    print("3.3 Tipărește toate cheltuielile de un anumit tip")
    print("Rapoarte:")
    print("4.1 Tipărește suma totală pentru un anumit tip de cheltuială")
    print("4.2 Găsește ziua în care suma cheltuită e maximă")
    print("4.3 Tipărește toate cheltuielile ce au o anumită sumă")
    print("4.4 Tipărește cheltuielile sortate după tip")
    print("Filtrare:")
    print("5.1 Elimină toate cheltuielile de un anumit tip")
    print("5.2 Elimină toate cheltuielile mai mici decât o sumă dată")
    print("Undo:")
    print("6 Reface ultima operație")
    print("Exit:")
    print("7 Exit aplicație")


def user_adauga_cheltuiala_la_buget(buget):
    print("Introduceti ziua (numar natural), suma(numar natural) si tipul cheltuielii, separate prin virgula:", '\n'
                                                                                                                "Tipurile disponibile sunt: mâncare, întreținere, îmbrăcăminte, telefon, altele")

    end = True
    while end:
        detalii = input(">>> ")
        detalii_list = detalii.split()
        if len(detalii_list) != 3:
            print("Detalii invalide! Incercati din nou.")
        elif not detalii_list[0].isdigit():
            print("Detalii invalide! Incercati din nou.")
        elif not detalii_list[1].isdigit():
            print("Detalii invalide! Incercati din nou.")
        else:
            end = False

    zi = int(detalii_list[0])
    suma = int(detalii_list[1])
    tip = detalii_list[2]
    Business.creeaza_cheltuiala_si_adauga_la_buget(zi, suma, tip, buget)


def user_actualizeaza_cheltuiala_la_buget(buget):
    cheltuieli = Domeniu.printeaza_toate_cheltuielile(buget)
    print("Alege-ti id-ul cheltuieli pe care vreti sa o actualizati: ")
    print(cheltuieli)
    end = True
    while end:
        id_user = input(">>> ")
        if not id_user.isdigit():
            print("Optiune invalida. Incercati din nou")
        elif int(id_user) < 1 or int(id_user) > len(buget):
            print("Optiune invalida. Incercati din nou2")
        else:
            end = False

    id_cheltuiala = int(id_user) - 1
    print("Super! Care sunt noile valori?")
    print("Introduceti ziua (numar natural), suma(numar natural) si tipul cheltuielii, separate prin virgula:")
    end = True
    while end:
        detalii = input(">>> ")
        detalii_list = detalii.split()
        if len(detalii_list) != 3:
            print("Detalii invalide! Incercati din nou.")
        else:
            end = False

    zi = int(detalii_list[0])
    suma = int(detalii_list[1])
    tip = detalii_list[2]
    Business.actualizeaza_cheltuiala_la_buget(zi, suma, tip, buget, id_cheltuiala)


def user_sterge_cheltuieli_la_zi_la_buget(buget):
    print("Introduceti o zi pentru care toate cheltuilile din acea zi vor fi sterse.")
    end = True
    while end:
        zi = input(">>> ")
        if not zi.isdigit():
            print("Optiune invalida. Incercati din nou")
        elif int(zi) < 1 or int(zi) > 31:
            print("Zi invalida. Incercati din nou")
        else:
            end = False
    zi = int(zi)
    Business.sterge_cheltuiala_la_zi_la_buget(buget, zi)


def user_sterge_cheltuieli_pentru_un_interval_de_timp_la_buget(buget):
    print(
        "Introduceti o zi de inceput si o zi de sfarsit, iar toate cheltuielile din acel interval inchis de timp vor fi sterse.")
    end = True
    while end:
        cmd = input(">>>")
        cmd_list = cmd.split()
        if len(cmd_list) != 2:
            print("Optiune invalida. Incercati din nou:")
        else:
            zi_inceput = cmd_list[0]
            zi_sfarsit = cmd_list[1]
            if not zi_inceput.isdigit():
                print("Optiune invalida. Incercati din nou")
            elif int(zi_inceput) < 1 or int(zi_inceput) > 31:
                print("Zi invalida. Incercati din nou")
            elif not zi_sfarsit.isdigit():
                print("Optiune invalida. Incercati din nou")
            elif int(zi_sfarsit) < 1 or int(zi_sfarsit) > 31:
                print("Zi invalida. Incercati din nou")
            else:
                end = False

    zi_inceput = int(zi_inceput)
    zi_sfarsit = int(zi_sfarsit)
    Business.sterge_cheltuieli_pentru_un_interval_de_timp_la_buget(buget, zi_inceput, zi_sfarsit)


def user_sterge_cheltuieli_pentru_un_anumit_tip_la_buget(buget):
    print("Introduceti un tip de cheltuiala")
    tip = input(">>>")
    Business.sterge_cheltuieli_pentru_un_anumit_tip_la_buget(buget, tip)


def user_tipareste_toate_cheltuielile_mai_mari_ca_o_suma(buget):
    print("Introduceti o suma pentru care se vor afisa toate cheltuilelile cu suma mai mare:")
    end = True
    while end:
        suma = input(">>> ")
        if not suma.isdigit():
            print("Optiune invalida. Incercati din nou")
        else:
            end = False

    suma = int(suma)
    print("Cheltuielile dvs sunt:")
    print(Business.tipareste_toate_cheltuielile_mai_mari_ca_o_suma(buget, suma))


def user_tipareste_cheltuieli_efectuate_inainte_de_zi_si_mai_mici_decat_o_suma(buget):
    print("Introduceti o zi si o suma si se vor tipari toate cheltuielile efectuate inainte de acea zi si mai mici "
          "decat acea suma:")
    end = True
    while end:
        cmd = input(">>> ")
        cmd_list = cmd.split()
        if len(cmd_list) != 2:
            print("Optiune invalida. Incercati din nou")
        else:
            zi = cmd_list[0]
            suma = cmd_list[1]
            if not zi.isdigit() or not suma.isdigit():
                print("Optiune invalida. Incercati din nou")
            else:
                end = False

    zi = int(zi)
    suma = int(suma)
    print("Cheltuielile dvs sunt:")
    print(Business.tipareste_cheltuieli_efectuate_inainte_de_zi_si_mai_mici_decat_o_suma(buget, zi, suma))


def user_tipareste_cheltuieli_de_un_anumit_tip(buget):
    print("Introduceti un tip de cheltuiala")
    tip = input(">>> ")
    print("Cheltuielile dvs sunt:")
    print(Business.tipareste_cheltuieli_de_un_anumit_tip(buget, tip))


def user_tipareste_suma_totala_pentru_un_tip_de_cheltuiala(buget):
    print("Introduceti un tip de cheltuiala")
    tip = input(">>> ")
    suma = Business.tipareste_suma_totala_pentru_un_tip_de_cheltuiala(buget, tip)
    return suma


def user_gaseste_ziua_cu_cheltuiala_maxima(buget):
    ziua = Business.gaseste_ziua_cu_cheltuiala_maxima(buget)
    return ziua


def user_tipareste_cheltuieli_de_un_anumita_suma(buget):
    print("Introduceti o suma pentru care se vor afisa toate cheltuilelile care au aceasta suma:")
    end = True
    while end:
        suma = input(">>> ")
        if not suma.isdigit():
            print("Optiune invalida. Incercati din nou")
        else:
            end = False

    suma = int(suma)
    print("Cheltuielile dvs sunt:")
    print(Business.tipareste_cheltuieli_de_o_anumita_suma(buget, suma))


def user_tipareste_cheltuieli_sortate_dupa_tip(buget):
    print(Business.tipareste_cheltuieli_sortate_dupa_tip(buget))


def user_filtreaza_toate_cheltuielile_de_un_tip(buget, buget_secundar):
    print("Introduceti un tip de cheltuiala")
    tip = input(">>> ")
    Business.filtreaza_toate_cheltuielile_de_un_tip(buget, buget_secundar, tip)


def user_filtreaza_toate_cheltuielile_mai_mici_decat_o_suma(buget, buget_secundar):
    print("Introduceti o suma pentru care se vor filtra toate cheltuilelile care au aceasta suma:")
    end = True
    while end:
        suma = input(">>> ")
        if not suma.isdigit():
            print("Optiune invalida. Incercati din nou")
        else:
            end = False

    suma = int(suma)
    Business.filtreaza_toate_cheltuielile_mai_mici_decat_o_suma(buget, buget_secundar, suma)


def ruleaza_aplicatia(buget, buget_secundar, undo_list):
    undo_list = []

    printeaza_meniu()
    while True:
        cmd = input(">>> ")
        cmd_list = cmd.split()
        first_option = cmd_list[0]
        if len(cmd_list) > 1:
            second_option = cmd_list[1]
        if len(cmd_list) > 2:
            print("Optiune invalida. Incercati din nou:")
        else:
            if first_option == "7":
                print("Bugetul este: ", buget)
                print("La revedere!")
                return

            elif first_option == "1":
                if second_option == "1":
                    end = True
                    while end:
                        try:
                            user_adauga_cheltuiala_la_buget(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "2":
                    end = True
                    while end:
                        try:
                            user_actualizeaza_cheltuiala_la_buget(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                else:
                    print("Optiune invalida. Incercati din nou:")

            elif first_option == "2":
                if second_option == "1":
                    end = True
                    while end:
                        try:
                            user_sterge_cheltuieli_la_zi_la_buget(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "2":
                    end = True
                    while end:
                        try:
                            user_sterge_cheltuieli_pentru_un_interval_de_timp_la_buget(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "3":
                    end = True
                    while end:
                        try:
                            user_sterge_cheltuieli_pentru_un_anumit_tip_la_buget(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                else:
                    print("Optiune invalida. Incercati din nou:")

            elif first_option == "3":
                if second_option == "1":
                    end = True
                    while end:
                        try:
                            user_tipareste_toate_cheltuielile_mai_mari_ca_o_suma(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "2":
                    end = True
                    while end:
                        try:
                            user_tipareste_cheltuieli_efectuate_inainte_de_zi_si_mai_mici_decat_o_suma(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "3":
                    end = True
                    while end:
                        try:
                            user_tipareste_cheltuieli_de_un_anumit_tip(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                else:
                    print("Optiune invalida. Incercati din nou:")

            elif first_option == "4":
                if second_option == "1":
                    end = True
                    while end:
                        try:
                            suma = user_tipareste_suma_totala_pentru_un_tip_de_cheltuiala(buget)
                            print("Suma tuturor cheltuielilor este:", suma)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "2":
                    end = True
                    while end:
                        try:
                            ziua = user_gaseste_ziua_cu_cheltuiala_maxima(buget)
                            print("Ziua cu suma maxima este:", ziua)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "3":
                    end = True
                    while end:
                        try:
                            user_tipareste_cheltuieli_de_un_anumita_suma(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "4":
                    end = True
                    while end:
                        try:
                            print("Cheltuielile sortate dupa tip sunt:")
                            user_tipareste_cheltuieli_sortate_dupa_tip(buget)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                else:
                    print("Optiune invalida. Incercati din nou:")

            elif first_option == "5":
                if second_option == "1":
                    end = True
                    while end:
                        try:
                            user_filtreaza_toate_cheltuielile_de_un_tip(buget, buget_secundar)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                elif second_option == "2":
                    end = True
                    while end:
                        try:
                            user_filtreaza_toate_cheltuielile_mai_mici_decat_o_suma(buget, buget_secundar)
                            print("Finalizat! Alege alta optiune din meniu:")
                            end = False
                        except ValueError as ve:
                            print(ve)
                else:
                    print("Optiune invalida. Incercati din nou:")

            elif first_option == "6":
                buget = Business.undo_buget(undo_list)
                buget_secundar = Business.undo_buget_secundar(undo_list)
                undo_list.pop()
                print("Finalizat! ")
            else:
                print("Optiune invalida. Incercati din nou:")
