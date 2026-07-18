from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Shopping Cart HTML (change the path if needed)
driver.get(r"C:\Users\Lenovo\PycharmProjects\Software Testing and Automation\STA Test 4\shopping cart.html")

driver.maximize_window()
time.sleep(2)

# -------------------------
# Add Laptop
# -------------------------
driver.find_element(By.ID, "addLaptop").click()
time.sleep(1)

# Add Mobile
driver.find_element(By.ID, "addMobile").click()
time.sleep(1)

# Verify first total
total = driver.find_element(By.ID, "total").text

if total == "Total: ₹70000":
    print("✅ Multiple Products Added Successfully")
    print("✅ Cart Total Verified")
else:
    print("❌ Cart Total Incorrect:", total)

# -------------------------
# Update Laptop Quantity
# -------------------------
qty = driver.find_element(By.ID, "laptopQty")
qty.clear()
qty.send_keys("2")

driver.find_element(By.ID, "updateCart").click()
time.sleep(1)

# Verify updated total
updated_total = driver.find_element(By.ID, "total").text

if updated_total == "Total: ₹120000":
    print("✅ Quantity Updated Successfully")
    print("✅ Updated Total Verified")
else:
    print("❌ Updated Total Incorrect:", updated_total)

print("\n🎉 Shopping Cart Test Passed")

input("Press Enter to close...")

driver.quit()
