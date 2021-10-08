from Kupci import kupac
from Prodavci import prodavac
from Menadzeri import menadzer
from Pozdrav import pozdrav

def login():
    opcija2 = meni()

    while opcija2 != "e":

        if opcija2 == "1":
           kupac()
           login()
           return

        elif opcija2 == "2":
            prodavac()
            login()
            return

        elif opcija2 == "3":
            menadzer()
            login()
            return

        elif opcija2 == "r":
            registrovanje_kupca()
            meni_posle_registracije()
            kupac()
            login()

        elif opcija2 == "b":
            return

    pozdrav()

def login_meni():
    print("\nMolimo Vas da unesete jednu od sledecih opcija:\n")
    print("1 - Ako zelite da se ulogujete kao kupac")
    print("2 - Ako zelite da se ulogujete kao prodavac")
    print("3 - Ako zelite da se ulogujete kao menadzer")
    print("r - Ako niste napravili nalog. Na ovaj nacin cete se registrovati")
    print("b - Ako zelite da se vratite nazad")
    print("e - Ako zelite da izadjete iz aplikacije")


def meni():
    login_meni()
    opcija2 = input("\nUnesite opciju: ")
    while opcija2 not in ("1", "2", "3", "r", "b", "e"):
        print("\nUneli ste neodgovarajucu opciju!\n")
        login_meni()
        opcija2 = input("\nPokusajte ponovo: ")
    return opcija2


def meni_za_registrovanje():

    opcija2 = input("Unesite opciju: ")
    while opcija2 not in ("r"):
        print("\nUneli ste neodgovarajucu opciju!")
        print("\nUkoliko ste se vec registrovali, unesite opciju 1")
        print("Ukoliko ste nov korisnik, unesite opciju 2")
        opcija2 = input("\nPokusajte ponovo: ")
    return opcija2


def podaci_korisnika():
    file = open("korisnici.txt", "r")
    sadrzaj = file.readlines()

    for linija in sadrzaj:
        reci = linija.split("|")
        korisnicko_ime = reci[0]
        lozinka = reci[1]
        ime = reci[2]
        prezime = reci[3]
        uloga = reci[4].replace('\n', '')
    file.close()


def registrovanje_kupca():
    print("\nKako biste se registrovali, unesite sledece podatke: ")
    print("Podatke kao sto su broj pasosa, drzavljanstvo i pol, ukoliko ne zelite, ne morate unositi.\n")

    novo_korisnicko_ime = input("Korisnicko ime: ")
    nova_lozinka = input("Lozinka: ")
    novo_ime = input("Ime: ")
    novo_prezime = input("Prezime: ")
    novi_broj_pasosa = input("Broj pasosa: ")
    novo_drzavljanstvo = input("Drzavljanstvo: ")
    novi_telefon = input("Kontakt telefon: ")
    novi_email = input("Email adresa: ")
    novi_pol = input("Pol: ")

    file = open("korisnici.txt", "a")

    while novo_korisnicko_ime == "" or nova_lozinka == "" or novo_ime == "" or novo_prezime == ""\
            or novi_telefon == "" or novi_email == "":
        print("Niste uneli sve neophodne podatke. Pokusajte ponovo.")

        novo_korisnicko_ime = input("\nKorisnicko ime: ")
        nova_lozinka = input("Lozinka: ")
        novo_ime = input("Ime: ")
        novo_prezime = input("Prezime: ")
        novi_broj_pasosa = input("Broj pasosa: ")
        novo_drzavljanstvo = input("Drzavljanstvo: ")
        novi_telefon = input("Kontakt telefon: ")
        novi_email = input("Email adresa: ")
        novi_pol = input("Pol: ")

    if novi_broj_pasosa == "":
        file.write(
            novo_korisnicko_ime+"|"+nova_lozinka+"|"+novo_ime+"|"+novo_prezime+"|"+"kupac"+"|"+"nije navedeno"+
            "|"+novo_drzavljanstvo+"|"+novi_telefon+"|"+novi_email+"|"+novi_pol+"\n")


    if novo_drzavljanstvo == "":
        file.write(
            novo_korisnicko_ime+"|"+nova_lozinka+"|"+novo_ime+"|"+novo_prezime+"|"+"kupac"+"|"+novi_broj_pasosa+
            "|"+"nije navedeno"+"|"+novi_telefon+"|"+novi_email+"|"+novi_pol+"\n")


    if novi_pol == "":
        file.write(
            novo_korisnicko_ime+"|"+nova_lozinka+"|"+novo_ime+"|"+novo_prezime+"|"+"kupac"+"|"+novi_broj_pasosa+
            "|"+novo_drzavljanstvo+"|"+novi_telefon+"|"+novi_email+"|"+"nije navedeno"+"\n")

    else:
        file.write(novo_korisnicko_ime+"|"+nova_lozinka+"|"+novo_ime+"|"+novo_prezime+"|"+"kupac"+"|"+novi_broj_pasosa
               +"|"+novo_drzavljanstvo+"|"+novi_telefon+"|"+novi_email+"|"+novi_pol+"\n")

    file.close()

def print_meni_posle_registracije():

    print("\nMolimo Vas da unesete jednu od sledecih opcija:\n")
    print("1 - Ako zelite da se ulogujete kao kupac")
    print("e - Ako zelite da izadjete iz aplikacije")

def meni_posle_registracije():

    print_meni_posle_registracije()

    opcija = input("\nUnesite opciju: ")
    while opcija not in ("1", "e"):
        print("\nUneli ste neodgovarajucu opciju!\n")
        login_meni()
        opcija = input("\nPokusajte ponovo: ")

    if opcija == "1":
        kupac()

    if opcija == "e":
        pozdrav()