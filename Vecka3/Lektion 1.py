'''
b = 'Jag går i Nackademin""'
a = """ Jag kan nu skiva som en
stycke med radbrytning,
Med tre citattecken fungarar på samma
 sätt (backslash n) som också är radbrytning"""
print(b+"\n"+a)

x = 10302030;
print(type(x))

print(len("Alla bokstäver är vokaler och konsonanter")


x = int("10")
print(type(x))                                      # kolla klass på värdet x

a = ["10", "Bjorn", 4]                              # Skapa en lista med olika värden
a = []                                              # Nollställ listan
print(a)


a = int(3.1415)
b = [i for i in range(1,20)]
x = [2*a*i for i in range(1,20)]
y = [a*i**2 for i in range(1,20)]
print(b)
print("omkretsen på en cirkel",x)
print("arean på en cirkel",y)



tre_listor =[["a","b","c"], ["1","2","3"],["x","y","z"]]
print(tre_listor)

for i in tre_listor:                            # den här listar första listan
    for j in i:                                 # den här listar listan i listan
        print(j,end=" ")                        # den här printar ut elementen ur listan i listan samt # Vid varje element lägger den till mellanslag i slutet av värdet



x=[["1","2","3"],["4","5","6"]]


for row in x:
    for col in row:
        print(col, end=" ")
'''
import math
x = [[2*math.pi*i] for i in range(5)]
print(x)

