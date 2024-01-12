import Domeniu
import Business
import Validari
import Repository


def domain_tests():
    def testeaza_get_zi():
        assert (Domeniu.get_zi(Domeniu.creeaza_cheltuiala(1, 2, "mancare")) == 1)
        assert (Domeniu.get_zi(Domeniu.creeaza_cheltuiala(3, 4, "telefon")) == 3)

    testeaza_get_zi()

    def testeaza_get_suma():
        assert (Domeniu.get_suma(Domeniu.creeaza_cheltuiala(1, 2, "mancare")) == 2)
        assert (Domeniu.get_suma(Domeniu.creeaza_cheltuiala(3, 4, "telefon")) == 4)

    testeaza_get_suma()

    def testeaza_get_tip():
        assert (Domeniu.get_tip(Domeniu.creeaza_cheltuiala(1, 2, "mancare")) == "mancare")
        assert (Domeniu.get_tip(Domeniu.creeaza_cheltuiala(3, 4, "telefon")) == "telefon")

    testeaza_get_tip()

    def testeaza_creare_cheltuiala():
        cheltuiala = Domeniu.creeaza_cheltuiala(10, 100, "mancare")
        assert (Domeniu.get_zi(cheltuiala) == 10)
        assert (Domeniu.get_suma(cheltuiala) == 100)
        assert (Domeniu.get_tip(cheltuiala) == "mancare")

    testeaza_creare_cheltuiala()

    def testeaza_printeaza_cheltuiala():
        cheltuiala = Domeniu.creeaza_cheltuiala(1, 2, "mancare")
        assert (Domeniu.printeaza_o_cheltuiala(cheltuiala, "") == "ZIUA: 1 SUMA: 2 TIP: mancare")

    testeaza_printeaza_cheltuiala()

    def testeaza_printeaza_toate_cheltuielile():
        cheltuiala_unu = Domeniu.creeaza_cheltuiala(1, 2, "mancare")
        cheltuiala_doi = Domeniu.creeaza_cheltuiala(3, 4, "telefon")
        buget_de_test = []
        Repository.adauga_cheltuiala_la_buget(cheltuiala_unu, buget_de_test)
        Repository.adauga_cheltuiala_la_buget(cheltuiala_doi, buget_de_test)
        string_de_test = Repository.printeaza_toate_cheltuielile(buget_de_test)
        assert (string_de_test == "ID: 1 ZIUA: 1 SUMA: 2 TIP: mancare\nID: 2 ZIUA: 3 SUMA: 4 TIP: telefon\n")

    testeaza_printeaza_toate_cheltuielile()

    def testeaza_adauga_cheltuiala_la_buget():
        cheltuiala = Domeniu.creeaza_cheltuiala(1, 1, "mancare")
        buget_de_test = []
        #functie de creeaza buget
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_de_test)
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_de_test)
        assert (Repository.get_dimensiune_buget(buget_de_test) == 2)

    testeaza_adauga_cheltuiala_la_buget()

    def testeaza_sterge_cheltuiala_la_buget():
        cheltuiala = Domeniu.creeaza_cheltuiala(1, 1, "mancare")
        buget_de_test = []
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_de_test)
        Repository.sterge_cheltuiala_din_buget(cheltuiala, buget_de_test)
        assert (Repository.get_dimensiune_buget(buget_de_test) == 0)

    testeaza_sterge_cheltuiala_la_buget()

    def testeaza_actualizeaza_cheltuiala_la_buget():
        cheltuiala_init = Domeniu.creeaza_cheltuiala(1, 1, "mancare")
        cheltuiala_noua = Domeniu.creeaza_cheltuiala(2, 3, "telefon")
        buget_de_test = []
        Repository.adauga_cheltuiala_la_buget(cheltuiala_init, buget_de_test)
        Repository.actualizeaza_cheltuiala(cheltuiala_noua, 0, buget_de_test)
        assert (Repository.get_cheltuiala(buget_de_test, 0) == cheltuiala_noua)

    testeaza_actualizeaza_cheltuiala_la_buget()

    def testeaza_dimensiune_buget():
        cheltuiala = Domeniu.creeaza_cheltuiala(1, 1, "mancare")
        buget_de_test = []
        assert (Repository.get_dimensiune_buget(buget_de_test) == 0)
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget_de_test)
        assert (Repository.get_dimensiune_buget(buget_de_test) == 1)

    testeaza_dimensiune_buget()

    def testeaza_get_cheltuiala():
        buget = []
        cheltuiala = Domeniu.creeaza_cheltuiala(1, 1, "mancare")
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget)
        assert (Repository.get_cheltuiala(buget, 0) == cheltuiala)

    testeaza_get_cheltuiala()


