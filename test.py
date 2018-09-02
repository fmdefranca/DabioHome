class Test(object):
    name = 'fabio'
    age = 28


class BabyFabio(Test):
    name = 'baby Fabio'

class ChangeOnlyAge(Test):
    age = 23

new_person = BabyFabio()

new_age = ChangeOnlyAge()

print("{} {}".format(new_person.name, new_person.age))
print("{} {}".format(new_age.name, new_age.age))