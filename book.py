class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.set_price(price)

    def get_price(self):
        return self.price

    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be numeric.")
        self.price = price


b1 = Book('Practical Programming', 'Gries, Campbell, Montojo', 383, 50)
b2 = Book('Building a Career in Data Science', 'Robinson, Nolis', 322, 40)

print(b1.get_price())
print(b2.get_price())
