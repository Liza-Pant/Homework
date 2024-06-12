class User:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.lastname}. {self.city}. Баланс: {self.balance} руб."

    def get_guest(self):
        return f"{self.name} {self.lastname}. {self.city}"

user1 = User("Иван", "Петров", "Москва", 50000)
user2 = User("Анна", "Приставкина", "Ростов-на Дону", 50000)
user3 = User("Лизка", "Соловей", "Санкт_Петербург", 50000)
user4 = User("Петька", "Горохов", "Екатеринбург", 50000)

guests = [user1, user2, user3, user4]

for guest in guests:
    print(guest.get_guest())
