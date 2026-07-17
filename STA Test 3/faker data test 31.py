from faker import Faker

fake = Faker()

print("Name :", fake.name())
print("Email :", fake.email())
print("Subject :", fake.sentence(nb_words=3))
print("Message :", fake.paragraph())