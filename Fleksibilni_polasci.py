import datetime
from datetime import timedelta, date
from Ucitavanje_konkretnih_letova import *

trenutni_dan = datetime.datetime.now()

file = open("aerodromi.txt", "r")
sadrzaj = file.readlines()
aerodromi = {}

gradovi = []

for linija in sadrzaj:
    reci = linija.split("|")
    sifra_aerodroma = reci[0]
    naziv_aerodroma = reci[1]
    grad = reci[2]
    drzava = reci[3]
    aerodromi[str(sifra_aerodroma)] = grad
    gradovi.append(grad)
file.close()

file2 = open("konkretni_avionski_letovi.txt")
sadrzaj2 = file2.readlines()

lista_datuma_polaska = []

lista_datuma_dolaska = []

for linija2 in sadrzaj2:
    linija2 = linija2.replace("\n", "")
    reci2 = linija2.split("|")
    datum_polaska = reci2[2]
    datum_dolaska = reci2[3]
    lista_datuma_polaska.append(datum_polaska)
    lista_datuma_dolaska.append(datum_dolaska)
file2.close()


def fleksibilni_polasci():

    ucitaj_konkretne_letove()

    polaziste = input("\nUnesite polaziste: ")
    odrediste = input("\nUnesite odrediste: ")

    while polaziste not in gradovi or odrediste not in gradovi:
        print("\nNema informacija za dato polaziste ili odrediste. Pokusajte ponovo.")
        polaziste = input("\nUnesite polaziste: ")
        odrediste = input("\nUnesite odrediste: ")

    polazisni_datum = input("\nUnesite datum polaska: ")

    while polazisni_datum not in lista_datuma_polaska:
        print("\nNema rezultata za ovaj unos.")
        polazisni_datum = input("\nUnesite datum polaska: ")

    broj_fleksibilnih_dana_polazak = input("\nUnesite broj fleksiblnih dana za polazak: ")

    while int(broj_fleksibilnih_dana_polazak) not in range(16):
        print("\nUneli ste velik broj. Dozvoljeno je do 15.")
        broj_fleksibilnih_dana_polazak = input("\nUnesite broj fleksiblnih dana za polazak: ")

    dolazisni_datum = input("\nUnesite datum dolaska: ")

    while dolazisni_datum not in lista_datuma_dolaska:
        print("\nNema rezultata za ovaj unos.")
        dolazisni_datum = input("\nUnesite datum dolaska: ")

    broj_fleksibilnih_dana_dolazak = input("\nUnesite broj fleksibilnih dana za dolazak: ")

    while int(broj_fleksibilnih_dana_dolazak) not in range(16):
        print("\nUneli ste velik broj. Dozvoljeno je do 15.")
        broj_fleksibilnih_dana_dolazak = input("\nUnesite broj fleksiblnih dana za dolazak: ")

    dann_polazak, mesec_polazak, godina_polazak = datum_polaska[:-1].split(".")

    unesen_datum_polazak = datetime.datetime(int(godina_polazak), int(mesec_polazak), int(dann_polazak))
    prvi_fleksibilni_datum_polazak = unesen_datum_polazak - timedelta(int(broj_fleksibilnih_dana_polazak))
    drugi_fleksibilni_datum_polazak = unesen_datum_polazak + timedelta(int(broj_fleksibilnih_dana_polazak))

    dann_dolazak, mesec_dolazak, godina_dolazak = datum_dolaska[:-1].split(".")

    unesen_datum_dolazak = datetime.datetime(int(godina_dolazak), int(mesec_dolazak), int(dann_dolazak))
    prvi_fleksibilni_datum_dolazak = unesen_datum_dolazak - timedelta(int(broj_fleksibilnih_dana_dolazak))
    drugi_fleksibilni_datum_dolazak = unesen_datum_dolazak + timedelta(int(broj_fleksibilnih_dana_dolazak))

    datumi_polaska = []

    # for i in podaci_konkretni_letovi:
    #     datumi_polaska.append(i["datum polaska"])
    #
    # while int(dann) < 0 or int(dann) > 31:
    #     print("\nIzabrali ste neispravan broj dana. ")
    #     print("Pokusajte ponovo. ")
    #
    #     godina = input("Unesite godinu: ")
    #     mesec = input("Unesite mesec: ")
    #     dann = input("Unesite dan: ")
    #     datum_za_proveravanje = (dann + "." + mesec + "." + godina + ".")
    #
    #     unesen_datum = datetime.datetime(int(godina), int(mesec), int(dann))
    #     prvi_fleksibilni_datum = unesen_datum - timedelta(3)
    #     drugi_fleksibilni_datum = unesen_datum + timedelta(3)
    #
    #
    # while int(mesec) < 0 and int(mesec) > 12:
    #     print("\nIzabrali ste neispravan broj meseci. ")
    #     print("Pokusajte ponovo. ")
    #
    #     godina = input("Unesite godinu: ")
    #     mesec = input("Unesite mesec: ")
    #     dann = input("Unesite dan: ")
    #     datum_za_proveravanje = (dann + "." + mesec + "." + godina + ".")
    #
    #     unesen_datum = datetime.datetime(int(godina), int(mesec), int(dann))
    #     prvi_fleksibilni_datum = unesen_datum - timedelta(3)
    #     drugi_fleksibilni_datum = unesen_datum + timedelta(3)
    #
    # while int(godina) < 0:
    #     print("\nIzabrali ste neispravan broj godina. ")
    #     print("Pokusajte ponovo. ")
    #
    #     godina = input("\nUnesite godinu: ")
    #     mesec = input("Unesite mesec: ")
    #     dann = input("Unesite dan: ")
    #     datum_za_proveravanje = (dann + "." + mesec + "." + godina + ".")
    #
    #     unesen_datum = datetime.datetime(int(godina), int(mesec), int(dann))
    #     prvi_fleksibilni_datum = unesen_datum - timedelta(3)
    #     drugi_fleksibilni_datum = unesen_datum + timedelta(3)
    #
    # while datum_za_proveravanje not in datumi_polaska:
    #     print("\nNema rezultata. ")
    #     print("Pokusajte ponovo. ")
    #
    #     godina = input("\nUnesite godinu: ")
    #     mesec = input("Unesite mesec: ")
    #     dann = input("Unesite dan: ")
    #     datum_za_proveravanje = (dann + "." + mesec + "." + godina + ".")
    #
    #     unesen_datum = datetime.datetime(int(godina), int(mesec), int(dann))
    #     prvi_fleksibilni_datum = unesen_datum - timedelta(3)
    #     drugi_fleksibilni_datum = unesen_datum + timedelta(3)


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

            if broj_konkretnog_leta == broj_leta and dan_leta > trenutni_dan:
                if dan_leta > prvi_fleksibilni_datum_polazak and dan_leta < drugi_fleksibilni_datum_polazak and \
                        polaziste == aerodromi[str(polazisni_aerodrom)]:
                    print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(sifra_konkretnog_leta,
                    aerodromi[str(polazisni_aerodrom)], aerodromi[str(odredisni_aerodrom)], vreme_poletanja,
                    vreme_sletanja, prevoznik, datum_poletanja, model_aviona, cena))
                    print(135 * "_")

                if dan_leta > prvi_fleksibilni_datum_dolazak and dan_leta < drugi_fleksibilni_datum_dolazak and \
                    odrediste == aerodromi[str(odredisni_aerodrom)]:
                    print("{0:^14}{1:^16}{2:^19}{3:^15}{4:^20}{5:^10}{6:^19}{7:^15}{8:^8}".format(sifra_konkretnog_leta,
                                                                                                  aerodromi[str(
                                                                                                      polazisni_aerodrom)],
                                                                                                  aerodromi[str(
                                                                                                      odredisni_aerodrom)],
                                                                                                  vreme_poletanja,
                                                                                                  vreme_sletanja,
                                                                                                  prevoznik,
                                                                                                  datum_poletanja,
                                                                                                  model_aviona, cena))
                    print(135 * "_")


    file1.close()
    file2.close()


# if (dan_leta > trenutni_dan and broj_konkretnog_leta == broj_leta and dan_leta > prvi_fleksibilni_datum_polazak and dan_leta < drugi_fleksibilni_datum_polazak)\
#                     or (dan_leta > prvi_fleksibilni_datum_dolazak and dan_leta < drugi_fleksibilni_datum_dolazak) and polaziste == aerodromi[str(polazisni_aerodrom)] and odrediste == aerodromi[str(odredisni_aerodrom)]: