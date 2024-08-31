def custom_write(file_name, strings):
    count_ = 0
    position = 0
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
       file.write(i + '\n')
    file.close()

    file2 = open(file_name, 'rb')
    for i in file2:
        count_ += 1
        start_position = position  # Сохраняем текущую позицию
        line_data = i  # Читаем строку
        position += len(line_data)  # Увеличиваем позицию на длину строки
        strings_positions[(count_, start_position)] = i.decode().strip()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)