from Pozdrav import pozdrav
from Ucitavanje_modela_aviona import *
from Ucitavanje_konkretnih_letova import *
from Ucitavanje_letova import *
from Ucitavanje_korisnika import *
from collections import Counter
import datetime
from Ucitavanje_vremena_dolaska import *
from Ucitavanje_vremena_polaska import *
from datetime import timedelta
from Ucitavanje_karata import *
from enumeracija import TipPrijaveNaLet

trenutno_vreme = datetime.datetime.now()

broj_slobodnih_sedista = []

recnik_unetih_podataka = {}

lista_sifri_konkretnih_letova = []

pretvaranje_slova_u_brojeve = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                               "K": 11, "L": 12, "M": 13}

sifra_kolone_redovi = []

kolone_i_redovi = []

slova = 0

matrica = []

podmatrica = []

lista_za_unos = [0]

lista_broja_sedista = []

novo_ime = "novo ime"

novo_prezime = "novo prezime"

lista_za_unos_prijava_na_let = [0]


def prodavac():
    file1 = open("korisnici.txt", "r")
    sadrzaj1 = file1.readlines()

    uneto_korisnicko_ime = input("\nUnesite korisnicko ime: ")
    uneta_lozinka = input("Unesite lozinku: ")

    for linija in sadrzaj1:
        reci = linija.split("|")
        korisnicko_ime = reci[0]
        lozinka = reci[1]
        ime = reci[2]
        prezime = reci[3]
        uloga = reci[4].replace('\n', '')
        korisnici = {"korisnicko ime": korisnicko_ime,
                    "lozinka": lozinka,
                    "ime": ime,
                    "prezime": prezime,
                    "uloga": uloga}
        korisnicko_ime.join(korisnici["korisnicko ime"])
        lozinka.join(korisnici["lozinka"])

        if korisnici["korisnicko ime"] == uneto_korisnicko_ime and korisnici["lozinka"] == uneta_lozinka:

            if uloga == "prodavac":

                print("\nUspesno ste se prijavili kao prodavac!")
                recnik_unetih_podataka["uneto korisnicko ime"] = uneto_korisnicko_ime
                recnik_unetih_podataka["uneta lozinka"] = uneta_lozinka
                meni_za_prodavca()
                return

    print("\nUneli ste pogresno korisnicko ime ili lozinku. Pokusajte ponovo.")
    izbor = input("Unesite '1' ako zelite da pokusate opet. Unesite 'b' ako zelite da se vratite nazad u glavni meni. ")

    while izbor not in ("1", "b"):
        print("\nNiste uneli odgovarajucu opciju. Pokusajte ponovo.")
        izbor = input("\nUnesite '1' ako zelite da pokusate opet. Unesite 'b' ako zelite da se vratite nazad: ")

    if izbor == "1":
        prodavac()
    elif izbor == "b":
        return

    file1.close()


def print_meni_za_prodavca():
    print("\nIzaberite jednu od sledecih opcija:\n ")
    print("1 - Prodaja karata")
    print("2 - Prijava na let (check-in)")
    print("3 - Izmena karte")
    print("4 - Brisanje karte")
    print("5 - Pretraga prodatih karata")
    print("o - Odjava")
    print("e - Izlazak iz aplikacije")


def racunanje_broja_sedista_po_modelu_aviona():

    for i in podaci_modeli_aviona:
        broj_sedista = {}
        naziv_modela = i["naziv modela"]
        broj_redova = int(i["broj redova"])
        broj_sedista_u_redu = int(pretvaranje_slova_u_brojeve[i["broj sedista u redu"]])
        ukupan_broj_sedista = broj_redova * broj_sedista_u_redu

        broj_sedista["naziv modela"] = naziv_modela
        broj_sedista["ukupan broj sedista"] = ukupan_broj_sedista
        broj_slobodnih_sedista.append(broj_sedista)

racunanje_broja_sedista_po_modelu_aviona()


def recnik_koji_spaja_sifre_i_sedista():

    for i in podaci_konkretni_letovi:

        for j in podaci_avionski_letovi:

            for k in broj_slobodnih_sedista:
                recnik = {}

                if i["broj konkretnog leta"] == j["broj leta"] and j["model aviona"] == k["naziv modela"]:

                    recnik["sifra"] = i["sifra konkretnog leta"]
                    recnik["broj sedista"] = k["ukupan broj sedista"]
                    lista_broja_sedista.append(recnik)

