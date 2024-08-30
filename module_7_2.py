def custom_write(file_name, strings):
	count_ = 0
	strings_positions = {}
	file = open(file_name, 'w', encoding='utf-8')
	for i in strings:

		file.write(i + '\n')


	file.close()
	file2 = open(file_name, 'rb')
	for i in file2:
		count_ += 1
		number_ = file2.tell()
		strings_positions[(count_, number_)] = i.decode()

	return (strings_positions)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)