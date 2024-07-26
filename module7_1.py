class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        self.products = []

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products_str = file.read()
        return products_str

    def add(self, *products):
        with open(self.__file_name, 'r') as file:
            existing_products = file.readlines()

        for product in products:
            if str(product) + '\n' not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
