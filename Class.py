class User:
    def init(self, username, email, password):
        self.username = username  # Имя пользователя
        self.email = email  # Электронная почта пользователя
        self.password = password  # Пароль пользователя

class Product:
    def init(self, name, price, description, quantity):
        self.name = name  # Название продукта
        self.price = price  # Цена продукта
        self.description = description  # Описание продукта
        self.quantity = quantity  # Количество продукта на складе

class ShoppingCart:
    def init(self):
        self.items = []  # Список товаров в корзине пользователя

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})  # Добавление товара в корзину

    def remove_item(self, product):
        for item in self.items:
            if item['product'] == product:
                self.items.remove(item)  # Удаление товара из корзины

class Order:
    def init(self, user, items, total_price, shipping_address):
        self.user = user  # Пользователь, оформивший заказ
        self.items = items  # Список товаров в заказе
        self.total_price = total_price  # Общая стоимость заказа
        self.shipping_address = shipping_address  # Адрес доставки

    def place_order(self):
        # Логика для оформления заказа
        pass

class Payment:
    def init(self, order, payment_method, amount):
        self.order = order  # Заказ, который оплачивается
        self.payment_method = payment_method  # Способ оплаты
        self.amount = amount  # Сумма оплаты

    def process_payment(self):
        # Логика для обработки платежа
        pass

class Review:
    def init(self, product, user, rating, comment):
        self.product = product  # Продукт, к которому относится отзыв
        self.user = user  # Пользователь, оставивший отзыв
        self.rating = rating  # Оценка продукта
        self.comment = comment  # Текст отзыва

class Category:
    def init(self, name, description):
        self.name = name  # Название категории
        self.description = description  # Описание категории

class Discount:
    def init(self, code, percentage, expiration_date):
        self.code = code  # Код скидки
        self.percentage = percentage  # Величина скидки в процентах
        self.expiration_date = expiration_date  # Дата окончания скидки

class Shipping:
    def init(self, method, cost, estimated_delivery):
        self.method = method  # Способ доставки
        self.cost = cost  # Стоимость доставки
        self.estimated_delivery = estimated_delivery  # Предполагаемая дата доставки

class Promotion:
    def init(self, name, description, discount, start_date, end_date):
        self.name = name  # Название акции
        self.description = description  # Описание акции
        self.discount = discount  # Скидка, предоставляемая в рамках акции
        self.start_date = start_date  # Дата начала акции
        self.end_date = end_date  # Дата окончания акции

class Wishlist:
    def init(self, user):
        self.user = user  # Пользователь, владелец списка желаний
        self.items = []  # Список товаров в списке желаний

    def add_item(self, product):
        self.items.append(product)  # Добавление товара в список желаний

    def remove_item(self, product):
        self.items.remove(product)  # Удаление товара из списка желаний

class Vendor:
    def init(self, name, email, products):
        self.name = name  # Название поставщика
        self.email = email  # Электронная почта поставщика
        self.products = products  # Список продукции, поставляемой поставщиком

    def add_product(self, product):
        self.products.append(product)  # Добавление продукта от поставщика

    def remove_product(self, product):
        self.products.remove(product)  # Удаление продукта от поставщика

class Inventory:
    def init(self):
        self.products = []  # Список всех продуктов на складе интернет-магазина

        def add_product(self, product):
            self.products.append(product)  # Добавление продукта на склад

        def remove_product(self, product):
            self.products.remove(product)  # Удаление продукта со склада

    class Notification:
        def init(self, user, message, date):
            self.user = user  # Пользователь, которому отправлено уведомление
            self.message = message  # Текст уведомления
            self.date = date  # Дата и время отправки уведомления