recnik_koji_spaja_sifre_i_sedista()


def meni_za_prodavca():
    print_meni_za_prodavca()

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2", "3", "4", "5", "o", "e"):
        print("\nNiste izabrali odgovarajucu opciju!\n")
        print("Pokusajte ponovo. ")
        print_meni_za_prodavca()
        izbor = input("\nUnesite opciju: ")

    if izbor == "1":
        odabir_konkretnog_leta()
        odabir_putnika()
        nastavak_prodaje()
        meni_za_prodavca()

    elif izbor == "2":
        prijava_na_let(TipPrijaveNaLet.NORMAL.value)
        nastavak_prijave_na_let()
        meni_za_prodavca()

    elif izbor == "3":
        izmena_karte()
        meni_za_prodavca()

    elif izbor == "4":
        brisanje_karte()
        meni_za_prodavca()

    elif izbor == "5":
        pretraga_prodatih_karata()
        meni_za_prodavca()

    elif izbor == "o":
        print("\nOdjavili ste se!\n")
        return

    elif izbor == "e":
        pozdrav()


def odabir_konkretnog_leta():

    for i in podaci_konkretni_letovi:

        datum_poletanja = i["datum polaska"]
        broj = datum_poletanja.split(".")
        dan = broj[0]
        mesec = broj[1]
        godina = broj[2]
        dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

        if dan_leta > trenutno_vreme:

            lista_sifri_konkretnih_letova.append(i["sifra konkretnog leta"])

    unos = input("\nUnesite sifru leta: ")

    while unos not in lista_sifri_konkretnih_letova:
        print("\nIzabrali ste neodgovarajucu sifru ili sifru za let koji je vec poleteo. Pokusajte ponovo")
        unos = input("\nUnesite sifru leta: ")

    lista_za_unos[0] = unos

    smanjivanje_broja_sedista()

    for i in lista_broja_sedista:

        if i["broj sedista"] <= 0:

            print("Nazalost, nema slobodnih sedista za ovaj let.")
            meni_za_prodavca()


def odabir_putnika():

    global novo_ime
    global novo_prezime

    lista_korisnickih_imena = []

    print("\nUkoliko je kupac registrovan, unesite 1.")
    print("Ukoliko prodajete kartu za neregistrovanog kupca, unesite 2.")
    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2"):
        print("Niste izabrali odgovarajucu opciju!")
        izbor = input("Pokusajte ponovo: ")

    if izbor == "1":

        korisnicko_ime = input("\nUnesite korisnicko ime putnika: ")

        for j in podaci_korisnici:
            lista_korisnickih_imena.append(j["korisnicko ime"])

        while korisnicko_ime not in lista_korisnickih_imena:
            print("\nData osoba ne postoji.")
            print("Pokusajte ponovo")
            korisnicko_ime = input("\nUnesite korisnicko ime putnika: ")

        for i in podaci_korisnici:

            if i["korisnicko ime"] == korisnicko_ime:
                recnik_unetih_podataka["uneto korisnicko ime"] = i["korisnicko ime"]
                recnik_unetih_podataka["uneta lozinka"] = i["sifra"]

        potvrda_prodaje()

    elif izbor == "2":
        novo_ime = input("\nUnesite ime osobe: ")
        novo_prezime = input("Unesite prezime osobe: ")

        potvrda_prodaje_neregistrovanog_kupca()


def nastavak_prodaje():

    print("\nUkoliko zelite da prodate jos jednu kartu za isti konkretni let, unesite 1")
    print("Ukoliko zelite da prodate kartu za neki drugi let, unesite 2")
    print("Ukoliko zelite da se vratite nazad u meni za prodavca, unesite 3")

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2", "3"):
        print("\nNiste uneli odgovarajucu opciju!")
        izbor = input("\nPokusajte ponovo: ")

    if izbor == "1":

        smanjivanje_broja_sedista()

        for i in lista_broja_sedista:

            if i["broj sedista"] <= 0:
                print("Nazalost, nema slobodnih sedista za ovaj let.")
                meni_za_prodavca()

            else:
                odabir_putnika()

    elif izbor == "2":
        izbor_narednog_leta()

    elif izbor == "3":
        pass


