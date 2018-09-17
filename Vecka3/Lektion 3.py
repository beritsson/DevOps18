
age = 0
while True:
    age = int(input("Hur gammal är du? "))
    if age < 18:
        print("Sorry du är för ung")
        break
    elif age > 69:
        print("HAHAHA skämtar du eller, du är ju död")
        break
    else:
        låna = int(input("Hur mycket vill du låna? "))
        if (låna < 434):
            print("Tyvärr är det för lite")
        elif (låna > 3000000):
            print("Vi har inte täckning för det")
        else:
            if låna >= 434 and (låna <= 720):
                x = låna * 1.063
                print("Din ränta är 6.3% och din totala skuld blir: ", x)

            elif (låna >= 1000) and (låna <= 1494):
                x = låna * 1.03
                print("Din ränta är 3% och din totala skuld blir: ", x)
            elif (låna >=1000000) and (låna <= 3000000):
                x = låna * 0.0143
                y = x / 12
                print("Din årliga ränta blir: ", x)
                print("Din månatliga ränta blir: ",y)

                amortera = int(input("Vill du amortera? [1],[2]"))
                if (amortera == 1):
                    storlek = int(input("Hur mycket vill du amortera per månad?: "))
                    years = låna / (storlek * 12)
                    print("Det kommer ta dig",years," år att betala av ditt lån")
#                    minskning = for i in range(years):


'''
Plugga på > < tecknen. Jag har väldigt svårt för dem
=====================================

a,b,c = 10,5,2
if (a < b) or (c < b) or (c == 700):
    print("Det stämmer")
else:
    ("Stämmer inte")


x = "jörn "                             # %s - string (definneras med "xxx"
y = "bor i Älvsjö, i Långsjö "          # Man kan ha flerradskommentar (""") och enradskommentar (")
z = 'i'                                 # %c - char (definneras med 'xxx')
u = 'B'
dec = 4.123456789                       # %f - float (avrundar den femte decimalen)
tal = 4.123456789123456789              # %d - decimal (avrundar till heltal)
                                        # %(.4)s - Den visar de fyra första tecknen i strängen. Samma fungerar för %f


#print(("Jag heter %c%s%.5s %.15f  %d" % (u,x,y,tal,dec)))
print(sorted("%c%s" % (u,x)))
print((input("Vad vill du göra? : ")).upper())
'''

x = input(("Skriv in ett namn: ").lower())
y = input(("Vilken bokstav söker du?: ").lower())
print("Du undrar om bokstaven", y, "finns i namnet", x)
for i in x:
    if(y == i):
        print("Ja", y, "finns i",x)


