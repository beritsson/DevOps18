'''x = [12.2,34,"björn",4,5,"6"]
for i in range(0,6):
    print(x[i])


Detta printar värdet i en lista.
for i in range 0,6 anger hur många element det är i listan. Ändras den får jag ut mindre element

================================

x = [["12.2", "34", "björn"],[ "4", "5", "6"]]
for rad in range(2):
    for col in range(2):
        print(x[rad][col],end =" ")

Man läser delar av listan i listan.
rad in range = anger att det finns två listor i listan. Anger jag fler än 2 listor blir det error
Så anger jag siffran 1 ger det första listan.
col in range = anger vilka element som ska printas. Här kan jag ange 1-3, anger jag 4 blir det error

Detta kan skrivas ut utan range, som ger samma sak

x = [["12.2", "34", "björn"],[ "4", "5", "6"]]
for rad in x:
    for col in rad:
        print(col, end=" ")

=================================

Flerrads kommentar i koden

Singelrad är
x = "Detta är en singelradskomentar"
print(x)

Flerradskommentar
x = """ Detta är
en flerrads
kommentar"""
print(x)

=================================


===================
Kontrollstruktuerer
===================
for-sats
while-sats
if-sats

Tre variabler ska jämföras

a, b, c = 10, 20, 5
if (a < b and c < a and c == 5):
    print("det stämmer")
else:
    print("det stämmer inte")

Om dessa tre stämmer om a, b, c = 10, 20, 5
AND gör att om något av dessa påståenden skulle vara felaktiga fungerar inte formeln och den ger ELSE
Att lättast göra en negation på påståendet

if not(a < b and c < a and c == 5):


for i in range(10):
    if i == 4:
        break
    print(i)

i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)

===================================

1000 - 1498 => 3%
434 - 720 => 6.3%
'''


myloan = input("Hur mycket vill du låna? ")
if (434 - 7
    litet = (myloan * (6.3/100))
    print("Ditt lån + ränta blir: ", litet)

elif (1000 - 1498):
    stort = (myloan * (3/100))
    print("Ditt lån + 3% ränta blir: ",stort)


