# Base Book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def read(self):
        return f"Reading the physical book: {self.title}"

# EBook class inheriting from Book
class EBook(Book):
    def __init__(self, title, author, pages, format_type):
        # Call the parent class's __init__ method
        super().__init__(title, author, pages)
        self.format_type = format_type
    
    def read(self):
        return f"Reading the {self.format_type} ebook: {self.title}"
    
    def download(self):
        return f"Downloading {self.title} in {self.format_type} format"

# Example usage
def main():
    # Creating a physical book
    physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    
    # Creating an ebook
    ebook = EBook("Python Basics", "John Smith", 200, "PDF")
    
    # Displaying book information
    print("Book Information:")
    print("-" * 30)
    print(physical_book.display_info())
    print(ebook.display_info())
    
    # Demonstrating polymorphism with read() method
    print("\nReading Books:")
    print("-" * 30)
    print(physical_book.read())
    print(ebook.read())
    
    # Demonstrating ebook-specific method
    print("\nEbook Special Feature:")
    print("-" * 30)
    print(ebook.download())

if __name__ == "__main__":
    main()