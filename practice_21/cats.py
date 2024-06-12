import json


class Cat:
    def __init__(self, name='', age=0):
        self.name = name
        # self.sex = sex
        self.age = age

    def init_from_dict(self, event_dict):
        self.name = event_dict.get("name")
        self.sex = event_dict.get("gender").get("name")
        self.age = event_dict.get("age")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def get_sex(self):
        return self.sex


with open('json_cats.json', 'r', encoding="UTF-8") as json_file:
    data_cats = json.load(json_file)

cat_obj = Cat()
cat_obj.init_from_dict(data_cats)
for i in data_cats:
    print('Кличка', cat_obj.get_name())
    print('Возраст', cat_obj.get_age())
    print('Пол', cat_obj.get_sex())
    print('------------')

# for i in data_cats:
#     print(data_cats[i])
#     print('перевод\n')
