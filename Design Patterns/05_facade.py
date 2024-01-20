# Subsystem classes representing low-level hardware components

class CPU:
    def execute(self):
        return "Executing CPU instructions"

class Memory:
    def load(self):
        return "Loading data into memory"

class HardDrive:
    def read(self):
        return "Reading data from hard drive"


# Facade class providing a simplified interface

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        result = []
        result.append(self.cpu.execute())
        result.append(self.memory.load())
        result.append(self.hard_drive.read())
        return result


# Client code

if __name__ == "__main__":
    # Using the computer through the facade
    computer = ComputerFacade()
    result = computer.start()

    # Displaying the simplified output
    print("Computer is starting:")
    for operation in result:
        print(operation)
