import pygraphviz as pgv

class User:
    def __init__(self, login, password, email, name):
        self.login = login
        self.password = password
        self.email = email
        self.name = name

class Category:
    pass

class Transport(Category):
    pass

class Electronics(Category):
    pass

class PersonalItems(Category):
    pass

# Создаем граф
G = pgv.AGraph(strict=True)

# Добавляем узлы (классы)
G.add_node('User', shape='rectangle')
G.add_node('Category', shape='rectangle')
G.add_node('Transport', shape='rectangle')
G.add_node('Electronics', shape='rectangle')
G.add_node('PersonalItems', shape='rectangle')
G.add_node('Login', shape='oval')
G.add_node('Password', shape='oval')
G.add_node('Email', shape='oval')
G.add_node('Name', shape='oval')

# Добавляем связи
G.add_edge('User', 'Login')
G.add_edge('User', 'Password')
G.add_edge('User', 'Email')
G.add_edge('User', 'Name')
G.add_edge('Category', 'Transport')
G.add_edge('Category', 'Electronics')
G.add_edge('Category', 'PersonalItems')

# Устанавливаем параметры отображения
G.layout(prog='dot')

# Рисуем диаграмму в файл
G.draw('uml_diagram.png')

print("UML диаграмма сохранена в файле 'uml_diagram.png'")
