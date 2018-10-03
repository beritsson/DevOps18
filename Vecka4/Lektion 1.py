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


När man har en fil och behöver titta snabbt. Förmodligen är detta det korrekta sättet.
Man öppnar filen, man gör sitt och sen stängs filen

with open("testfil.txt",mode="r+") as p:            # Här öppnar jag en textfil tillfälligt. sen close-ar den filen
    hej = p.read()
print(hej*2)

Har jag en fil som är länkad till en variabel p, men i open-senariet använder en annan variabel k når jag texten i med
den första variabeln p
Anlednigen att stänga filen efter editering är om filen är jättestor så ska den inte ligga och ta arbetsminne.
Men printar jag open-senariets variabel går det inte efter den efter som den är stängd.

