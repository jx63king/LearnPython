# https://www.afternerd.com/blog/learn-python/#level1

# class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name

p = Person('Alice', 22)
p.get_name()


