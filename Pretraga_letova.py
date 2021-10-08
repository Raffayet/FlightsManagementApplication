from Ucitavanje_aerodroma import *
from Ucitavanje_konkretnih_letova import *
from Ucitavanje_letova import *
import datetime

trenutni_dan = datetime.datetime.now()

file = open("aerodromi.txt", "r")
sadrzaj = file.readlines()
aerodromi = {}

for linija in sadrzaj:
    reci = linija.split("|")
    sifra_aerodroma = reci[0]
    naziv_aerodroma = reci[1]
    grad = reci[2]
    drzava = reci[3]
    aerodromi[str(sifra_aerodroma)] = grad
file.close()

def pretraga_letova():

    ucitaj_aerodrome()
    ucitaj_avionske_letove()
    ucitaj_konkretne_letove()

    print("\nDati su sledeci kriterijumi pretrage: ")
    print("\n1 - Polaziste")
    print("2 - Odrediste")
    print("3 - Datum polaska")
    print("4 - Datum dolaska")
    print("5 - Vreme poletanja")
    print("6 - Vreme sletanja")
    print("7 - Prevoznik")
    print("\n8 - Izlaz")
    kriterijum = input("\nIzaberite kriterijum pretrage: ")

    while kriterijum not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        print("\nNiste uneli odgovarajuci kriterijum. ")

        print("\nDati su sledeci kriterijumi pretrage: ")
        print("\n1 - Polaziste")
        print("2 - Odrediste")
        print("3 - Datum polaska")
        print("4 - Datum dolaska")
        print("5 - Vreme poletanja")
        print("6 - Vreme sletanja")
        print("7 - Prevoznik")
        print("\n8 - Izlaz")

        kriterijum = input("\nPokusajte ponovo: ")

    if kriterijum == "1":
        polaziste = input("\nUnesite polaziste: ")

        nadjen = False

        for i in podaci_aerodroma:
            if polaziste == i["grad"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()
        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3]
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(polaziste) == aerodromi[polazisni_aerodrom]:

                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(sifra_konkretnog_leta,
                        aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                        vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "2":
        odrediste = input("\nUnesite odrediste: ")

        nadjen = False

        for i in podaci_aerodroma:
            if odrediste == i["grad"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3]
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(odrediste) == aerodromi[
                        odredisni_aerodrom]:
                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "3":
        datum_polaska = input("\nUnesite datum polaska: ")

        nadjen = False

        for i in podaci_konkretni_letovi:
            if datum_polaska == i["datum polaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3]
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(datum_polaska) == datum_poletanja:

                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "4":
        datum_dolaska = input("\nUnesite datum dolaska: ")

        nadjen = False

        for i in podaci_konkretni_letovi:
            if datum_dolaska == i["datum dolaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3].replace('\n', '')
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(datum_dolaska) == datum_sletanja:

                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()



    if kriterijum == "5":
        vreme_polaska = input("\nUnesite vreme polaska: ")

        nadjen = False

        for i in podaci_avionski_letovi:
            if vreme_polaska == i["vreme polaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    linija.replace('\n', '')
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3].replace('\n', '')
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(
                            vreme_polaska) == vreme_poletanja:
                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "6":
        vreme_dolaska = input("\nUnesite vreme dolaska: ")

        nadjen = False

        for i in podaci_avionski_letovi:

            if vreme_dolaska == i["vreme dolaska"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    linija.replace('\n', '')
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3].replace('\n', '')
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(
                            vreme_dolaska) == vreme_sletanja:
                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "7":
        prevozznik = input("\nUnesite prevoznika: ")

        nadjen = False

        for i in podaci_avionski_letovi:

            if prevozznik == i["prevoznik"]:
                nadjen = True

        if not nadjen:
            print("\nNema rezultata. \n")
            pretraga_letova()

        else:

            file1 = open("avionski_letovi.txt", "r")
            file2 = open("konkretni_avionski_letovi.txt", "r")
            sadrzaj1 = file1.readlines()
            sadrzaj2 = file2.readlines()

            print(
                "| SIFRA LETA | POLAZISNI GRAD | ODREDISNI GRAD | VREME POLETANJA | VREME SLETANJA | "
                "PREVOZNIK | DATUM POLETANJA | MODEL AVIONA | CENA |")
            print(135 * "_")

            for linija in sadrzaj1:
                reci = linija.split("|")
                broj_leta = reci[0]
                polazisni_aerodrom = reci[1]
                odredisni_aerodrom = reci[2]
                vreme_poletanja = reci[3]
                vreme_sletanja = reci[4]
                sletanje_sledeceg_dana = reci[5]
                prevoznik = reci[6]
                dani = reci[7]
                model_aviona = reci[8]
                cena = reci[9]

                for linija in sadrzaj2:
                    linija.replace('\n', '')
                    reci = linija.split("|")
                    sifra_konkretnog_leta = reci[0]
                    broj_konkretnog_leta = reci[1]
                    datum_poletanja = reci[2]
                    datum_sletanja = reci[3].replace('\n', '')
                    broj = datum_poletanja.split(".")
                    dan = broj[0]
                    mesec = broj[1]
                    godina = broj[2]
                    dan_leta = datetime.datetime(int(godina), int(mesec), int(dan))

                    if dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and str(
                            prevozznik) == prevoznik:
                        print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(
                            sifra_konkretnog_leta,
                            aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                            vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                        print(135 * "_")

            file1.close()
            file2.close()

    if kriterijum == "8":
        return
