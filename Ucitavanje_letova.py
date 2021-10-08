podaci_avionski_letovi = []

def ucitaj_avionske_letove():

    file = open("avionski_letovi.txt", "r")
    sadrzaj = file.readlines()
    file.close()

    for linija in sadrzaj:
        recnik_avionski_letovi = {}
        reci = linija.split("|")
        recnik_avionski_letovi["broj leta"] = reci[0]
        recnik_avionski_letovi["sifra polazista"] = reci[1]
        recnik_avionski_letovi["sifra odredista"] = reci[2]
        recnik_avionski_letovi["vreme polaska"] = reci[3]
        recnik_avionski_letovi["vreme dolaska"] = reci[4]
        recnik_avionski_letovi["sletanje sledeceg dana"] = reci[5]
        recnik_avionski_letovi["prevoznik"] = reci[6]
        recnik_avionski_letovi["dani"] = reci[7]
        recnik_avionski_letovi["model aviona"] = reci[8]
        recnik_avionski_letovi["cena"] = reci[9].replace('\n', '')
        podaci_avionski_letovi.append(recnik_avionski_letovi)

ucitaj_avionske_letove()


