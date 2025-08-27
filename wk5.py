#  Design Your Own Class! 🏗️

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def call(self):
        print(f"{self.brand} has good specifications of {self.model}")
    
    
class Devices(Phone):
    pass

    def call(self):
        print(f"{self.brand} device is calling using {self.model} OS")

device = Devices("Techno", "Android")
print(device.model)
print(device.brand)
device.call()

mine = Phone("Techno", "Andriod")
mine.call()
        


#  Polymorphism Challenge! 

class phone:
    def speak(self):
        return "Generic phone sound..."
    
class Andriod:
    def speak(self):
        return "Rings out loud..."
    
class Tablet:
    def speak(self):
        return "Chimes out loud..."
    
class IPAD:
    def speak(self):
        return "Sings out loud..."

for device in [ Andriod(), Tablet(), IPAD()]:
    print(device.speak())
    

        