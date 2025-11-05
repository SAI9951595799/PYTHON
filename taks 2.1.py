class Car:
    def __init__(self, make, model, year, running):
        self.make = make
        self.model = model
        self.year = year
        self.running = running
    def show(self):
           print(f"car brand:{self.make}")
           print(f"car model:{self.model}")
           print(f"car year:{self.year}")
    def start(self):
           if  self.running==True:
               print(f"{self.make} {self.model} {self.year} is running successfully")
    def stop(self):
           if self.running==False:
               print(f"{self.make} {self.model} {self.year} is stopped")
car1=Car("Audi", "Q5", 2024,False)
car1.show()
car1.start()
car1.stop()
