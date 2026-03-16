class Animal:
    def print_property():
        print("make sound")
class Dog:
    def sound():
        print("dog barks")

class Puppy(Dog,Animal):
    def child():
        print("child of dog")
ob=Puppy
ob.child()
ob.sound()
ob.print_property()