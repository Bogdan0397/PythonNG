
import pickle
books = [("Book A", 29.99), ("Book B", 39.95), ("Book C", 24.50)]

with open("books.bin", "rb") as file:
    print(pickle.load(file))