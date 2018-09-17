'''Filhantering
Skapa filer och läsa filer

skapa en ny fil:
skapa en fil till en variabel
f = open("Textfil.txt",mode="w")            # Nu skapas en textfil.txt mode read eller write (måste ändra mode vid läs eller skriv?)
                                            # "a" = apend
                                            # "r+" =read/write-mode
skriv till fil
f.write = ("text")

Läsa från fil
f.open("Textfil.txt",mode="r")              # Ändra mode till Read
f.read()

När man läser från fil, antingen f.read(), allt ihop, eller f.readline() rad för rad måste man spela tillbaka pekaren till start med
f.seek(0)                                   # (0) är antal tecken. prova att ändra (0 till andra tecken)

print()     -   funktioner
f.read()    -   metoder

'''
d = open("text.txt",mode="r+")
print(d,mode)