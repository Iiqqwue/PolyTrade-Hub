
class User:
    def init(self, username, email, password):
        self.username = username  # Имя пользователя
        self.email = email  # Электронная почта пользователя
        self.password = password  # Пароль пользователя

class Product:
    def init(self, name, price, description, quantity, seller):
        self.name = name  # Название товара
        self.price = price  # Цена товара
        self.description = description  # Описание товара
        self.quantity = quantity  # Количество товара
        self.seller = seller  # Продавец товара

class Advertisement:
    def init(self, title, description, owner):
        self.title = title  # Заголовок объявления
        self.description = description  # Описание объявления
        self.owner = owner  # Владелец объявления

class ShoppingCart:
    def init(self):
        self.items = []  # Товары в корзине

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})  # Добавление товара в корзину

    def remove_item(self, product):
        for item in self.items:
            if item['product'] == product:
                self.items.remove(item)  # Удаление товара из корзины

class Order:
    def init(self, user, items, total_price, shipping_address):
        self.user = user  # Пользователь, оформивший заказ
        self.items = items  # Товары в заказе
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
        self.product = product  # Товар, к которому относится отзыв
        self.user = user  # Пользователь, оставивший отзыв
        self.rating = rating  # Оценка товара
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
        self.items = []  # Товары в списке желаний

    def add_item(self, product):
        self.items.append(product)  # Добавление товара в список желаний

    def remove_item(self, product):
        self.items.remove(product)  # Удаление товара из списка желаний

class Vendor:
    def init(self, name, email, products):
        self.name = name  # Название продавца
        self.email = email  # Электронная почта продавца
        self.products = products  # Товары, предлагаемые продавцом

    def add_product(self, product):
        self.products.append(product)  # Добавление товара от продавца

    def remove_product(self, product):
        self.products.remove(product)  # Удаление товара от продавца

class Inventory:
    def init(self):
        self.products = []  # Товары на складе

class Notification:
    def init(self, user, message, date):
        self.user = user  # Получатель уведомления
        self.message = message  # Содержание уведомления
        self.date = date  # Дата и время уведомления

class AdvertisementManager:
    def init(self):
        self.advertisements = []  # Список объявлений

    def add_advertisement(self, advertisement):
        self.advertisements.append(advertisement)  # Добавление объявления

    def remove_advertisement(self, advertisement):
        self.advertisements.remove(advertisement)  # Удаление объявления

class PaymentProcessor:
    def process_payment(self, payment_info):
        # Логика обработки платежа
        pass

class ReviewManager:
    def init(self):
        self.reviews = []  # Список отзывов

    def add_review(self, review):
        self.reviews.append(review)  # Добавление отзыва

    def remove_review(self, review):
        self.reviews.remove(review)  # Удаление отзыва

class CategoryManager:
    def init(self):
        self.categories = []  # Список категорий

    def add_category(self, category):
        self.categories.append(category)  # Добавление категории

    def remove_category(self, category):
        self.categories.remove(category)  # Удаление категории

class DiscountManager:
    def init(self):
        self.discounts = []  # Список скидок

    def add_discount(self, discount):
        self.discounts.append(discount)  # Добавление скидки

    def remove_discount(self, discount):
        self.discounts.remove(discount)  # Удаление скидки

