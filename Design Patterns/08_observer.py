import tkinter as tk

# Subject: SubjectButton
class SubjectButton:
    def __init__(self, master, text="Click me"):
        self.button = tk.Button(master, text=text, command=self.click)
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def click(self):
        print("Button clicked!")
        self.notify_observers()

# Observer: Observer
class Observer:
    def update(self):
        pass

# Concrete Observer: LoggingObserver
class LoggingObserver(Observer):
    def update(self):
        print("Logging: Button clicked!")

# Concrete Observer: PopupObserver
class PopupObserver(Observer):
    def update(self):
        popup = tk.Toplevel()
        popup.title("Notification")
        label = tk.Label(popup, text="Button clicked!")
        label.pack()

# Client code
if __name__ == "__main__":
    root = tk.Tk()

    # Creating a button and observers
    button = SubjectButton(root)
    logging_observer = LoggingObserver()
    popup_observer = PopupObserver()

    # Adding observers to the button
#    button.add_observer(logging_observer)
    button.add_observer(popup_observer)

    # Placing the button in the Tkinter window
    button.button.pack()

    root.mainloop()
