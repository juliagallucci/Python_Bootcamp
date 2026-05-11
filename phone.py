class Phone:
    def __init__(self, model, id, name, brand, price):
        self.set_model(model)
        self.set_id(id)
        self.set_name(name)
        self.set_brand(brand)
        self.set_price(price)

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be numeric.")
        self._price = price

    def calculate_total(self, tax):
        return self._price + (self._price * tax)


phone = Phone("iPhone 15", 1, "iPhone", "Apple", 999)
print("Price:", phone.get_price())
print("Total with 13% tax:", phone.calculate_total(0.13))
