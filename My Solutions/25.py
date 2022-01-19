class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


rashik = Person("Rashik")
print("%s name is %s" % (Person.name, rashik.name))

rafsan = Person()
rafsan.name = "Rafsan"
print("%s name is %s" % (Person.name, rafsan.name))