def smanjivanje_broja_sedista():
    file = open("karte.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    umanjilac = 0
    brojac = 0

    for i in lista_za_unos:

        for linija in sadrzaj:
            reci = linija.split("|")
            sifra_leta = reci[2]
            umanjilac = umanjilac + sifra_leta.count(i)

            for j in lista_broja_sedista:

                for k in broj_slobodnih_sedista:

                    if i == j["sifra"]:
                        j["broj sedista"] = k["ukupan broj sedista"] - int(umanjilac)


def potvrda_prodaje():
    print("\nUkoliko zelite da potvrdite prodaju, unesite 1.")
    print("Ukoliko zelite da se vratite nazad, u meni za prodavca, unesite 2.")

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2"):
        print("\nNiste izabrali odgovarajucu opciju!")
        izbor = input("\nPokusajte ponovo: ")

    if izbor == "1":

        izrada_karte()
        print("\nKarta je prodata!")
        nastavak_prodaje()

    elif izbor == "2":
        meni_za_prodavca()


def izrada_karte():

    file = open("karte.txt", "r")
    sadrzaj = file.readlines()

    for linija in sadrzaj:
        reci = linija.split("|")
        broj_karte = int(reci[0])
        broj_kupovine = int(reci[1])

    file.close()

    broj_karte = broj_karte + 1
    broj_kupovine = broj_kupovine + 1

    file = open("karte.txt", "a")

    for j in lista_za_unos:

        for i in podaci_korisnici:

            if i["korisnicko ime"] == recnik_unetih_podataka["uneto korisnicko ime"]:

                korisnicko_ime = i["korisnicko ime"]
                broj_telefona = i["broj telefona"]
                email = i["email"]
                ime = i["ime"]
                prezime = i["prezime"]
                broj_pasosa = i["broj pasosa"]
                drzavljanstvo = i["drzavljanstvo"]
                pol = i["pol"]

                file.write("\n"+"{:04d}".format(broj_karte)+"|"+"{:02d}".format(broj_kupovine)+"|"+j+"|"+korisnicko_ime+"|"+broj_telefona+"|"
                           + email+"|"+ime+"|"+prezime+"|"+broj_pasosa+"|"+drzavljanstvo+"|"+pol)

    file.close()


def izbor_narednog_leta():

    aerodrom = 0
    datum_sletanja = 0
    razlika = 0

    for i in lista_za_unos:

        for j in podaci_konkretni_letovi:

            for k in podaci_avionski_letovi:

                if i == j["sifra konkretnog leta"] and j["broj konkretnog leta"] == k["broj leta"]:

                    aerodrom = k["sifra polazista"]

                    for m in podaci_vreme_polaska:

                        for n in podaci_vreme_dolaska:

                            if k["vreme polaska"] == m["vreme polaska"] and k["vreme dolaska"] == n[
                                "vreme dolaska"] \
                                and j["datum polaska"] == m["datum polaska"] and j["datum dolaska"] == n[
                                    "datum dolaska"]:

                                datum_prethodnog_leta = datetime.datetime(year=int(n["godine"]), month=int(n["meseci"]),
                                                                      day=int(n["dani"]), hour=int(n["sati"]),
                                                                      minute=int(n["minuti"]))

                                datum_narednog_leta = datetime.datetime(year=int(m["godine"]), month=int(m["meseci"]),
                                                                    day=int(m["dani"]), hour=int(m["sati"]),
                                                                    minute=int(m["minuti"]))

                                razlika = datum_narednog_leta - datum_prethodnog_leta

                                if k["sifra polazista"] == aerodrom and razlika < datetime.timedelta(minutes=120):
                                    print("\nIzaberite jedan od dostupnih letova za ovaj aerodrom: ")
                                    print(j["sifra konkretnog leta"])


    print("\nTrenutno nema letova sa istog aerodroma koji polecu u roku od 120 minuta posle"
    "sletanja prethodnog leta.")


def potvrda_prodaje_neregistrovanog_kupca():

    print("\nUkoliko zelite da potvrdite prodaju, unesite 1.")
    print("Ukoliko zelite da se vratite nazad, u meni za prodavca, unesite 2.")

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2"):
        print("\nNiste izabrali odgovarajucu opciju!")
        izbor = input("\nPokusajte ponovo: ")

    if izbor == "1":

        izrada_karte_neregistrovanog_korisnika()
        print("\nKarta je prodata!")

    elif izbor == "2":
        meni_za_prodavca()


def izrada_karte_neregistrovanog_korisnika():

    file = open("karte.txt", "r")
    sadrzaj = file.readlines()

    for linija in sadrzaj:
        reci = linija.split("|")
        broj_karte = int(reci[0])
        broj_kupovine = int(reci[1])

    file.close()

    broj_karte = broj_karte + 1
    broj_kupovine = broj_kupovine + 1

    file = open("karte.txt", "a")

    for j in lista_za_unos:

        file.write("\n" + "{:04d}".format(broj_karte) + "|" + "{:02d}".format(
        broj_kupovine) + "|" + j + "|" + novo_ime + "|" + novo_prezime + "|"
        + "-" + "|" + "-" + "|" + "-" + "|" + "-" + "|" + "-" + "|" + "-")

    file.close()


def spajanje_sifri_karata_i_sedista():

    for a in podaci_karte:

        for i in podaci_konkretni_letovi:

            for j in podaci_avionski_letovi:

                for k in podaci_modeli_aviona:
                    recnik_sedista = {}

                    if a["sifra leta"] == i["sifra konkretnog leta"] and i["broj konkretnog leta"] == j["broj leta"] and j["model aviona"] == k["naziv modela"]:

                        recnik_sedista["sifra karte"] = a["sifra karte"]
                        recnik_sedista["broj redova"] = k["broj redova"]
                        recnik_sedista["broj kolona"] = int(pretvaranje_slova_u_brojeve[k["broj sedista u redu"]])
                        sifra_kolone_redovi.append(recnik_sedista)

spajanje_sifri_karata_i_sedista()


def prijava_na_let(tip_prijave):

    global slova

    global matrica

    global podmatrica

    global lista_za_unos_prijava_na_let

    lista_broja_redova = 0

    lista_broja_kolona = 0

    lista_broja_slova = []

    duzina_linije1 = 0

    lista_karti_po_korisniku = []

    broj_reda = 1

    broj_kolone = 1

    lista_imena = []

    lista_prezimena = []

    file1 = open("karte.txt", "r")
    sadrzaj1 = file1.readlines()
    file1.close()

    for linija1 in sadrzaj1:
        reci1 = linija1.split("|")
        duzina_linijee = len(reci1)

    for i in podaci_karte:

        if recnik_unetih_podataka["uneto korisnicko ime"] == i["korisnicko ime"]:
            lista_karti_po_korisniku.append(i["sifra karte"])

    if tip_prijave == TipPrijaveNaLet.NORMAL.value:

        uneta_sifra_karte = input("\nUnesite sifru karte: ")

        lista_za_unos_prijava_na_let[0] = uneta_sifra_karte

        lista_za_unos_prijava_na_let[0] = uneta_sifra_karte

    elif tip_prijave == TipPrijaveNaLet.POVEZANI_LETOVI.value:

        uneta_sifra_karte = input("\nUnesite sifru karte: ")

        while uneta_sifra_karte not in lista_karti_po_korisniku:
            print("\nNiste uneli odgovarajucu kartu. Pokusajte ponovo")
            uneta_sifra_karte = input("\nUnesite sifru karte: ")

        aerodrom_prvog_leta = None
        aerodrom_drugog_leta = None

        for x in lista_za_unos_prijava_na_let:

            for i in podaci_karte:

                for j in podaci_konkretni_letovi:

                    for k in podaci_avionski_letovi:

                        if x == i["sifra karte"] and i["sifra leta"] == j["sifra konkretnog leta"] and \
                                j["broj konkretnog leta"] == k["broj leta"]:

                            aerodrom_prvog_leta = k["sifra polazista"]

                for m in podaci_karte:

                    for o in podaci_konkretni_letovi:

                        for l in podaci_avionski_letovi:

                            if uneta_sifra_karte == m["sifra karte"] and m["sifra leta"] == o[
                                "sifra konkretnog leta"] and \
                                    o["broj konkretnog leta"] == l["broj leta"]:
                                aerodrom_drugog_leta = l["sifra polazista"]

            if aerodrom_prvog_leta != aerodrom_drugog_leta:
                print("\nOva sifra leta oznacava let koji ne polazi sa istog aerodroma!")
                return

    else:

        uneta_sifra_karte = lista_za_unos_prijava_na_let[0]

        ime = input("\nUnesite ime osobe: ")
        prezime = input("Unesite prezime osobe: ")

        for j in podaci_korisnici:
            lista_imena.append(j["ime"])

        for k in podaci_korisnici:
            lista_prezimena.append(k["prezime"])

        while ime not in lista_imena or prezime not in lista_prezimena:
            print("\nData osoba ne postoji.")
            print("Pokusajte ponovo")
            ime = input("\nUnesite ime osobe: ")
            prezime = input("Unesite prezime osobe: ")


    print("")

    print("\nSlobodna mesta su oznacena sa O. Zauzeta su oznacena sa X.")

    print("")

    for m in podaci_karte:

        for n in podaci_konkretni_letovi:

            broj = n["datum polaska"].split(".")
            dan = broj[0]
            mesec = broj[1]
            godina = broj[2]
            dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

            razlika = dan_leta - trenutno_vreme

            if uneta_sifra_karte == m["sifra karte"] and m["sifra leta"] == n["sifra konkretnog leta"] and razlika > datetime.timedelta(hours=48):     #Pre provere promeniti znak iz < u >

                print("\nNe mozete se jos prijaviti na let. To mozete uraditi u periodu od 48 sati pre leta. \n")
                return

    for red in sifra_kolone_redovi:

        if red["sifra karte"] == uneta_sifra_karte:

            for domet in range(int(red["broj kolona"])):

                print("{:01d}".format(broj_kolone), end=' ')
                broj_kolone = broj_kolone + 1

    print("")
    print("")

    for i in sifra_kolone_redovi:

        if i["sifra karte"] == uneta_sifra_karte:

            if i["broj kolona"] == 8:

                matrica = [["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "]]

            elif i["broj kolona"] == 9:

                matrica = [["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "]]

            elif i["broj kolona"] == 13:

                matrica = [["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O ", "O "]]

            elif i["broj kolona"] == 6:

                matrica = [["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "],
                           ["O ", "O ", "O ", "O ", "O ", "O "]]

    for hy in sifra_kolone_redovi:

        if hy["sifra karte"] == uneta_sifra_karte:

            if hy["broj kolona"] == 8:

                file4 = open("zauzeta_sedista_1.txt", "r")

                matrica = []
                for linija in file4.readlines():
                    linija = linija.replace("\n", "")
                    matrica.append([x for x in linija.split(",")])
                file4.close()

            elif hy["broj kolona"] == 9:

                file5 = open("zauzeta_sedista_2.txt", "r")

                matrica = []
                for linija in file5.readlines():
                    linija = linija.replace("\n", "")
                    matrica.append([x for x in linija.split(",")])
                file5.close()

            elif hy["broj kolona"] == 13:

                file6 = open("zauzeta_sedista_3.txt", "r")

                matrica = []
                for linija in file6.readlines():
                    linija = linija.replace("\n", "")
                    matrica.append([x for x in linija.split(",")])
                file6.close()

            elif hy["broj kolona"] == 6:

                file7 = open("zauzeta_sedista_4.txt", "r")

                matrica = []
                for linija in file7.readlines():
                    linija = linija.replace("\n", "")
                    matrica.append([x for x in linija.split(",")])
                file7.close()

    for i in sifra_kolone_redovi:

        if i["sifra karte"] == uneta_sifra_karte:

            lista_broja_redova = i["broj redova"]

            lista_broja_kolona = i["broj kolona"]

            if duzina_linije1 <= 11:

                for redovi in matrica:

                    if i["broj kolona"] == 8:

                        print(str(redovi[0] + redovi[1] + redovi[2] + redovi[3] + redovi[4] + redovi[5] + redovi[6] +
                                  redovi[7]) + "   " + "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif i["broj kolona"] == 9:

                        print(str(redovi[0] + redovi[1] + redovi[2] + redovi[3] + redovi[4] + redovi[5] + redovi[6] +
                                redovi[7] + redovi[8]) + "   " + "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif i["broj kolona"] == 13:

                        print(str(redovi[0] + redovi[1] + redovi[2] + redovi[3] + redovi[4] + redovi[5] + redovi[6] +
                                redovi[7] + redovi[8] + redovi[9] + redovi[10] + redovi[11] + redovi[12]) + "   " + \
                        "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif i["broj kolona"] == 6:

                        print(str(redovi[0] + redovi[1] + redovi[2] + redovi[3] + redovi[4] + redovi[5]) + "   " + \
                        "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1



    uneti_red = int(input("\nUnesite broj reda: "))
    uneta_kolona = int(input("\nUnesite broj sedista u redu: "))

    while int(uneti_red) < 0 or int(uneti_red) > int(lista_broja_redova) or int(uneta_kolona) < 0 or int(uneta_kolona) > int(lista_broja_kolona):

        print("\nNiste uneli odgovarajuc broj reda ili odgovarajuce mesto u redu. Pokusajte ponovo.")

        uneti_red = int(input("\nUnesite broj reda: "))
        uneta_kolona = int(input("Unesite broj sedista u redu: "))

    print("")

    while matrica[uneti_red - 1][uneta_kolona - 1] == "X ":

        print("\nOvo sediste je vec zauzeto. Probajte sa nekim drugim.")
        uneti_red = int(input("\nUnesite broj reda: "))
        uneta_kolona = int(input("Unesite broj sedista u redu: "))

    broj_kolone = 1

    for red in sifra_kolone_redovi:

        if red["sifra karte"] == uneta_sifra_karte:

            for domet in range(int(red["broj kolona"])):
                print("{:01d}".format(broj_kolone), end=' ')
                broj_kolone = broj_kolone + 1

    print("")
    print("")

    matrica[uneti_red - 1][uneta_kolona - 1] = "X "

    broj_reda = 1

    for b in sifra_kolone_redovi:

        if b["sifra karte"] == uneta_sifra_karte:

            lista_broja_redova = b["broj redova"]

            lista_broja_kolona = b["broj kolona"]

            if duzina_linije1 <= 11:

                for redoviiiii in matrica:

                    if b["broj kolona"] == 8:

                        print(str(redoviiiii[0] + redoviiiii[1] + redoviiiii[2] + redoviiiii[3] + redoviiiii[4] +
                                    redoviiiii[5] + redoviiiii[6] +
                                redoviiiii[7]) + "   " + "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif b["broj kolona"] == 9:

                        print(str(redoviiiii[0] + redoviiiii[1] + redoviiiii[2] + redoviiiii[3] + redoviiiii[4] +
                                  redoviiiii[5] + redoviiiii[6] +
                                  redoviiiii[7] + redoviiiii[8]) + "   " + "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif b["broj kolona"] == 13:

                        print(str(redoviiiii[0] + redoviiiii[1] + redoviiiii[2] + redoviiiii[3] + redoviiiii[4] +
                                  redoviiiii[5] + redoviiiii[6] +
                                  redoviiiii[7] + redoviiiii[8] + redoviiiii[9] + redoviiiii[10] + redoviiiii[11] +
                                  redoviiiii[12]) + "   " + \
                              "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

                    elif b["broj kolona"] == 6:

                        print(str(redoviiiii[0] + redoviiiii[1] + redoviiiii[2] + redoviiiii[3] + redoviiiii[4] +
                                  redoviiiii[5]) + "   " + \
                              "{:02d}".format(broj_reda))
                        print("")
                        kolone_i_redovi.append([slova])

                        broj_reda = broj_reda + 1

    #ispis_reda = matrica[int(uneti_red)]
    #ispis_kolone = matrica[int(uneta_kolona)]
    file2 = open("karte.txt", "r")

    sadrzaj2 = file2.readlines()

    p = 0

    for linija2 in sadrzaj2:
        reci2 = linija2.split("|")
        sifra_karte = reci2[0]

        p = p + 1

        if sifra_karte == uneta_sifra_karte:

            sadrzaj2[int(uneta_sifra_karte) - 1] = sadrzaj2[int(uneta_sifra_karte) - 1].replace("\n", "")
            sadrzaj2[int(uneta_sifra_karte) - 1] = sadrzaj2[int(uneta_sifra_karte) - 1] + "|" + str(uneti_red) + "." + str(uneta_kolona) + "\n"

    file2.close()

    novi_file = open("karte.txt", "w")

    novi_file.writelines(sadrzaj2)

    novi_file.close()

    for br_kolona in sifra_kolone_redovi:

        if br_kolona["broj kolona"] == 8:

            if br_kolona["sifra karte"] == uneta_sifra_karte:

                file3 = open("zauzeta_sedista_1.txt", "w")

                for reddd in matrica:

                    file3.write(reddd[0] + "," + reddd[1] + "," + reddd[2] + "," + reddd[3] + "," + reddd[4] + "," +
                                reddd[5] + "," + reddd[6] + "," + reddd[7] + '\n')

                file3.close()

        elif br_kolona["broj kolona"] == 9:

            if br_kolona["sifra karte"] == uneta_sifra_karte:

                file8 = open("zauzeta_sedista_2.txt", "w")

                for reddd in matrica:

                    file8.write((reddd[0] + "," + reddd[1] + "," + reddd[2] + "," + reddd[3] + "," + reddd[4] + "," +
                                 reddd[5] + "," + reddd[6] + "," + reddd[7] + "," + reddd[8] + '\n'))

                file8.close()

        elif br_kolona["broj kolona"] == 13:

            if br_kolona["sifra karte"] == uneta_sifra_karte:

                file9 = open("zauzeta_sedista_3.txt", "w")

                for reddd in matrica:

                    file9.write(reddd[0] + "," + reddd[1] + "," + reddd[2] + "," + reddd[3] + "," + reddd[4] + "," +
                                reddd[5] + "," + reddd[6] + "," + reddd[7] + "," + reddd[8] + "," + reddd[9] + "," +
                                reddd[10] + "," + reddd[11] + "," + reddd[12] + '\n')

                file9.close()

        elif br_kolona["broj kolona"] == 6:

            if br_kolona["sifra karte"] == uneta_sifra_karte:

                file10 = open("zauzeta_sedista_4.txt", "w")

                for reddd in matrica:

                    file10.write(reddd[0] + "," + reddd[1] + "," + reddd[2] + "," + reddd[3] + "," + reddd[4] + "," +
                                 reddd[5] + '\n')

                file10.close()
    print("")

    print("\nUspesna prijava na let!")


def nastavak_prijave_na_let():

    print("\nUkoliko zelite da se prijavite za povezane konkretne letove, unesite 1")
    print("Ukoliko zelite da se prijavite za nekog drugog putnika, unesite 2")
    print("Ukoliko zelite da se vratite nazad u meni za kupca, unesite 3")

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2", "3"):
        print("\nNiste uneli odgovarajucu opciju!")
        izbor = input("\nPokusajte ponovo: ")

    if izbor == "1":
        prijava_na_let(TipPrijaveNaLet.POVEZANI_LETOVI.value)
        nastavak_prijave_na_let()

    elif izbor == "2":
        prijava_na_let(TipPrijaveNaLet.SAPUTNIK.value)
        nastavak_prijave_na_let()

    elif izbor == "3":
        pass


def izmena_karte():
    print("Evo odma")


def brisanje_karte():
    karta_za_brisanje = input("\nUnesite sifru karte koju zelite da obrisete: ")

    lista_sifri_karata = []

    for i in podaci_karte:
        lista_sifri_karata.append(i["sifra karte"])

    while karta_za_brisanje not in lista_sifri_karata:
        print("\nOva karta nije prodata. Pokusajte ponovo")
        karta_za_brisanje = input("\nUnesite sifru karte koju zelite da obrisete: ")

    file = open("karte_za_brisanje.txt", "a")
    file.write(karta_za_brisanje+"\n")
    file.close()

def pretraga_prodatih_karata():
    print("Evo odma")

