from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open HTML file (change this path if needed)
driver.get(r"C:\Users\Lenovo\PycharmProjects\Software Testing and Automation\STA Test 4\product filter.html")

driver.maximize_window()
time.sleep(2)

# Dropdown
dropdown = Select(driver.find_element(By.ID, "category"))

# Expected products for each category
expected = {
    "electronics": ["Laptop", "Mobile"],
    "clothing": ["T-Shirt", "Jeans"],
    "books": ["Python Book", "Java Book"]
}

# Test each category
for category, expected_products in expected.items():

    dropdown.select_by_value(category)
    time.sleep(1)

    visible_products = []

    products = driver.find_elements(By.CLASS_NAME, "product")

    for product in products:
        if product.is_displayed():
            visible_products.append(product.find_element(By.TAG_NAME, "h3").text)

    if visible_products == expected_products:
        print(f"✅ {category.capitalize()} Filter Passed")
    else:
        print(f"❌ {category.capitalize()} Filter Failed")
        print("Expected:", expected_products)
        print("Found:", visible_products)

print("\n🎉 Product Filtering Test Completed")

input("Press Enter to close...")

driver.quit()