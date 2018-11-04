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
      hodnota = alphabet.index(rozlozene[i])
      ciselna.append(hodnota)
      i = i+1
    return ciselna

def hlavna():
    alphabet = ["a","á","ä","b","c","č","d",
               "ď","dž","e","é","f","g",
               "h","i","í","j","k","l",
               "ĺ","ľ","m","n","ň","o",
               "ó","ô","p","q","r","ŕ",
               "s","š","t","ť","u","ú",
               "v","w","q","x","y","ý",
               "z","ž"]
 
    sprava = ''
    if len(sys.argv) != 2:
        sprava = 'prazdne'
    else:
        sprava = sys.argv[1]
    rozlozene = rozklad_spravy(sprava)
    ciselna = prevod(rozlozene, alphabet)
    print(ciselna)

hlavna()
