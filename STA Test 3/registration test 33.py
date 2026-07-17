from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

fake = Faker()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(r"C:\Users\Lenovo\PycharmProjects\Software Testing and Automation\registration test 3.html")

driver.maximize_window()

# Generate valid data
name = fake.name()
email = fake.email()
password = fake.password(length=10)

# Fill the form
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)

# Click Register
driver.find_element(By.ID, "register").click()

# Verify success message
success = driver.find_element(By.ID, "success-message").text

if success == "Registration Successful":
    print("✅ Registration Test Passed")
else:
    print("❌ Registration Test Failed")

input("Press Enter to close...")

driver.quit()