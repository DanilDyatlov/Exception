class Notebook:

    def __init__(self): # Метод для создания словаря 
        self.record = {}

    def add_person(self, key, val): # Метод для добавдения в словарь значений
        self.record[key] = val
    
    def find_person(self, name): # Метод для поиска значений в словаре 
        if name in self.record: 
            data = " ".join(self.record[name]) # переменая data которая означает значения для переменной name
            return f'{name} {data}'
        return ('Такого контанкта нет')
    
    def del_name(self, name): # Метод находит в словаре ключ и удаляет его 
        if name in self.record:
            del self.record[name]
            return f'{name} удален'
        raise ('Такого контанкта нет')
    
    def info(self): # Метод показывает все сохраненые контанкты
        return self.record.items()
    
print('Телефонная книга')
print('''Выберите действие
1 - Добавить контакт
2 - Найти контакт
3 - Удалить контакт
4 - Просмотреть контакты
5 - Выход''')
 
book =  Notebook()
 
while True:
    print("Введите команду \n")
    command = input()
    if command == '1':
        name = input("Имя: ")
        num = input("Номер телефона: ")
        print(book.addPerson(name, [num]))
    elif command == '2':
        name = input("Введите имя контакта >:  ")
        print(book.find(name))
    elif command == '3':
        name = input("Введите имя которое хотите удалить >:  ")
        print(book.del_name(name))
    elif command == '4':
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)
    elif command == '5':
        break
    else:
        print('Неизвестная команда')


        

    

        
