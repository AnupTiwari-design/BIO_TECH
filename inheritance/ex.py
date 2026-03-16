class Animal:

    def sound():
        print("Animal make sound")


class Cat(Animal):
    def voice():
        print("cat meow")

ob=Cat
ob.sound()
ob.voice()