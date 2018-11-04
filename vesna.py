#!/usr/bin/python3
import sys

def kluce(hodnoty, sprava):
#    print(len(hodnoty))
#    print(hodnoty[1])
    return

def rozklad_spravy(sprava):
#    print(sprava)
    return

def hlavna():
    abeceda = {1:"a", 2:"á", 3:"ä", 4:"b", 5:"c", 6:"č", 7:"d", 8:"ď", 9:"dž",
            10:"e", 11:"é", 12:"f", 13:"g", 14:"h", 15:"i", 16:"í", 17:"j",
            18:"k", 19:"l", 20:"ĺ", 21:"ľ", 22:"m", 23:"n", 24:"ň", 25:"o",
            26:"ó", 27:"ô", 28:"p", 29:"q", 30:"r", 31:"ŕ", 32:"s", 33:"š",
            34:"t", 35:"ť", 36:"u", 37:"ú", 38:"v", 39:"w", 40:"q", 41:"x",
            42:"y", 43:"ý", 44:"z", 45:"ž"}
    sprava = ''
    if len(sys.argv) != 2:
        print('prazdne')
    else:
        sprava = sys.argv[1]
    rozklad = rozklad_spravy(sprava)
    print(rozklad)
    kluce(abeceda, sprava)

hlavna()
