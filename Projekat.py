from Login import login
from Pregled_nl import pregled_nl
from Pretraga_letova import pretraga_letova
from Prikaz_10 import prikaz_10_najjeftinijih
from Fleksibilni_polasci import fleksibilni_polasci
from Pozdrav import pozdrav
from Visekriterijumska_pretraga import *
from Ucitavanje_karata import *
from Ucitavanje_vremena_polaska import *
from Ucitavanje_modela_aviona import *
from Ucitavanje_letova import *
from Ucitavanje_konkretnih_letova import *
from Ucitavanje_korisnika import *
from Ucitavanje_aerodroma import *
from Ucitavanje_vremena_dolaska import *

#Pokretanjem ovog fajla se pokrece ceo program


def main():

    dobrodoslica()
    pocetni_meni()
    opcija1 = unos_opcije()

    while opcija1 != "e":

        if opcija1 == "1":
            login()
            meni_za_nastavak()

        elif opcija1 == "2":
            pregled_nl()
            meni_za_nastavak()

        elif opcija1 == "3":
            pretraga_letova()
            meni_za_nastavak()

        elif opcija1 == "4":
            visekriterijumska_pretraga_pocetak()
            visekriterijumska_pretraga_kraj()
            meni_za_nastavak()

        elif opcija1 == "5":
            prikaz_10_najjeftinijih()
            meni_za_nastavak()

        elif opcija1 == "6":
            fleksibilni_polasci()
            meni_za_nastavak()

    pozdrav()


def dobrodoslica():
    print("-------------------------")
    print("{0:^25}".format("PRODAJA AVIONSKIH KARATA"))
    print("-------------------------")
    print("{0:^25}" .format("DOBRODOSLI!"))
    print("-------------------------")


def pocetni_meni():
    print("Molimo Vas da unesete jednu od sledecih opcija:")
    print("Ukoliko zelite da izadjete iz aplikacije, unesite \"e\"\n")
    print("1 - Prijava na sistem")
    print("2 - Pregled nerealizovanih letova")
    print("3 - Pretraga letova")
    print("4 - Visekriterijumska pretraga letova")
    print("5 - Prikaz 10 najjeftinijih letova")
    print("6 - Fleksibilni polasci")
    print("e - Izlazak iz aplikacije")


def unos_opcije():
    opcija1 = input("\nUnesite opciju: ")
    while opcija1 not in ("1", "2", "3", "4", "5", "6", "e"):
        print("\nUneli ste neodgovarajucu opciju!\n")
        pocetni_meni()
        opcija1 = input("\nPokusajte ponovo: ")
    return opcija1


def meni_za_nastavak():
    print("------------")
    print("GLAVNI MENI")
    print("------------")
    pocetni_meni()
    opcija1 = unos_opcije()

    while opcija1 != "e":

        if opcija1 == "1":
            login()
            meni_za_nastavak()

        elif opcija1 == "2":
            pregled_nl()
            meni_za_nastavak()

        elif opcija1 == "3":
            pretraga_letova()
            meni_za_nastavak()

        elif opcija1 == "4":
            visekriterijumska_pretraga_pocetak()
            visekriterijumska_pretraga_kraj()
            meni_za_nastavak()

        elif opcija1 == "5":
            prikaz_10_najjeftinijih()
            meni_za_nastavak()

        elif opcija1 == "6":
            fleksibilni_polasci()
            meni_za_nastavak()

    pozdrav()


if __name__ == "__main__":
    main()