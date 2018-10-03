'''OOP - Objekt orienterad Programmering

Allt anses vara OBJEKT

Egenskaper eller attribut  -  variabler

class person:
    pass
person1 = person()                  # Instansiera
print(person)                       # Instansiera

person2 = person()
print(person)

Instansiera = Skapa objekt i klassen
person1 och person2 är variabler
.name är en EGENSKAP

Hur man skapar OOP
1. Man börjar med klass deklaration
    class person
        pass

2. Skapa ett objekt av klassen (instansiering)
    person1 = person()   # klassen anges i nr 2 som en funktion
3.

Så här kan man göra ordagrant


class person:
    pass
person1 = person()
print(person)
person1.name = "Björn"
person1.intresse = "Byggvård"
person1.civilstånd = "Gift"
print(person1.__dict__)



person2 = person()
print(person)
person2.name = "Sara"
person2.intresse = "Bada"
person2.civilstånd = "Gift"
print(person2.name,person2.civilstånd,person2.intresse)

====================================================

Det här är ett lättare sätt
'''
class person:

    name = None
    intresse = None


    def __init__(self, name, intresse, civilstånd, ålder):
        self.name = name
        self.intresse = intresse
        self.civilstånd = civilstånd
        self.ålder = ålder


person1 = person("Björn","byggvård","gift","45")
person2 = person("Sara","Bada","Gift","40")
person3 = person(input("Vad heter du? "), input("Vad är ditt intresse? "), input("Civilstånd? "),input("Hur gammal är du? "))
person4 = person(input("Vad heter du? "), input("Vad är ditt intresse? "), input("Civilstånd? "),input("Hur gammal är du? "))
print(person1.__dict__)
print(person2.__dict__)
print(person3.__dict__)
print(person4.__dict__)
'''
=============================================

Nu gör vi egenskaperna hemliga. Två understrykningar gör man dem osynliga.
Finns __ i __name i classen och i DEF. Då går det inte att få upp dem printen print(person1.xxx)
Men tar jag bort dubbel understrykning på class och def så går det att få upp den i printen

class Person:
    __name = None
    __intresse = None

    def __init__(self, name, intresse):
        self.__name = name
        self.__intresse = intresse

    def getname(self):
        return self.__name
    def setname(self,intresse):
        self.__name = intresse



person1 = Person("Björn", "Bygga hus")
person1.setname("äta mat")
print(person1.getname())

'''