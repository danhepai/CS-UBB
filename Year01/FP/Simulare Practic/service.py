import operator


class Service:
    """
    Description: Abstract data type pentru service-ul aplicatiei. Face legatura intre UI si Repository
    :return:
    """
    def __init__(self, repoConcurenti, repoParticipari):
        """
        Description: Constructor
        :param: repository pentru concurenti, repository pentru participari
        :return:
        """
        self.__repoConcurenti = repoConcurenti
        self.__repoParticipari = repoParticipari

    def afisare_concurenti_dupa_an(self, an):
        """
        Description: Creeaza un string cu toti concurentii care s-au nascut dupa anul introdus de utilizator
        :return: string
        """
        ans = ""
        concurenti = self.__repoConcurenti.get_toti_concurentii()
        for concurent in concurenti:
            if concurent.getAn() > int(an):
                ans += str(concurent) + '\n'

        if ans == "":
            return f"Nu sunt concurenti nascuti dupa anul: {an}\n"
        else:
            return ans

    def afisare_clasament_pe_tari(self):
        """
        Description: Creeaza un string cu toate tarile ce au participat si punctajele lor
        :return: string
        """
        ans = ""
        participari = self.__repoParticipari.get_toate_participarile()
        tari = {}

        for participare in participari:
            concurent = self.__repoConcurenti.get_concurent_by_id(participare.getIdConcurent())
            if concurent.getTara() not in tari:
                tari[concurent.getTara()] = int(participare.getPunctaj())
            else:
                tari[concurent.getTara()] += int(participare.getPunctaj())

        tari_sorted = dict(sorted(tari.items(), key=operator.itemgetter(1), reverse=True))
        for tara in tari_sorted:
            ans += f"Tara: {tara.upper()}" + f" Puntaj: {tari_sorted[tara]}" + '\n'

        return ans
