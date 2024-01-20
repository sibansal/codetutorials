import copy

class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

class FileSystem:
    def __init__(self):
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def copy_file(self, file_name, target_directory):
        for file in self.files:
            if file.name == file_name:
                new_file = file.clone()
                new_file.name = f"{target_directory}/{file_name}"
                self.add_file(new_file)
                print(f"File '{file_name}' copied to '{target_directory}'")
                return
        print(f"File '{file_name}' not found.")

# Client code
if __name__ == "__main__":
    # Creating a prototype file
    original_file = File("example.txt", "This is the content of the original file.")

    # Creating a file system and adding the prototype file
    file_system = FileSystem()
    file_system.add_file(original_file)

    # Copying the prototype file to a new directory
    file_system.copy_file("example.txt", "backup")

    # Modifying the original file does not affect the copied file
    original_file.content = "Modified content."

    # Displaying the content of the copied file
    for file in file_system.files:
        print(f"File: {file.name}, Content: {file.content}")
