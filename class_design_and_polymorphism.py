# Title: Class Design and Polymorphism Example

import sys

# Ensure UTF-8 encoding for compatibility with emojis
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    # Fallback for older Python versions
    pass

# Assignment 1: Book and EBook Classes with Inheritance
class Book:
    """A class representing a book."""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        """Simulates reading the book."""
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        """Displays book information."""
        return f"'{self.title}' by {self.author}, {self.pages} pages."

class EBook(Book):
    """A subclass representing an electronic book."""
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def download(self):
        """Simulates downloading the eBook."""
        print(f"Downloading '{self.title}' by {self.author}, size: {self.file_size}MB.")

    def info(self):
        """Displays eBook information, overriding the parent method."""
        return f"'{self.title}' by {self.author}, {self.pages} pages, {self.file_size}MB file size."

# Activity 2: Polymorphism with Animals and Vehicles
class Animal:
    """A base class for animals."""
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    """A class representing a dog."""
    def move(self):
        print("The dog runs on four legs. 🐕")  # Emoji for UTF-8 terminals

class Bird(Animal):
    """A class representing a bird."""
    def move(self):
        print("The bird flies in the sky. 🕊️")  # Emoji for UTF-8 terminals

class Vehicle:
    """A base class for vehicles."""
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    """A class representing a car."""
    def move(self):
        print("The car drives on the road. 🚗")  # Emoji for UTF-8 terminals

class Plane(Vehicle):
    """A class representing a plane."""
    def move(self):
        print("The plane flies in the air. ✈️")  # Emoji for UTF-8 terminals

# Main program demonstrating both features
if __name__ == "__main__":
    # Part 1: Demonstrate Book and EBook
    print("Book and EBook Demonstration:")
    my_book = Book("1984", "George Orwell", 328)
    my_ebook = EBook("Digital Fortress", "Dan Brown", 356, 1.5)
    print(my_book.info())
    my_book.read()
    print(my_ebook.info())
    my_ebook.download()
    
    print("\nPolymorphism Demonstration:")
    # Part 2: Demonstrate Polymorphism with Animals and Vehicles
    # Create instances of animals
    my_dog = Dog()
    my_bird = Bird()

    # Create instances of vehicles
    my_car = Car()
    my_plane = Plane()

    # Demonstrate polymorphic behavior
    print("Animal Moves:")
    my_dog.move()
    my_bird.move()

    print("\nVehicle Moves:")
    my_car.move()
    my_plane.move()
