from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

fake = Faker()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(r"file:///C:/Users/Lenovo/PycharmProjects/Software%20Testing%20and%20Automation/login.html")

driver.maximize_window()

# Generate invalid credentials
username = fake.user_name()
password = fake.password()

print("Username:", username)
print("Password:", password)

# Enter invalid credentials
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# Click Login
driver.find_element(By.ID, "login").click()

# Verify error message
error = driver.find_element(By.ID, "error-message").text

if error == "Invalid Username or Password":
    print("✅ Test Passed")
else:
    print("❌ Test Failed")

input("Press Enter to close the browser...")

driver.quit()