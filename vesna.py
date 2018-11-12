#!/usr/bin/python3
import sys

def rozklad_spravy(sprava):
    upravene = []
    for znak in sprava:
        upravene.append(znak)
    return upravene

def prevod(rozlozene, alphabet):
    ciselna = []
    i = 0
    while i < len(rozlozene):
        try:
            hodnota = alphabet.index(rozlozene[i])
            ciselna.append(hodnota)
            i = i+1
        except ValueError:
            sys.exit()
    return ciselna

def abeceda():
    male_pismena = ["a","á","ä","b","c","č","d","ď","dž","e","é","f","g",
               "h","i","í","j","k","l","ĺ","ľ","m","n","ň","o","ó","ô",
               "p","q","r","ŕ","s","š","t","ť","u","ú","v","w","x",
               "y","ý","z","ž"]

    znaky = [",",".","!","?","_","-",";","/","=","*"]

    velke_pismena = ["A","Á","B","C","Č","D","Ď","DŽ","E","É","F","G",
               "H","I","Í","J","K","L","Ĺ","Ľ","M","N","Ň","O","Ó",
               "P","Q","R","Ŕ","S","Š","T","Ť","U","Ú","V","W","X",
               "Y","Ý","Z","Ž"]
    alphabet = male_pismena + znaky + velke_pismena
    return alphabet

def spracovanie(abeceda):
    # nezvlada znak medzery a hviezdicku na zaciatku
    alphabet = abeceda()
    sprava = ''
    if len(sys.argv) != 2:
        sprava = 'prazdne'
    else:
        sprava = sys.argv[1]
    rozlozene = rozklad_spravy(sprava)
    ciselna = prevod(rozlozene, alphabet)
    print(ciselna)

def hlavna():
    spracovanie(abeceda)

hlavna()
