class Product:
	def __init__(self, name, weight, category):
		self.name = name
		self.weight = weight
		self.category = category
	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'


class Shop:
	__file_name = 'products.txt'
	def get_products(self):
		string_ = ''
		file = open(self.__file_name,'r')
		data = file.read()
		for i in data:
			string_ += i
		file.close()
		return string_

	def add(self, *products):
		product = self.get_products()
		for i in products:
			if i.name not in product:
				file = open(self.__file_name, 'a')
				file.write(' ' + i.name)

				file.close()
			else:
				print(f'Продукт {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2) # __str__
#
s1.add(p1, p2, p3)
#
print(s1.get_products())
