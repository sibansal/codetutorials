from abc import ABC, abstractmethod

# Subject interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject: Actual heavy image loading
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from {self.filename}")

    def display(self):
        print(f"Displaying image from {self.filename}")

# Proxy: Virtual proxy for lazy loading
class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client code
if __name__ == "__main__":
    # Using the virtual proxy for lazy loading
    image_proxy = ImageProxy("large_image.jpg")

    # The real image is loaded and displayed only when needed
    image_proxy.display()
