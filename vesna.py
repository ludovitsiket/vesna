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
            ciselna.append(hodnota+1)
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

def make_keys(alphabet):
    x=1
    y=[]
    while x<(len(alphabet)+1):
        y.append(x)
        x+=1
    return y

def make_dict(alphabet, keys):
    x=1
    dictionary = dict.fromkeys(keys)
    while x<(len(alphabet)+1):
        dictionary[x] = alphabet[x-1]
        x+=1
    return dictionary

def multi_replace(content, to_replace, repl):
    for elem in to_replace:
        if elem in content:
            content = content.replace(elem, repl)
    return content

def citaj_subor(subor):
    with open(subor, 'r') as sprava:
        obsah = sprava.read()
        obsah = multi_replace(obsah, ['\n','[',']'], "")
    return obsah

def zapis_subor(subor, obsah):
    with open(subor, 'w') as sprava:
        sprava.write(str(obsah))
    return sprava

def help_syntax():
    print("Skript vyzaduje python3.x")
    print("""Syntax: python3 vesna.py parameter
Sprava urcena na zakodovanie musi byt ulozena v subore sprava.txt, 
pre dekodovanie musi byt zakodovana sprava ulozena v subore kodovana.txt
Parametre: 'k' zakodovanie suboru
           'd' dekodovanie suboru""")

def coding(subor_spravy, alphabet, kod_sprava):
    sprava = citaj_subor(subor_spravy)
    rozlozene = rozklad_spravy(sprava)
    ciselna = prevod(rozlozene, alphabet)
    kod = zapis_subor(kod_sprava, ciselna)
    print("OK")

def slicing_list(content):
    result=[]
    a=0
    b=3
    character=','
    while b<(len(content)*2):
        r=(content[a:b])
        if character in r:
            r=r.replace(character,'')
        result.append(r)
        a+=3
        b+=3
    print(result)
#return result

def processing_decode(kod_sprava):
    content=[]
    obsah = citaj_subor(kod_sprava)
    for item in obsah:
        item = multi_replace(item, [' ','[',']'], "")
        content.append(item)
    content = ''.join(content)
    return content

def decoding(kod_sprava, dictionary):
    content = processing_decode(kod_sprava)
    slicing_list(content)
    print(content)

def vynimka(e):
    print(e)
    help_syntax()
    sys.exit()

def spracovanie(abeceda):
    try:
        arg = sys.argv[1]
    except IndexError as e:
        vynimka(e)
    alphabet = abeceda()
    keys = make_keys(alphabet)
    dictionary = make_dict(alphabet, keys)
    subor_spravy = "sprava.txt"
    kod_sprava = "kodovana.txt"
    if arg == 'k':
        try:
            coding(subor_spravy, alphabet, kod_sprava)
        except FileNotFoundError as e:
            vynimka(e)
    elif arg == 'd':
        try:
            decoding(kod_sprava, dictionary)
        except FileNotFoundError as e:
            vynimka(e)
    else:
        help_syntax()
        sys.exit()

if __name__ == '__main__':
    try:
        spracovanie(abeceda)
    except KeyboardInterrupt:
        sys.exit()
