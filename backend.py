# сюда нужно импортировать классы бд
import sqlite3
import data.config


class UserInterface:
    def __init__(self, login, password, path_to_db = data.config.path_to_database):
        # if not self.try_log_in(login, password):
        #     raise Exception('Пользователя с такими данными не существует! Неверен логин/пароль!')
        self.path_to_db = path_to_db
        self.login = login
        self.password = password
        self.create_table_of_users()


    def create_table_of_users(self):
        sql = '''
        create table IF NOT EXISTS `users` (
          `user_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
          `login` varchar(255) not null,
          `password` varchar(255) not null
        )'''
        self.execute(sql, commit=True)


    def create_table_of_desk(self):
        sql = '''
        create table IF NOT EXISTS `desk` (
            `desk_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
            
        )'''
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


    @staticmethod
    def is_login_exist(self, login):
        # проверяет существует ли пользователь с указанным логином
        sql = "SELECT * FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)

        if result is not None:
            print("Пользовательн с таким логином существует")
            return True  # существует
        else:
            print("Пользователья с таким логином не существует")
            return False  # не существует


    @staticmethod
    def try_log_in(self, login, password):
        # проверяет cуществует ли пользователь с логин/пароль
        sql = "SELECT * FROM users WHERE login=? AND password=?"
        result = self.execute(sql, (login, password), fetchone=True)

        if result is not None:
            print("Пользователь с таким логином и паролем существует")
            return True  # существует
        else:
            print("Пользователья с таким логином и паролем существует")
            return False  # не существует (Неверен логин/пароль)


    @staticmethod
    def add_new_user(self, login, password):
        if UserInterface.is_login_exist(login):
            raise Exception('Пользователя с таким логином уже существует!')
        # добавляем в бд нового пользователя
        sql_insert = "INSERT INTO users (login, password) VALUES (?, ?)"
        self.execute(sql_insert, (login, password), commit=True)
        print("Пользователь успешно добавлен")
        return True


    @staticmethod
    def get_user_login_by_id(self, id):
        # возвращает логин пользователя по id
        sql = "SELECT login FROM users WHERE user_id =?"
        result = self.execute(sql, (id,), fetchone=True)
        login = result[0]
        if result is not None:
            print("Логин пользователя по его id")
            return login


    @staticmethod
    def get_user_id_by_login(self, login):
        # возвращает id пользователя по логину (логин уникален для каждого пользователя)
        sql = "SELECT id FROM users WHERE login=?"
        result = self.execute(sql, (login,), fetchone=True)
        id = result[0]
        if result is not None:
            print("id пользователя по его логину")
            return id

    def create_desk(self, desk_name, desk_type):
        # создаём доску в бд
        # владелец доски self.login
        # True - доска успешно создана
        # False - доска с таким именем уже существует
        return True

    def get_owned_desks(self):
        # список досок которыми владеет пользователь (self.login) в формате (desk_id, desk_name, public, owner_login)

        return [(0, 'Доска 1', 0, 'Myself'), (1, 'Доска для 2112', 1, 'Myself')]

    def get_public_desks(self):
        # список публичных досок в формате (desk_id, desk_name, public)

        return [(33, 'Доска 333', 1, 'Sera'), (222, 'Доска 77', 1, 'Bob')]

    def can_edit_desk(self, desk_id):
        # можем ли мы редактировать доску
        # доску может редактировать владелец или пользователь из таблицы "права на редактирования"

        return True

    @staticmethod
    def get_desk_name_by_desk_id(desk_id):
        # desk_name - не уникален

        return 'desk_name'

    @staticmethod
    def get_column_name_by_column_id(column_id):
        # column_name - не уникален

        return 'column_name'

    def change_desk_name(self, desk_id, new_desk_name):
        # изменяем имя доски в бд
        # True - успешно
        # False - доска с таким именем уже существует

        return True

    # TODO: LAST
    def change_column_name(self, column_id, new_column_name):
        # изменяем имя column в бд
        # True - успешно
        return True

    def del_column(self, column_id):
        # удоляем колонку из бд
        # True - успешно
        return True

    def del_desk(self, desk_id):
        # удоляем desk из бд
        # True - успешно
        return True

    def add_column_to_desk(self, desk_id, column_name):
        # добавляем новый столбец на доску
        # создание новой колонки в бд
        return True

    def add_card_to_column(self, card_title, card_status, card_desk_id, card_column_id):
        # добавляем карточку в конец колонки + в бд
        return True

    def get_desk_card(self, desk_id):
        # возвращает карточки в desk в формате:
        cards = {
            ('column_id', 'название столбца'): [
                ('card_id', 'card_title', 'card_status', 'card_number_in_column'),
                ('0', 'Заголовок', '1', '0'),
            ]
        }
        return {
            (22, 'Столбец 1'): [
                ('0', 'Заголовок 1', '1', '0'),
                ('1', 'Заголовок 2', '1', '1'),
                ('2', 'Заголовок 3', '2', '3'),
            ],
            (32, 'Столбец 2'): [
                ('33', 'Заголовок 1', '0', '0'),
                ('43', 'Заголовок ttt', '3', '1'),
            ]
        }

    def get_full_card_info(self, card_id):
        return {
            'card_id': '11',
            'card_title': 'Title 555',
            'card_text': 'lorem text',
            'card_status': 2,
            'card_author_login': 'Sergey',
            'card_desk_id': 3,
            'card_column_id': 333,
            'card_number_in_column': 33
        }

    def change_card_title(self, card_id, new_title):
        return True

    def change_card_text(self, card_id, new_text):
        return True

    def change_card_status(self, card_id, new_status):
        return True

    def move_card(self, card_id, current_column_id, new_column_id, card_number_in_new_column):
        # перемещает карточку в новый столбец
        # нужно перезаписать card_number_in_column для всех карточек в current_column_id и new_column_id
        return True

    def add_edit_rights_on_public_desk(self, user_id, desk_id):
        # добавляет пользователя права на редактирование публичной доски
        return True

    def del_edit_rights_on_public_desk(self, user_id, desk_id):
        # удаляет пользователя права на редактирование публичной доски
        return True

    def get_all_user(self):
        # список всех пользователе (user_id, login)
        return [(1, 'Bob'), (3, 'Sera')]

    def get_all_user_with_edit_rights(self, desk_id):
        # список всех пользователе (user_id, login, can_edit_desk)
        # can_edit_desk - может ли пользователь редактировать доску с desk_id
        # (актуально только для общественных досок)
        return [(1, 'Bob', 0), (3, 'Sera', 1), (33, 'Pol', 1)]


if __name__ == '__main__':
    user1 = UserInterface("zxc", "123")
    user1.add_new_user("zxc", "123")