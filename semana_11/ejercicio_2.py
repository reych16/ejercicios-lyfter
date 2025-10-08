class Person:
    def __init__(self, name):
        self.name = name

class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
    

    def add_passengers(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} subió al bus")
        else:
            print("El bus está lleno. No puede subir más pasajeros.")

    
    def remove_passenger(self, person):
        if person in self.passengers: 
            self.passengers.remove(person)
            print(f"{person.name} bajó del bus.")
        else:
            print(f"{person.name} no está en el bus.")


p1 = Person("Reychel")
p2 = Person("Byron")
p3 = Person("Sandra")


bus = Bus(2)

bus.add_passengers(p1)
bus.add_passengers(p2)
bus.add_passengers(p3)

bus.remove_passenger(p1)
bus.remove_passenger(p3)

