class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id
    def display_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}"
    
class Book(Product):
    def __init__(self, name, price, product_id, author, isbn):
        super().__init__(name, price, product_id)
        self.author = author
        self.isbn = isbn
    
    def display_info(self):
        #method overriding to add book specific details
        base_info = super().display_info()
        return f"{base_info}, Author: {self.author}, ISBN: {self.isbn}"
    
class Electronics(Product): # electronics inherits from Product
    def __init__(self, name, price, product_id, brand, warranty_period):
        super().__init__(name, price, product_id)
        self.brand = brand
        self.warranty_period = warranty_period

    
    def display_info(self):
        #method overriding to add electronics specific details
        base_info = super().display_info()
        return f"{base_info}, Brand: {self.brand}, Warranty: {self.warranty_period} years"
    
my_book = Book("The Great Gatsby", 10.99, "B001", "F. Scott Fitzgerald", "9780743273565")
my_electronic = Electronics("Smartphone", 699.99, "E001", "Samsung", 2)

print("\n--- Book Information (Inherited) ---")
print(my_book.display_info())   

print("\n--- Electronics Information (Inherited) ---")
print(my_electronic.display_info())   