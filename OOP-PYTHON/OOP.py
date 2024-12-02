# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"{self.model} is calling {number} 📞"

    def send_message(self, number, message):
        return f"{self.model} sent a message to {number}: {message}"

    def __str__(self):
        return f"{self.brand} {self.model}, {self.storage}GB Storage, {self.battery}mAh Battery"

# Child Class (Inheritance Layer)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_resolution):
        super().__init__(brand, model, storage, battery)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        return f"{self.model} took a photo with {self.camera_resolution}MP resolution 📸"

# Using the Classes
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 3700)
print(phone1)
print(phone1.make_call("123-456-7890"))

phone2 = SmartphoneWithCamera("Apple", "iPhone 14", 256, 3200, 48)
print(phone2)
print(phone2.take_photo())