def business_tests():
    def testeaza_creeaza_cheltuiala_si_adauga_la_buget():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 1, "mancare", buget_de_test)
        assert (Repository.get_dimensiune_buget(buget_de_test) != 0)

    testeaza_creeaza_cheltuiala_si_adauga_la_buget()

    def testeaza_actualizare_de_cheltuiala_din_buget():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 1, "mancare", buget_de_test)
        Business.actualizeaza_cheltuiala_la_buget(2, 2, "telefon", buget_de_test, 0)
        assert (Repository.get_cheltuiala(buget_de_test, 0) == [2, 2, "telefon"])

    testeaza_actualizare_de_cheltuiala_din_buget()

    def testeaza_stergere_cheltuiala_din_buget():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 1, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 10, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(5, 1, "intretinere", buget_de_test)
        Business.sterge_cheltuiala_la_zi_la_buget(buget_de_test, 1)
        Business.sterge_cheltuieli_pentru_un_anumit_tip_la_buget(buget_de_test, "telefon")
        Business.sterge_cheltuieli_pentru_un_interval_de_timp_la_buget(buget_de_test, 4, 6)
        assert (Repository.get_dimensiune_buget(buget_de_test) == 0)

    testeaza_stergere_cheltuiala_din_buget()

    def testeaza_tiparire_cheltuieli_mai_mari_ca_suma():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 3, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 1, "telefon", buget_de_test)
        string_de_test = Business.tipareste_toate_cheltuielile_mai_mari_ca_o_suma(buget_de_test, 2)
        assert (string_de_test == "1 -> ZIUA: 1 SUMA: 3 TIP: mancare")

    testeaza_tiparire_cheltuieli_mai_mari_ca_suma()

    def testeaza_tiparire_cheltuieli_inainte_de_zi_si_mai_mici_decat_o_suma():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "telefon", buget_de_test)
        string_de_test = Business.tipareste_cheltuieli_efectuate_inainte_de_zi_si_mai_mici_decat_o_suma(buget_de_test,
                                                                                                        30, 99)
        assert (string_de_test == "1 -> ZIUA: 20 SUMA: 10 TIP: telefon")

    testeaza_tiparire_cheltuieli_inainte_de_zi_si_mai_mici_decat_o_suma()

    def testeaza_tiparire_cheltuieli_de_un_anumit_tip():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "telefon", buget_de_test)
        string_de_test = Business.tipareste_cheltuieli_de_un_anumit_tip(buget_de_test, "telefon")
        assert (string_de_test == "1 -> ZIUA: 20 SUMA: 10 TIP: telefon")

    testeaza_tiparire_cheltuieli_de_un_anumit_tip()

    def testeaza_tiparire_suma_totala_pentru_un_tip_de_cheltuiala():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "mancare", buget_de_test)
        suma_de_test = Business.tipareste_suma_totala_pentru_un_tip_de_cheltuiala(buget_de_test, "telefon")
        assert (suma_de_test == 110)

    testeaza_tiparire_suma_totala_pentru_un_tip_de_cheltuiala()

    def testeaza_gaseste_ziua_cu_cheltuiala_maxim():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "mancare", buget_de_test)
        zi_de_test = Business.gaseste_ziua_cu_cheltuiala_maxima(buget_de_test)
        assert (zi_de_test == 10)

    testeaza_gaseste_ziua_cu_cheltuiala_maxim()

    def testeaza_tipareste_cheltuieli_de_o_anumita_suma():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(2, 10, "telefon", buget_de_test)
        string_de_test = Business.tipareste_cheltuieli_de_o_anumita_suma(buget_de_test, 10)
        assert (string_de_test == "1 -> ZIUA: 20 SUMA: 10 TIP: mancare\n2 -> ZIUA: 2 SUMA: 10 TIP: telefon\n")

    testeaza_tipareste_cheltuieli_de_o_anumita_suma()

    def testeaza_tipareste_cheltuieli_sortate_dupa_tip():
        buget_de_test = []
        Business.creeaza_cheltuiala_si_adauga_la_buget(10, 100, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(20, 10, "mancare", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(2, 10, "telefon", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(2, 10, "intretinere", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(1, 1, "altele", buget_de_test)
        Business.creeaza_cheltuiala_si_adauga_la_buget(3, 2, "imbracaminte", buget_de_test)
        string_de_test = Business.tipareste_cheltuieli_sortate_dupa_tip(buget_de_test)
        assert (string_de_test == "1 -> ZIUA: 20 SUMA: 10 TIP: mancare\n2 -> ZIUA: 2 SUMA: 10 TIP: intretinere\n3 -> "
                                  "ZIUA: 3 SUMA: 2 TIP: imbracaminte\n4 -> ZIUA: 10 SUMA: 100 TIP: telefon\n5 -> ZIUA: 2 "
                                  "SUMA: 10 TIP: telefon\n6 -> ZIUA: 1 SUMA: 1 TIP: altele\n")

    testeaza_tipareste_cheltuieli_sortate_dupa_tip()

    def testeaza_filtreaza_toate_cheltuielile_de_un_tip():
        buget = []
        buget_secundar = []
        cheltuiala = Domeniu.creeaza_cheltuiala(10,10, "mancare")
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget)
        Business.filtreaza_toate_cheltuielile_de_un_tip(buget, buget_secundar,"mancare")
        assert (Repository.get_dimensiune_buget(buget) == 0)
        assert (Repository.get_dimensiune_buget(buget_secundar) == 1)

    testeaza_filtreaza_toate_cheltuielile_de_un_tip()


    def testeaza_filtreaza_toate_cheltuielile_mai_mici_decat_o_suma():
        buget = []
        buget_secundar = []
        cheltuiala = Domeniu.creeaza_cheltuiala(10,10, "mancare")
        Repository.adauga_cheltuiala_la_buget(cheltuiala, buget)
        Business.filtreaza_toate_cheltuielile_mai_mici_decat_o_suma(buget, buget_secundar, 11)
        assert (Repository.get_dimensiune_buget(buget) == 0)
        assert (Repository.get_dimensiune_buget(buget_secundar) == 1)

    testeaza_filtreaza_toate_cheltuielile_mai_mici_decat_o_suma()


def validation_tests():
    def testeaza_valideaza_cheltuiala():
        cheltuiala_corecta = Domeniu.creeaza_cheltuiala(1,1,"telefon")
        cheletuiala_invalida = Domeniu.creeaza_cheltuiala(32,-1,"bere")
        try:
            Validari.valideaza_cheltuiala(cheltuiala_corecta)
            assert True
        except ValueError:
            assert False

        try:
            Validari.valideaza_cheltuiala(cheletuiala_invalida)
            assert False
        except ValueError as ve:
            assert (str(ve) == "Zi invalida!\nSuma invalida! Nu poate fi negativa!\nTip invalid!\n")

    testeaza_valideaza_cheltuiala()

    def testeaza_valideaza_interval_de_timp():
        try:
            Validari.valideaza_interval_de_zile(5,4)
            assert False
        except ValueError as ve:
            assert (str(ve) == "Interval de timp invalid! \n")

    testeaza_valideaza_interval_de_timp()


def ruleaza_toate_testele():
    domain_tests()
    business_tests()
    validation_tests()
