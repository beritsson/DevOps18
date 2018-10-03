import random
class Person:
    __name = None
    __intresse = None
    ras = "Homo"

    def __init__(self, name, haircut, intresse = None):
        self.__name = name
        self.__intresse = intresse
        self.haircut = haircut

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

    def getintresse(self):
        return self.__intresse
    def setintresse(self,intresse):
        self.__intresse = intresse

    def check_intresse(self):
        if self.__intresse is None:
            self.__intresse = "studera"
            return "eftersom {0} inte tycker om nått antar jag att {0} gillar {1}".format(self.__name, self.__intresse)
        else:
            return "Vad roligt för dig då att du gillar {}".format(self.__intresse)


class Student(Person):
   # __student_id = random.randint(0, 100)                           # Här körs random en gång, oavsett studenter blir det samma randomnummer
    elevklass = "student"

    def __init__(self,name,haircut, intresse = None):
        super(Student, self).__init__(name, haircut, intresse)
        self .__student_id = random.randint(0,100)                       # Här blir det olika randomnummer under def

    def wellcome(self):
        return "Hej mitt intresse är {}".format(self.__intresse)

    def getstudent(self):
        return self.__student_id
    def setstudent(self,student_id):
        self.__student_id = student_id
'''                     Detta är för första klassen, borttagna för att göra det lättare att se resultatet i class student
person1 = Person("Björn","Dansa","Kortklippt,")
person2 = Person("Sara","Bada","Långhårig")
person3 = Person(input("Vad heter du? "), input("Vad är ditt intresse? "),input("Hår? :"))
print(person1.ras,person1.getname(),person1.getintresse(),person1.haircut)
print(person3.ras,person2.__dict__)
print(person2.ras,person2.getname(),person2.getintresse(),person2.haircut)
'''


person = Student('Björn', 'Kort')
print(person.__dict__)
print(person.check_intresse())
print(person.check_intresse())

person.setintresse('Åka skridskor')
print(person.check_intresse())

person1 = Student("Björn","Trångt")
print(person1.__dict__)