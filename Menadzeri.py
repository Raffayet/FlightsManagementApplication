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
from Ucitavanje_karata import *
from Ucitavanje_aerodroma import *

lista_brojeva_letova = []

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


def menadzer():
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

            if uloga == "menadzer":

                print("\nUspesno ste se prijavili kao menadzer!")
                recnik_unetih_podataka["uneto korisnicko ime"] = uneto_korisnicko_ime
                recnik_unetih_podataka["uneta lozinka"] = uneta_lozinka
                meni_za_menadzera()
                return

    print("\nUneli ste pogresno korisnicko ime ili lozinku. Pokusajte ponovo.")
    izbor = input("Unesite '1' ako zelite da pokusate opet. Unesite 'b' ako zelite da se vratite nazad u glavni meni. ")

    while izbor not in ("1", "b"):
        print("\nNiste uneli odgovarajucu opciju. Pokusajte ponovo.")
        izbor = input("\nUnesite '1' ako zelite da pokusate opet. Unesite 'b' ako zelite da se vratite nazad: ")

    if izbor == "1":
        menadzer()
    elif izbor == "b":
        return

    file1.close()

def print_meni_za_menadzera():
    print("\nIzaberite jednu od sledecih opcija:\n ")
    print("1 - Pretraga prodatih karata")
    print("2 - Registracija novih prodavaca")
    print("3 - Kreiranje letova")
    print("4 - Izmena letova")
    print("5 - Brisanje karata")
    print("6 - Izvestavanje")
    print("o - Odjava")
    print("e - Izlazak iz aplikacije")

def meni_za_menadzera():
    print_meni_za_menadzera()

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2", "3", "4", "5", "6", "o", "e"):
        print("\nNiste izabrali odgovarajucu opciju!\n")
        print("Pokusajte ponovo. ")
        print_meni_za_menadzera()
        izbor = input("\nUnesite opciju: ")

    if izbor == "1":
        pretraga_prodatih_karata()
        meni_za_menadzera()

    elif izbor == "2":
        registracija_novih_prodavaca()
        meni_za_menadzera()

    elif izbor == "3":
        kreiranje_letova()
        meni_za_menadzera()

    elif izbor == "4":
        izmena_letova()
        meni_za_menadzera()

    elif izbor == "5":
        brisanje_karata()
        meni_za_menadzera()

    elif izbor == "6":
        izvestavanje()
        meni_za_menadzera()

    elif izbor == "o":
        print("\nOdjavili ste se!\n")
        return

    elif izbor == "e":
        pozdrav()

