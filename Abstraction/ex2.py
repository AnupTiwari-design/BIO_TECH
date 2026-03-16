from abc import ABC

class Fan(ABC):
    def on():
        pass

    def off():
        pass

    def details():
        print("features of fan")

class Celling_Fan(Fan):

    def on():
        print("fan is onn")
    def off():
        print("fan is off")
ob=Celling_Fan
ob.details()
ob.on()
ob.off()