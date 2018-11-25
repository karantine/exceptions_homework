# 'Functions' homework extended with command 'n'

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

command = input('Введите команду:\n\n p - спросит номер документа и выведет имя человека, которому он принадлежит,\n l - выведет список всех документов в формате passport "2207 876234" "Василий Гупкин",\n s - спросит номер документа и выведет номер полки, на которой он находится,\n a - добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться,\n n - выведет имена всех владельцев документов\n\nЧтобы выйти, введите exit.\n')

# n - функция, выводящая имена всех владельцев документов. С помощью исключения KeyError проверяйте, если поле "name" и документа.

def get_name(documents):
    try:
        for item in documents:
            print(item['name'])
    except KeyError:
        print('Ни одного имени не обнаружено')

# p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def person():
  doc_number = input('Введите номер документа:')
  result = ''
  for doc in documents:
    if doc_number == doc['number']:
      result = doc['name']
      print('Имя владельца: {}\n'.format(result))
  if result == '':
      print('Имя не найдено.\n')
  return result

# l - команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def document_list(documents):
  new_list = []
  for item in documents:
    new_list.append(item.values())
  print('{}\n'.format(new_list))
  return new_list

# def document_list(documents):
#   for dicts in documents:
#     for value in dicts.items():
#       result = list(dicts.values())
#     print('{}\n'.format(result))
#   return result

# s - команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def shelf():
  result = ''
  document_number = input('Введите номер документа:')
  for shelf_num, doc_list in directories.items():
    for doc_num in doc_list:
      if document_number == doc_num:
        result = shelf_num
        print('Документ хранится на полке: {}\n'.format(result))
        return result
  print('Не найдено\n')
  return result

# a - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add_doc(documents, directories):
  doc_type = input('Введите тип документа:')
  doc_num = input('Введите номер документа:')
  owner_name = input('Введите имя:')
  shelf = input('Введите номер полки:') 
  dict_item = {}
  dict_item['type'] = doc_type
  dict_item['number'] = doc_num
  dict_item['name'] = owner_name
  documents.append(dict_item)
  if shelf not in directories.keys():
    directories[shelf] = []
  directories[shelf].append(doc_num)
  
  print(documents)
  print(directories)

while command:
  if command == 'p':
    person()
  if command == 'l':
    document_list(documents)
  if command == 's':
    shelf()
  if command == 'a':
    add_doc(documents, directories)
  if command == 'n':
      get_name(documents)
  if command == 'exit':
      break
  else:
    command = input('Введите команду: p, l, s или a. Чтобы выйти, введите exit.\n')
    if command == 'exit':
      break