def pretraga_prodatih_karata():
    print("\nDati su sledeci kriterijumi pretrage karata: ")
    print("\n1 - Polaziste")
    print("2 - Odrediste")
    print("3 - Datum polaska")
    print("4 - Datum dolaska")
    print("5 - Putnik")
    print("\n6 - Izlaz")

    kriterijum = input("\nIzaberite kriterijum pretrage: ")

    while kriterijum not in ("1", "2", "3", "4", "5", "6"):
        print("\nNiste uneli odgovarajuci kriterijum. ")

        print("\nDati su sledeci kriterijumi pretrage: ")
        print("\n1 - Polaziste")
        print("2 - Odrediste")
        print("3 - Datum polaska")
        print("4 - Datum dolaska")
        print("5 - Putnik")
        print("\n6 - Izlaz")

        kriterijum = input("\nPokusajte ponovo: ")

    if kriterijum == "1":
        polaziste = input("\nUnesite polaziste: ")

        nadjen = False

        for i in podaci_aerodroma:
            if polaziste == i["grad"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_prodatih_karata()
        else:

            file1 = open("aerodromi.txt")
            file2 = open("avionski_letovi.txt")
            file3 = open("konkretni_avionski_letovi.txt")
            file4 = open("karte.txt")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()
            sadrzaj3 = file3.readlines()
            sadrzaj4 = file4.readlines()

            print(
                "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
                "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                sifra_aerodroma = reci[0]
                grad = reci[2]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    broj_leta = reci[0]
                    sifra_polazista = reci[1]

                    for linija in sadrzaj3:
                        reci = linija.split("|")
                        sifra_konkretnog_leta = reci[0]
                        broj_konkretnog_leta = reci[1]

                        for linija in sadrzaj4:
                            reci = linija.split("|")
                            sifra_karte = reci[0]
                            broj_karte = reci[1]
                            sifra_leta = reci[2]
                            broj_telefona = reci[4]
                            ime = reci[6]
                            prezime = reci[7]
                            broj_pasosa = reci[8]
                            drzavljanstvo = reci[9]
                            pol = reci[10]

                            if polaziste == grad and sifra_aerodroma == sifra_polazista and broj_leta == broj_konkretnog_leta and sifra_konkretnog_leta == sifra_leta:
                                print(
                                    "{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(sifra_karte,
                                    broj_karte, sifra_leta, broj_telefona, ime, prezime, broj_pasosa, drzavljanstvo,
                                    pol))
                                print(135 * "_")

            file1.close()
            file2.close()
            file3.close()
            file4.close()

    if kriterijum == "2":
        odrediste = input("\nUnesite odrediste: ")

        nadjen = False

        for i in podaci_aerodroma:
            if odrediste == i["grad"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_prodatih_karata()
        else:

            file1 = open("aerodromi.txt")
            file2 = open("avionski_letovi.txt")
            file3 = open("konkretni_avionski_letovi.txt")
            file4 = open("karte.txt")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()
            sadrzaj3 = file3.readlines()
            sadrzaj4 = file4.readlines()

            print(
                "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
                "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                sifra_aerodroma = reci[0]
                grad = reci[2]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    broj_leta = reci[0]
                    sifra_odredista = reci[2]

                    for linija in sadrzaj3:
                        reci = linija.split("|")
                        sifra_konkretnog_leta = reci[0]
                        broj_konkretnog_leta = reci[1]

                        for linija in sadrzaj4:
                            reci = linija.split("|")
                            sifra_karte = reci[0]
                            broj_karte = reci[1]
                            sifra_leta = reci[2]
                            broj_telefona = reci[4]
                            ime = reci[6]
                            prezime = reci[7]
                            broj_pasosa = reci[8]
                            drzavljanstvo = reci[9]
                            pol = reci[10]

                            if odrediste == grad and sifra_aerodroma == sifra_odredista and broj_leta == broj_konkretnog_leta and sifra_konkretnog_leta == sifra_leta:
                                print(
                                    "{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(sifra_karte,
                                    broj_karte, sifra_leta, broj_telefona, ime, prezime, broj_pasosa, drzavljanstvo,
                                    pol))
                                print(135 * "_")

            file1.close()
            file2.close()
            file3.close()
            file4.close()

    if kriterijum == "3":
        datum_polaska = input("\nUnesite datum polaska: ")

        nadjen = False

        for i in podaci_konkretni_letovi:
            if datum_polaska == i["datum polaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_prodatih_karata()
        else:

            file3 = open("konkretni_avionski_letovi.txt")
            file4 = open("karte.txt")
            sadrzaj3 = file3.readlines()
            sadrzaj4 = file4.readlines()

            print(
                "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
                "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
            print(135 * "_")

            for linija in sadrzaj3:
                reci = linija.split("|")
                sifra_konkretnog_leta = reci[0]
                broj_konkretnog_leta = reci[1]
                datum_kretanja = reci[2]

                for linija in sadrzaj4:
                    reci = linija.split("|")
                    sifra_karte = reci[0]
                    broj_karte = reci[1]
                    sifra_leta = reci[2]
                    broj_telefona = reci[4]
                    ime = reci[6]
                    prezime = reci[7]
                    broj_pasosa = reci[8]
                    drzavljanstvo = reci[9]
                    pol = reci[10]

                    if datum_polaska == datum_kretanja and sifra_konkretnog_leta == sifra_leta:
                        print("{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(sifra_karte,
                        broj_karte, sifra_leta, broj_telefona, ime, prezime, broj_pasosa, drzavljanstvo, pol))
                        print(135 * "_")

            file3.close()
            file4.close()

    if kriterijum == "4":
        datum_dolaska = input("\nUnesite datum dolaska: ")

        nadjen = False

        for i in podaci_konkretni_letovi:
            if datum_dolaska == i["datum dolaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_prodatih_karata()
        else:

            file3 = open("konkretni_avionski_letovi.txt")
            file4 = open("karte.txt")
            sadrzaj3 = file3.readlines()
            sadrzaj4 = file4.readlines()

            print(
                "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
                "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
            print(135 * "_")

            for linija in sadrzaj3:
                reci = linija.split("|")
                sifra_konkretnog_leta = reci[0]
                broj_konkretnog_leta = reci[1]
                datum_kretanja = reci[2]
                datum_sletanja = reci[3].replace('\n', '')

                for linija in sadrzaj4:
                    reci = linija.split("|")
                    sifra_karte = reci[0]
                    broj_karte = reci[1]
                    sifra_leta = reci[2]
                    broj_telefona = reci[4]
                    ime = reci[6]
                    prezime = reci[7]
                    broj_pasosa = reci[8]
                    drzavljanstvo = reci[9]
                    pol = reci[10]

                    if datum_dolaska == datum_sletanja and sifra_konkretnog_leta == sifra_leta:
                        print("{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(sifra_karte,
                        broj_karte, sifra_leta, broj_telefona, ime, prezime, broj_pasosa, drzavljanstvo, pol))
                        print(135 * "_")

            file3.close()
            file4.close()

    if kriterijum == "5":
        putnik = input("\nUnesite ime i prezime putnika: ")

        nadjen = False

        for i in podaci_karte:
            if putnik == i["ime"] + " " + i["prezime"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_prodatih_karata()
        else:

            file4 = open("karte.txt")
            sadrzaj4 = file4.readlines()

            print(
                "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
                "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
            print(135 * "_")

            for linija in sadrzaj4:
                reci = linija.split("|")
                sifra_karte = reci[0]
                broj_karte = reci[1]
                sifra_leta = reci[2]
                broj_telefona = reci[4]
                ime = reci[6]
                prezime = reci[7]
                broj_pasosa = reci[8]
                drzavljanstvo = reci[9]
                pol = reci[10]

                if putnik == ime + " " + prezime:
                    print("{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(sifra_karte,
                    broj_karte, sifra_leta, broj_telefona, ime, prezime, broj_pasosa, drzavljanstvo, pol))
                    print(135 * "_")

            file4.close()

    if kriterijum == "6":
        return

def registracija_novih_prodavaca():
    print("\nKako biste registrovali prodavca, unesite sledece podatke: ")

    novo_korisnicko_ime = input("\nKorisnicko ime: ")
    nova_lozinka = input("Lozinka: ")
    novo_ime = input("Ime: ")
    novo_prezime = input("Prezime: ")

    file = open("korisnici.txt", "a")

    while novo_korisnicko_ime == "" or nova_lozinka == "" or novo_ime == "" or novo_prezime == "":
        print("Niste uneli sve neophodne podatke. Pokusajte ponovo.")

        novo_korisnicko_ime = input("\nKorisnicko ime: ")
        nova_lozinka = input("Lozinka: ")
        novo_ime = input("Ime: ")
        novo_prezime = input("Prezime: ")

    file.write(
        novo_korisnicko_ime + "|" + nova_lozinka + "|" + novo_ime + "|" + novo_prezime + "|" + "prodavac" + "\n")

    file.close()

def kreiranje_letova():
    broj_novog_leta = input("\nUnesite broj novog leta: ")

    for x in podaci_avionski_letovi:
        lista_brojeva_letova.append(x["broj leta"])

    while broj_novog_leta in lista_brojeva_letova:
        print("\nOva sifra leta vec postoji! Ona mora biti jedinstvena. Pokusajte ponovo.")
        broj_novog_leta = input("\nUnesite broj novog leta: ")

    for i in broj_novog_leta:

        if len(broj_novog_leta) != 4:
            print("\nNiste uneli odgovarajuc format broja leta. Format treba da bude SLOVO-SLOVO-broj-broj. Pokusajte ponovo.")
            broj_novog_leta = input("\nUnesite broj novog leta: ")

        while broj_novog_leta[0] not in "QWERTYUIOPASDFGHJKLZXCVBNM" or broj_novog_leta[1] not in "QWERTYUIOPASDFGHJKLZXCVBNM" or broj_novog_leta[2] not in "0123456789" or broj_novog_leta[3] not in "0123456789":
            print("\nNiste uneli odgovarajuc format broja leta. Format treba da bude SLOVO-SLOVO-broj-broj. Pokusajte ponovo.")
            broj_novog_leta = input("\nUnesite broj novog aerodroma: ")

    polazisni_aerodrom_novog_leta = input("Unesite polazisni aerodrom novog leta: ")

    lista_aerodroma = []

    for j in podaci_aerodroma:
        lista_aerodroma.append(j["sifra"])

    while polazisni_aerodrom_novog_leta not in lista_aerodroma:
        print("\nOvaj aerodrom ne postoji u nasoj bazi podataka. Pokusajte ponovo.")
        polazisni_aerodrom_novog_leta = input("\nUnesite polazisni aerodrom novog leta: ")

    odredisni_aerodrom_novog_leta = input("Unesite odredisni aerodrom novog leta: ")

    while odredisni_aerodrom_novog_leta not in lista_aerodroma:
        print("\nOvaj aerodrom ne postoji u nasoj bazi podataka. Pokusajte ponovo.")
        odredisni_aerodrom_novog_leta = input("Unesite odredisni aerodrom novog leta: ")

    vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
    vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

    while not vreme_poletanja_sati.isdigit() or not vreme_poletanja_minuti.isdigit():
        print("\nNiste uneli odgovarajuc format vremena poletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
        vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
        vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

    while int(vreme_poletanja_sati) not in range(0, 24) or int(vreme_poletanja_minuti) not in range(0, 60):
        print("\nNiste uneli odgovarajuc format vremena poletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
        vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
        vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

    vreme_poletanja = "{:02d}".format(int(vreme_poletanja_sati)) + ":" + "{:02}".format(int(vreme_poletanja_minuti))

    vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
    vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

    while not vreme_sletanja_sati.isdigit() or not vreme_sletanja_minuti.isdigit():
        print(
            "\nNiste uneli odgovarajuc format vremena sletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
        vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
        vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

    while int(vreme_sletanja_sati) not in range(0, 24) or int(vreme_sletanja_minuti) not in range(0, 60):
        print(
            "\nNiste uneli odgovarajuc format vremena sletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
        vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
        vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

    vreme_sletanja = "{:02d}".format(int(vreme_sletanja_sati)) + ":" + "{:02}".format(int(vreme_sletanja_minuti))

    sletanje_sledeceg_dana = input("Sletanje sledeceg dana? (da, ne)")

    while sletanje_sledeceg_dana not in ("da", "ne"):
        print("\nNiste uneli dobar odgovor! Unesite da ili ne. ")
        sletanje_sledeceg_dana = input("Sletanje sledeceg dana? (da, ne)")

    prevoznik = input("Unesite prevoznika: ")

    lista_prevoznika = []

    for k in podaci_avionski_letovi:
        lista_prevoznika.append(k["prevoznik"])

    while prevoznik not in lista_prevoznika:
        print("Trenutno nemamo na raspolaganju datog prevoznika. Izaberite jednog od postojecih.")
        prevoznik = input("Unesite prevoznika: ")

    dani = input("Unesite dane u kojima se bi se obavljao dati let: ")

    while "ponedeljak" not in dani and "utorak" not in dani and "sreda" not in dani and "cetvrtak" not in dani and "petak" not in dani and "subota" not in dani and "nedelja" not in dani:
        print("\nNeispravan dan!")
        dani = input("Unesite dane u kojima se bi se obavljao dati let: ")

    model_aviona = input("Unesite model aviona: ")

    lista_modela_aviona = []

    for m in podaci_modeli_aviona:
        lista_modela_aviona.append(m["naziv modela"])

    while model_aviona not in lista_modela_aviona:
        print("Nemamo dati model. Uzmite jedan od postojecih.")
        print(lista_modela_aviona)
        model_aviona = input("Unesite model aviona: ")

    cena = input("Postavite cenu leta: ")

    while not cena.isdigit():
        print("Unesite cifru za cenu.")
        cena = input("Postavite cenu leta: ")


    file = open("avionski_letovi.txt", "a")

    file.write(broj_novog_leta+"|"+polazisni_aerodrom_novog_leta+"|"+odredisni_aerodrom_novog_leta+"|"+vreme_poletanja
               +"|"+vreme_sletanja+"|"+sletanje_sledeceg_dana+"|"+prevoznik+"|"+dani+"|"+model_aviona+"|"+cena+"\n")

    file.close()


def izmena_letova():

    broj_leta = input("\nUnesite broj leta za koji hocete da izvrsite promene: ")

    for x in podaci_avionski_letovi:
        lista_brojeva_letova.append(x["broj leta"])

    while broj_leta not in lista_brojeva_letova:
        print("\nOvaj broj leta ne postoji. Unesite jedan od postojecih.")
        print(lista_brojeva_letova)
        broj_leta = input("\nUnesite broj leta za koji hocete da izvrsite promene: ")

    file = open("avionski_letovi.txt", "r+")
    sadrzaj = file.readlines()

    brojac = 0

    for linija in sadrzaj:
        reci = linija.split("|")
        if reci[0] == broj_leta:

            print("\nUkoliko zelite da promenite sledece podatke, unesite da. U suprotnom, unesite ne.")
            izbor = input("\nBroj leta?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nBroj leta?")

            if izbor == "da":

                broj_novog_leta = input("\nUnesite broj novog leta: ")

                for x in podaci_avionski_letovi:
                    lista_brojeva_letova.append(x["broj leta"])

                while broj_novog_leta in lista_brojeva_letova:
                    print("\nOva sifra leta vec postoji! Ona mora biti jedinstvena. Pokusajte ponovo.")
                    broj_novog_leta = input("\nUnesite broj novog leta: ")

                for i in broj_novog_leta:

                    if len(broj_novog_leta) != 4:
                        print(
                            "\nNiste uneli odgovarajuc format broja leta. Format treba da bude SLOVO-SLOVO-broj-broj. Pokusajte ponovo.")
                        broj_novog_leta = input("\nUnesite broj novog leta: ")

                    while broj_novog_leta[0] not in "QWERTYUIOPASDFGHJKLZXCVBNM" or broj_novog_leta[
                        1] not in "QWERTYUIOPASDFGHJKLZXCVBNM" or broj_novog_leta[2] not in "0123456789" or broj_novog_leta[
                        3] not in "0123456789":
                        print(
                            "\nNiste uneli odgovarajuc format broja leta. Format treba da bude SLOVO-SLOVO-broj-broj. Pokusajte ponovo.")
                        broj_novog_leta = input("\nUnesite broj novog aerodroma: ")

                linija = linija.replace(reci[0], broj_novog_leta)
                sadrzaj[brojac] = linija

            elif izbor == "ne":
                broj_novog_leta = reci[0]

            izbor = input("\nPolazisni aerodrom?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nPolazisni aerodrom?")

            if izbor == "da":

                polazisni_aerodrom_novog_leta = input("Unesite polazisni aerodrom novog leta: ")

                lista_aerodroma = []

                for j in podaci_aerodroma:
                    lista_aerodroma.append(j["sifra"])

                while polazisni_aerodrom_novog_leta not in lista_aerodroma:
                    print("\nOvaj aerodrom ne postoji u nasoj bazi podataka. Pokusajte ponovo.")
                    polazisni_aerodrom_novog_leta = input("\nUnesite polazisni aerodrom novog leta: ")

                linija = linija.replace(reci[1], polazisni_aerodrom_novog_leta)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                polazisni_aerodrom_novog_leta = reci[1]

            izbor = input("\nOdredisni aerodrom?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nOdredisni aerodrom?")

            if izbor == "da":

                odredisni_aerodrom_novog_leta = input("Unesite odredisni aerodrom novog leta: ")

                lista_aerodroma = []

                for l in podaci_aerodroma:
                    lista_aerodroma.append(l["sifra"])

                while odredisni_aerodrom_novog_leta not in lista_aerodroma:
                    print("\nOvaj aerodrom ne postoji u nasoj bazi podataka. Pokusajte ponovo.")
                    odredisni_aerodrom_novog_leta = input("Unesite odredisni aerodrom novog leta: ")

                linija = linija.replace(reci[2], odredisni_aerodrom_novog_leta)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                odredisni_aerodrom_novog_leta = reci[2]

            izbor = input("\nVreme polaska?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nVreme polaska?")

            if izbor == "da":

                vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
                vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

                while not vreme_poletanja_sati.isdigit() or not vreme_poletanja_minuti.isdigit():
                    print(
                        "\nNiste uneli odgovarajuc format vremena poletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
                    vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
                    vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

                while int(vreme_poletanja_sati) not in range(0, 24) or int(vreme_poletanja_minuti) not in range(0, 60):
                    print(
                        "\nNiste uneli odgovarajuc format vremena poletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
                    vreme_poletanja_sati = input("Unesite vreme poletanja u satima: ")
                    vreme_poletanja_minuti = input("Unesite vreme poletanja u minutima: ")

                vreme_poletanja = "{:02d}".format(int(vreme_poletanja_sati)) + ":" + "{:02}".format(
                    int(vreme_poletanja_minuti))

                linija = linija.replace(reci[3], vreme_poletanja)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                vreme_poletanja = reci[3]

            izbor = input("\nVreme dolaska?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nVreme dolaska?")

            if izbor == "da":

                vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
                vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

                while not vreme_sletanja_sati.isdigit() or not vreme_sletanja_minuti.isdigit():
                    print(
                        "\nNiste uneli odgovarajuc format vremena sletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
                    vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
                    vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

                while int(vreme_sletanja_sati) not in range(0, 24) or int(vreme_sletanja_minuti) not in range(0, 60):
                    print(
                        "\nNiste uneli odgovarajuc format vremena sletanja. Format treba da bude sati1-sati2-:minuti1-minuti2. Pokusajte ponovo.")
                    vreme_sletanja_sati = input("Unesite vreme sletanja u satima: ")
                    vreme_sletanja_minuti = input("Unesite vreme sletanja u minutima: ")

                vreme_sletanja = "{:02d}".format(int(vreme_sletanja_sati)) + ":" + "{:02}".format(
                    int(vreme_sletanja_minuti))

                linija = linija.replace(reci[4], vreme_sletanja)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                vreme_sletanja = reci[4]

            izbor = input("\nSletanje sledeceg dana?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nSletanje sledeceg dana?")

            if izbor == "da":

                sletanje_sledeceg_dana = input("Sletanje sledeceg dana? (da, ne)")

                while sletanje_sledeceg_dana not in ("da", "ne"):
                    print("\nNiste uneli dobar odgovor! Unesite da ili ne. ")
                    sletanje_sledeceg_dana = input("Sletanje sledeceg dana? (da, ne)")

                linija = linija.replace(reci[5], sletanje_sledeceg_dana)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                sletanje_sledeceg_dana = reci[5]

            izbor = input("\nPrevoznik?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nPrevoznik?")

            if izbor == "da":

                prevoznik = input("Unesite prevoznika: ")

                lista_prevoznika = []

                for k in podaci_avionski_letovi:
                    lista_prevoznika.append(k["prevoznik"])

                while prevoznik not in lista_prevoznika:
                    print("Trenutno nemamo na raspolaganju datog prevoznika. Izaberite jednog od postojecih.")
                    prevoznik = input("Unesite prevoznika: ")

                linija = linija.replace(reci[6], prevoznik)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                prevoznik = reci[6]

            izbor = input("\nDani u kojima se izvrsava let?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nDani u kojima se izvrsava let?")

            if izbor == "da":

                dani = input("Unesite dane u kojima se bi se obavljao dati let: ")

                while "ponedeljak" not in dani and "utorak" not in dani and "sreda" not in dani and "cetvrtak" not in dani and "petak" not in dani and "subota" not in dani and "nedelja" not in dani:
                    print("\nNeispravan dan!")
                    dani = input("Unesite dane u kojima se bi se obavljao dati let: ")

                linija = linija.replace(reci[7], dani)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                dani = reci[7]

            izbor = input("\nModel aviona?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nModel aviona?")

            if izbor == "da":

                model_aviona = input("Unesite model aviona: ")

                lista_modela_aviona = []

                for m in podaci_modeli_aviona:
                    lista_modela_aviona.append(m["naziv modela"])

                while model_aviona not in lista_modela_aviona:
                    print("Nemamo dati model. Uzmite jedan od postojecih.")
                    print(lista_modela_aviona)
                    model_aviona = input("Unesite model aviona: ")

                linija = linija.replace(reci[8], model_aviona)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                model_aviona = reci[8]

            izbor = input("\nCena leta?")

            while izbor not in ("da", "ne"):
                print("\nNiste izabrali odgovarajucu opciju! Pokusajte ponovo.")
                izbor = input("\nCena leta?")

            if izbor == "da":

                cena = input("Postavite cenu leta: ")

                while not cena.isdigit():
                    print("Unesite cifru za cenu.")
                    cena = input("Postavite cenu leta: ")

                linija = linija.replace(reci[9].replace('\n', ''), cena)
                sadrzaj[brojac] = linija

            elif izbor == "ne":

                cena = reci[9].replace('\n', '')

        brojac = brojac + 1
    file.close()

    file2 = open("avionski_letovi.txt", "w")
    file2.writelines(sadrzaj)

def brisanje_karata():

    karte_za_brisanje = []

    print("\nKarte za brisanje oznacene od strane prodavca su sledece: ")

    file = open("karte_za_brisanje.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    print(
        "| SIFRA KARTE | BROJ KARTE | SIFRA LETA | BROJ TELEFONA |    IME    | "
        "  PREZIME   | BROJ PASOSA | DRZAVLJANSTVO | POL |")
    print(135 * "_")

    for karta in sadrzaj:
        karta = karta.replace('\n', '')

        for j in podaci_karte:

            if karta == j["sifra karte"]:

                print("{0:^14}{1:^13}{2:^15}{3:^11}{4:^18}{5:^6}{6:^21}{7:^10}{8:^12}".format(j["sifra karte"],
                j["redni broj kupovine"], j["sifra leta"], j["broj telefona"], j["ime"], j["prezime"], j["broj pasosa"]
                , j["drzavljanstvo"], j["pol"]))

    print("\nAko zelite da obrisete sve karte, unesite 1.")
    print("Ako zelite da obrisete jednu ili vise karata, unesite 2.")
    print("Ako zelite da ponistite brisanje karata od odavde navedenih, unesite 3.")

    izbor = input("\nUnesite opciju: ")

    while izbor not in ("1", "2", "3"):
        print("\nNiste uneli odgovarajucu opciju! Pokusajte ponovo.")
        izbor = input("\nUnesite opciju: ")

    if izbor == "1":
        file2 = open("karte.txt", "r+")
        sadrzaj2 = file2.readlines()

        for karta in sadrzaj:
            karta = karta.replace('\n', '')

            for linija2 in sadrzaj2:
                if linija2.startswith(karta):
                    sadrzaj2.remove(linija2)
        file2.close()
        file3 = open("karte.txt", "w")
        file3.writelines(sadrzaj2)
        file3.close()
        file4 = open("karte_za_brisanje.txt", "r+")
        sadrzaj4 = file4.readlines()
        for linija4 in sadrzaj4:
            sadrzaj4.remove(linija4)
        file4.close()
        file5 = open("karte_za_brisanje.txt", "w")
        file5.writelines(sadrzaj4)
        file5.close()

    elif izbor == "2":
        specificna_karta = input("Unesite sifru karte koju zelite da obrisete: ")

        for linija in sadrzaj:
            linija = linija.replace('\n', '')
            karte_za_brisanje.append(linija)

        while specificna_karta not in karte_za_brisanje:
            print("\nOva karta nije postavljena za brisanje od strane prodavca. Pokusajte ponovo")
            specificna_karta = input("\nUnesite sifru karte koju zelite da obrisete: ")

        file6 = open("karte.txt", "r+")
        sadrzaj6 = file6.readlines()
        file6.close()

        for linija6 in sadrzaj6:
            if linija6.startswith(specificna_karta):
                sadrzaj6.remove(linija6)
        file7 = open("karte.txt", "w")
        file7.writelines(sadrzaj6)
        file7.close()

        file8 = open("karte_za_brisanje.txt", "r+")
        sadrzaj8 = file8.readlines()
        file8.close()

        for linija8 in sadrzaj8:
            if linija8.startswith(specificna_karta):
                sadrzaj8.remove(linija8)
        file9 = open("karte_za_brisanje.txt", "w")
        file9.writelines(sadrzaj8)
        file9.close()

    elif izbor == "3":
        specificna_karta_za_ponistavanje = input("\nUnesite sifru karte koju zelite da ponistite: ")

        for linija in sadrzaj:
            linija = linija.replace('\n', '')
            karte_za_brisanje.append(linija)

        while specificna_karta_za_ponistavanje not in karte_za_brisanje:
            print("\nOva karta ni ne postoji u listi za brisanje! Pokusajte ponovo.")
            specificna_karta_za_ponistavanje = input("\nUnesite sifru karte koju zelite da ponistite: ")

        file10 = open("karte_za_brisanje.txt", "r+")
        sadrzaj10 = file10.readlines()

        for linija10 in sadrzaj10:
            if linija10.startswith(specificna_karta_za_ponistavanje):
                sadrzaj10.remove(linija10)
        file10.close()
        file11 = open("karte_za_brisanje.txt", "w")
        file11.writelines(sadrzaj10)
        file11.close()


def izvestavanje():
    print("Evo odma")