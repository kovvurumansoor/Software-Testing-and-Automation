from faker import Faker
from openpyxl import Workbook

fake = Faker()

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "ContactData"

# Heading
ws.append(["Name", "Email", "Subject", "Message"])

# Fake Data
name = fake.name()
email = fake.email()
subject = fake.sentence(nb_words=3)
message = fake.paragraph()

# Write data
ws.append([name, email, subject, message])

# Save Excel
wb.save("ContactData.xlsx")

print("ContactData.xlsx created successfully.")