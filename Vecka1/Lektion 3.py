'''for x in range(0,11):            # Skriver ut 0 * 5 = 0 upp till tio
    print(x, "* 5 = ", x *5)

#_______________________________
print("_____________________________")
print("Expotensiell beräkning")
print("_____________________________")
for x in range(10,0,-1):                    #range(0,10,2) = stegar upp två i taget upp till tio.
                                            #range(10,-1,-1) = stegar ner från tio till 1 med -a´1

    print(x,"^",x," = ",x**x)


#______________________________________________
for x in range(0,4):                        # matris. Första forloopen ger rad med blanksteg, nedräkning till fyra gånger
    print("")                               # under dessa fyra gånger görs
    print("-------------")
    print("|", end = "")
    for y in range(0,3):

        print(" + |", end = "")          # end = "" - fattar inte.


print("\n-------------")

_______________________________________________

x = 10                                      # x = 10 och y = 20 ska byta värde med varandra
y = 20

z = x                                       #
x = y
y = z

print(x)
print(y)



__________________________________________________

x = 10                                      # inbyggd funktion att vända värden
y = 20

x,y = y,x

print("x =",x)
print("y =",y)
_______________________________________________


for x in range(0,3):                        # matris. Första forloopen ger rad med blanksteg, nedräkning till fyra gånger
    print("")                               # under dessa fyra gånger görs
    print("-------------")
    print("|", end = "")
    for y in range(0,3):

        print(" ", x**4, " |", end = "")          # end = "" - fattar inte.


print("\n-------------")
___________________________________________
'''
import sys

print("Vad heter du?")
name = sys.stdin.readline()

print("Hej",name)

print("Hur gammal är du")
ålder = sys.stdin.readline()
print("Du är ", (ålder *365), " dagar gammal")



