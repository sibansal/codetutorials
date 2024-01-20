from abc import ABC, abstractmethod

# Mediator: AirTrafficControl
class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self, airplane):
        pass

    @abstractmethod
    def send_message(self, sender, message):
        pass

# Colleague: Airplane
class Airplane:
    def __init__(self, registration_number, atc):
        self.registration_number = registration_number
        self.atc = atc

    def send_message(self, message):
        self.atc.send_message(self, message)

    def receive_message(self, message):
        print(f"Airplane {self.registration_number} received message: {message}")

# Concrete Mediator: ConcreteAirTrafficControl
class ConcreteAirTrafficControl(AirTrafficControl):
    def __init__(self):
        self.airplanes = []

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    def send_message(self, sender, message):
        for airplane in self.airplanes:
            if airplane != sender:
                airplane.receive_message(message)

# Client code
if __name__ == "__main__":
    # Creating an air traffic control system
    atc = ConcreteAirTrafficControl()

    # Creating airplanes and registering them with the ATC
    airplane1 = Airplane("ABC123", atc)
    airplane2 = Airplane("XYZ789", atc)
    atc.register_airplane(airplane1)
    atc.register_airplane(airplane2)

    # Airplanes communicate through the ATC
    airplane1.send_message("Traffic ahead, change course.")
    airplane2.send_message("Acknowledged. Adjusting course.")
