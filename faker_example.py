from faker import Faker

fake = Faker('ru_RU')

print(fake.name()) # Выведет: Иван Иванов
print(fake.address())  # Выведет: ул. Пушкина, дом 10
print(fake.email())

# Генерация фейковых данных
data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}
