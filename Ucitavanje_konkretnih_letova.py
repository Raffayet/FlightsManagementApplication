podaci_konkretni_letovi = []


def ucitaj_konkretne_letove():

   file = open("konkretni_avionski_letovi.txt", "r")
   sadrzaj = file.readlines()
   file.close()

   for linija in sadrzaj:
      recnik_konkretni_letovi = {}
      reci = linija.split("|")
      recnik_konkretni_letovi["sifra konkretnog leta"] = reci[0]
      recnik_konkretni_letovi["broj konkretnog leta"] = reci[1]
      recnik_konkretni_letovi["datum polaska"] = reci[2]
      recnik_konkretni_letovi["datum dolaska"] = reci[3].replace('\n', '')
      podaci_konkretni_letovi.append(recnik_konkretni_letovi)

ucitaj_konkretne_letove()

