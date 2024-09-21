from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        if isinstance(weight, float) or isinstance(weight, int):
            self.weight = float(weight)
        else:
            print(f'{weight} не является числом')
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_products = open(self.__file_name, 'r')
        list_products = file_products.read()
        file_products.close()
        return list_products

    def add(self, *products):
        for product in products:
            if str(product.name) in self.get_products():        #в условии проверка ТОЛЬКО ПО ИМЕНИ!
                print('Продукт '+product.name+' уже есть в магазине')
            else:
                file_products = open(self.__file_name,'a')
                row_prod = str(product.name)+', '+str(product.weight)+', '+str(product.category)+'\n'
                file_products.write(row_prod)
                file_products.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')   #имя "Potato" уже есть с другим весом в р1,
                                                                # по условии задачи не добавлять в Shop!
print(p1) # __str__

print(s1.get_products())
s1.add(p1, p2, p3)
p4 = Product('Avocado', 0.5, 'Vegetables')
s1.add(p4)
print(s1.get_products())
