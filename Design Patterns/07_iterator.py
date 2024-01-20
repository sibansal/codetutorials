# Concrete Aggregate: MyDict
class MyDict:
    def __init__(self):
        self.items = {}

    def add_item(self, key, value):
        self.items[key] = value

    def create_iterator(self):
        return MyDictIterator(self)

# Concrete Iterator: MyDictIterator
class MyDictIterator:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.keys = list(my_dict.items.keys())
        self.index = 0

    def has_next(self):
        return self.index < len(self.keys)

    def next(self):
        if self.has_next():
            key = self.keys[self.index]
            value = self.my_dict.items[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration("End of iteration")

# Client code
if __name__ == "__main__":
    # Creating a dictionary and adding items
    my_dict = MyDict()
    my_dict.add_item("Key1", "Value1")
    my_dict.add_item("Key2", "Value2")
    my_dict.add_item("Key3", "Value3")

    # Iterating through the dictionary using the iterator
    iterator = my_dict.create_iterator()

    while iterator.has_next():
        key, value = iterator.next()
        print(f"{key}: {value}")
