# Getter
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


person = Person("John")
print(person.get_name())  # John


# -------------------------------------------------------------
# Setter
class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):
        self._name = new_name


person = Person("John")
person.set_name("Alice")
print(person.get_name())  # Alice

# -----------------------------------------------------------
# Hasheatter
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name_length(self):
        return len(self._name)


person = Person("John")
print(person.name_length)  # 4



# ============================================================
# property: property Pythonning o'ziga xos mahsulotidir,
# uning yordamida atributlarga o'qish, o'zgartirish va tekshir
# ish funksiyalari beriladi.
# property dekoratori va undan foydalanish orqali obyektlarga
# getter, setter va deleter funksiyalarni qo'shish mumkin.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


person = Person("John")
print(person.name)  # John


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


person = Person("John")
print(person.name)  # John

person.name = "Alice"
print(person.name)  # Alice


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


person = Person("John")
print(person.name)  # John

del person.name
print(person.name)  # AttributeError: 'Person' object has no attribute '_name'
