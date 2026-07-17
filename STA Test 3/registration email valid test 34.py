from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

fake = Faker()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(r"file:///C:/Users/Lenovo/PycharmProjects/Software%20Testing%20and%20Automation/registration%20test%203.html")

driver.maximize_window()

# Fill valid name
driver.find_element(By.ID, "name").send_keys(fake.name())

# Enter INVALID email
email = driver.find_element(By.ID, "email")
email.send_keys("mansoorgmail.com")      # Missing @

# Password
driver.find_element(By.ID, "password").send_keys("Admin@123")

# Click Register
driver.find_element(By.ID, "register").click()

# Check HTML5 validation message
validation = email.get_attribute("validationMessage")

if validation:
    print("✅ Email format validation is working.")
    print("Validation Message:", validation)
else:
    print("❌ Email validation failed.")

input("Press Enter to close...")

driver.quit()