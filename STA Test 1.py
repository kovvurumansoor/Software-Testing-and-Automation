from faker import Faker

fake_data = Faker()

for i in range(5):
    print(fake_data.name())
    print(fake_data.email())
    print(fake_data.password())