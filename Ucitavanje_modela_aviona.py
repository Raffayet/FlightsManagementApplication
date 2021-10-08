podaci_modeli_aviona = []

def ucitaj_modele_aviona():

    file = open("modeli_aviona.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        recnik_modeli_aviona = {}
        reci = linija.split("|")
        recnik_modeli_aviona["naziv modela"] = reci[0]
        recnik_modeli_aviona["broj redova"] = reci[1]
        recnik_modeli_aviona["broj sedista u redu"] = reci[2].replace('\n', '')
        podaci_modeli_aviona.append(recnik_modeli_aviona)

ucitaj_modele_aviona()

