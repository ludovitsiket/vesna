#!/usr/bin/python3
import sys

def rozklad_spravy(sprava):
    upravene = []
    for znak in sprava:
        upravene.append(znak)
    return upravene

def prevod(rozlozene, alphabet):
    ciselna = []
    for item in range(len(rozlozene)):
        try:
            hodnota = alphabet.index(rozlozene[item])
            ciselna.append(hodnota)
        except ValueError as e:
            print(e)
            sys.exit()
    return ciselna

def abeceda():
    male_pismena = ["a","á","ä","b","c","č","d","ď","dž","e","é","f","g",
               "h","i","í","j","k","l","ĺ","ľ","m","n","ň","o","ó","ô",
               "p","q","r","ŕ","s","š","t","ť","u","ú","v","w","x",
               "y","ý","z","ž"]

    znaky = [",",".","!","?","_","-",";","/","=","*",
    "@","#","$","%","^","&", " "]

    velke_pismena = ["A","Á","B","C","Č","D","Ď","DŽ","E","É","F","G",
               "H","I","Í","J","K","L","Ĺ","Ľ","M","N","Ň","O","Ó",
               "P","Q","R","Ŕ","S","Š","T","Ť","U","Ú","V","W","X",
               "Y","Ý","Z","Ž"]
    alphabet = male_pismena + znaky + velke_pismena
    return alphabet

def citaj_subor(subor):
    with open(subor, 'r') as sprava:
        obsah = sprava.read()
        obsah = obsah.replace("\n","")
    return obsah

def zapis_subor(subor, obsah):
    with open(subor, 'w') as sprava:
        sprava.write(str(obsah))
    return

def help_syntax():
    print("Skript vyzaduje python3.x")
    print("Sprava urcena na zakodovanie musi byt ulozena v subore sprava.txt")

def spracovanie(abeceda):
    alphabet = abeceda()
    subor_spravy = "sprava.txt"
    kod_sprava = "kodovana.txt"
    try:
        sprava = citaj_subor(subor_spravy)
    except FileNotFoundError as e:
        print(e)
        help_syntax()
        sys.exit()
    rozlozene = rozklad_spravy(sprava)
    ciselna = prevod(rozlozene, alphabet)
    kod = zapis_subor(kod_sprava, ciselna)
    print("OK")

def main():
    spracovanie(abeceda)

if __name__ == '__main__':
  main()
