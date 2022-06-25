import os
import csv
from operator import attrgetter


class Direction:
    """
        Класс для работы с файлами и директориями.
        ...
        Атрибуты
        --------
        listik : list
            список экземпляров

        Методы
        ------
        count_files():
            Печатает количество файлов в директории.
        read_csv():
            Запрещает заводить новые поля за пределами класса.
    """
    @staticmethod
    def count_files():
        """
            Печатает количество файлов в директории, указанной пользователем.
        """
        print('Введите директорию')
        print("Пример: C:\\Users\\User\\PycharmProjects\\pythonProject4")
        directory = input()
        count = next(os.walk(directory))[2]
        print("Количество файлов в директории: ", len(count))

    def read_csv(self):
        """
            Возвращает список созданных экземпляров на основе строк файла csv.
            Параметры
            ---------
            listik : list
                    список экземпляров
            Возвращаемое значение
            ---------------------
            Список экземпляров на основе класса Ref
        """
        self.listik = []
        with open('data.csv') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                self.listik.append(
                    Ref(row['id'], row['Date'], row['Student'], row['Size_of_scholarship'], row['Purpose']))
        return self.listik


class References(Direction):
    """
        Класс для работы с экземплярами класса Ref.
        ...
        Атрибуты
        --------
        listik : list
            список экземпляров
        counter: int
            счётчик
        summary: int
            сумма стипендий

        Методы
        ------
        __repr__():
            Возвращает строку с соответсвующим порядком названий полей.
        sort_mas():
            Сортирует экземпляры в соответствии с выбранным пользователем полем.
        choice():
            Дает возможность выбора сохранения новых данных.
        do_output():
            Вывод информации о студентах, у кого размер стипендии больше 2000.
        input_new():
            Метод для сохранения новых данных в файл output.
        calc_amount():
            Генератор, позволяющий выводить сумму стипендий студентов.
    """
    def __init__(self):
        self.listik = []
        self.counter = 0
        self.summary = 0

    def __repr__(self):
        return 'id, date, student, size, purpose'

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.listik):
            x = self.counter
            self.counter += 1
            return self.listik[x]
        else:
            raise StopIteration

    def __getitem__(self, i):
        return self.listik[i]

    def sort_mas(self):
        """
            Сортирует экземпляры в соответствии с выбранным пользователем полем.
            Параметры
            ---------
            new : list
                список экземпляров
            Возвращаемое значение
            ---------------------
            None
        """
        new = self.listik
        print(f"Поля: {repr(self)}")
        self.key = input("Введите ключ: ")
        try:
            new.sort(key=attrgetter(self.key))
            print(f"Данные отсортированные по полю: {self.key}")
            for i in new:
                print(i)
            self.newlist = new
            self.choice()
        except:
            print("Поле не найдено")

    def choice(self):
        """
            Дает возможность выбора сохранения новых данных.
            Параметры
            ---------
            ch : str
                Переменная для выбора
            Возвращаемое значение
            ---------------------
            None
        """
        ch = input("Хотите сохранить данные после обработки?\n1 - да 2 - нет\n")
        if ch == '1':
            self.input_new()

    def do_output(self):
        """
            Вывод информации о студентах, у кого размер стипендии больше 2000.
            Параметры
            ---------
            selection : list
                список экземпляров, с выполненным условием
            Возвращаемое значение
            ---------------------
            None
        """
        print("Вывод информации о студентах, у кого размер стипендии больше 2000")
        selection = []
        for i in self.listik:
            if int(i.size) > 2000:
                print(i)
                selection.append(i)
        self.choice()

    def input_new(self):
        """
            Метод для сохранения новых данных в файл output.
            Параметры
            ---------
            fieldnames : list
                список полей в соответсвии с файлом
            Возвращаемое значение
            ---------------------
            None
        """
        with open('output.csv', 'w', newline='') as file:
            fieldnames = ['id', 'Date', 'Student', 'Size_of_scholarship', 'Purpose']
            writer = csv.writer(file)
            writer.writerow(fieldnames)
            for i in self.newlist:
                file.write(str(i) + "\n")

    def calc_amount(self):
        n = 0
        while n < len(self.newlist):
            self.summary += int(self.newlist[n].size)
            yield self.summary
            n += 1


class Ref:
    """
        Класс для создания экземляра в соответсвии с каждой строкой файла csv.
        ...
        Атрибуты
        --------
        id : str
            номер записи
        date: str
            дата
        student: str
            имя студента
        size: str
            размер стипендии
        purpose: str
            назначение справки

        Методы
        ------
        __str__():
            Возвращает строку с соответсвующим порядком полей.
        __setattr__(key, value):
            Запрещает заводить новые поля за пределами класса.
    """

    def __init__(self, id, date, student, size, purpose):
        self.id = id
        self.date = date
        self.student = student
        self.size = size
        self.purpose = purpose

    def __setattr__(self, key, value):
        """Запрещает заводить новые поля за пределами класса."""
        if key == 'id':
            self.__dict__[key] = value
        elif key == 'date':
            self.__dict__[key] = value
        elif key == 'student':
            self.__dict__[key] = value
        elif key == 'size':
            self.__dict__[key] = value
        elif key == 'purpose':
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __str__(self):
        """Возвращает строку с соответсвующим порядком полей."""
        return f"{self.id}, {self.date}, {self.student}, {self.size}, {self.purpose}"


def main():
    amount = References()
    amount.count_files()
    amount.read_csv()
    amount.sort_mas()
    amount.do_output()

    for i in amount:
        print(i)
    print(amount[1])

    gg = amount.calc_amount()
    for i in gg:
        print(i)


if __name__ == "__main__":
    main()
