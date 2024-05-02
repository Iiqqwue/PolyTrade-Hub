import hashlib #делаем хеширование


def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

hash_password = "8ec8a1f1da12f4b4b5bb2f5dc668897d41fc7b80a0317a50575a8ac4d8744e81"
input_password = input("Введите пароль")
hash_input_password = my_hash(input_password)

if hash_password != hash_input_password:
    print("Вы успешно авторизовались")
else:
    print("Неверный пароль")
