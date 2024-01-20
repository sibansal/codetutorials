from abc import ABC, abstractmethod

# Context: VendingMachine
class VendingMachine:
    def __init__(self):
        # Initial state is idle
        self.state = IdleState(self)

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def select_product(self):
        self.state.select_product()

    def dispense_product(self):
        self.state.dispense_product()

# State: State
class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_product(self):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

# Concrete States: IdleState, AcceptingCoinsState, DispensingState
class IdleState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin inserted. Switching to accepting coins state.")
        self.vending_machine.set_state(AcceptingCoinsState(self.vending_machine))

    def select_product(self):
        print("Please insert a coin before selecting a product.")

    def dispense_product(self):
        print("Please insert a coin and select a product first.")

class AcceptingCoinsState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted.")

    def select_product(self):
        print("Product selected. Switching to dispensing state.")
        self.vending_machine.set_state(DispensingState(self.vending_machine))

    def dispense_product(self):
        print("Please select a product before dispensing.")

class DispensingState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Already dispensing. Please wait.")

    def select_product(self):
        print("Already dispensing. Please wait.")

    def dispense_product(self):
        print("Product dispensed. Switching back to idle state.")
        self.vending_machine.set_state(IdleState(self.vending_machine))

# Client code
if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.insert_coin()
    vending_machine.select_product()
    vending_machine.dispense_product()

    vending_machine.insert_coin()
    vending_machine.dispense_product()

    vending_machine.select_product()
    vending_machine.dispense_product()
