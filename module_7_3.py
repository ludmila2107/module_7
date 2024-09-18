class WordsFinder:
	def __init__(self, *file_names):
		self.file_names = file_names

	def get_all_words(self):
		all_words = {}
		exception = [',', '.', '=', '!', '?', ';', ':', ' - ']
		for name in self.file_names:
			with open(name, encoding='utf-8') as file1_:
				s = []
				for line in file1_:
					line = line.lower()
					for letter in line:
						filtered_line = ''.join(letter for letter in line if letter not in exception)
					line = filtered_line.strip()
					s += line.split()
					all_words[file1_.name] = line.split()
				all_words[file1_.name] = s
		return all_words
	# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
	# значение - позиция первого такого слова в списке слов этого файла.
	def find(self, word):
		self.word = word.lower()
		dict_ = {}
		data = self.get_all_words()

		for key, value in data.items():
			if self.word in value:
				print(value)
				dict_[key] = value.index(self.word)+1
		return (dict_)

	def count(self, word):
		self.word = word.lower()
		dict_ = {}
		data = self.get_all_words()

		for key, value in data.items():
			count_ = 0
			for i in value:
				if self.word == i:
					count_ += 1
			dict_[key] = count_
		return dict_


finder2 = WordsFinder('test.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего