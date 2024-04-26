#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
#на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
#Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
#пользователя из системы.

#Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
#('user' для обычных сотрудников).

#2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа,
#специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые
#позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь
#доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name, access_level):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def info(self):
        print(f"Добро пожаловать {self.__name}")
        print(f"Ваш id - {self.__id}")
        print(f"Уровень доступа - {self.__access_level}")



class Admin(User):
    def __init__(self, id, name, access_level="Admin"):
        super().__init__(id, name, access_level)
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user):
        if user in self.__user_list:
            self.__user_list.remove(user)
            print(f"Пользователь {user.get_name()} удален.")
        else:
            print("Пользователь не найден в списке.")

    def list_users(self):
        for user in self.__user_list:
            print(f"Пользователь: {user.get_name()}, ID: {user.get_id()}, Уровень доступа: {user.get_access_level()}")





user1 = User("1", "Иван", "пользователь")
admin1 = Admin("2", "Александр", "администратор")

user1.info()
admin1.info()

admin1.add_user(user1)
admin1.remove_user(user1)