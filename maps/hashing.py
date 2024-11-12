########## create a hash using user-defined objects#########
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.id, self.name))

s = Student("078722","Edgar")
print(hash(s.id))

