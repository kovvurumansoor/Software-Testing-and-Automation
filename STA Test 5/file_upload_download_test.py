from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import time

# ----------------------------
# Project Folder
# ----------------------------
project_path = r"C:\Users\Lenovo\PycharmProjects\Software Testing and Automation\STA Test 5"

download_folder = os.path.join(project_path, "downloads")

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# ----------------------------
# Chrome Options
# ----------------------------
options = Options()

prefs = {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ----------------------------
# Open HTML
# ----------------------------
driver.get(
    "file:///" + project_path.replace("\\", "/") + "/file_upload_download.html"
)

driver.maximize_window()
time.sleep(2)

# ----------------------------
# Valid File Upload
# ----------------------------
valid_file = os.path.join(project_path, "valid_file.pdf")

driver.find_element(By.ID, "fileInput").send_keys(valid_file)

driver.find_element(By.ID, "uploadBtn").click()

time.sleep(1)

message = driver.find_element(By.ID, "message").text

if message == "File uploaded successfully!":
    print("✅ Valid File Upload Passed")
else:
    print("❌ Valid File Upload Failed")

# ----------------------------
# Invalid File Upload
# ----------------------------
driver.refresh()
time.sleep(1)

invalid_file = os.path.join(project_path, "invalid_file.txt")

driver.find_element(By.ID, "fileInput").send_keys(invalid_file)

driver.find_element(By.ID, "uploadBtn").click()

time.sleep(1)

message = driver.find_element(By.ID, "message").text

if message == "Unsupported file format!":
    print("✅ Invalid File Rejected")
else:
    print("❌ Invalid File Test Failed")

# ----------------------------
# Download File
# ----------------------------
driver.find_element(By.ID, "downloadLink").click()
time.sleep(2)

print("✅ Download Button Clicked Successfully")

print("\n🎉 Question 51 Completed Successfully")

input("Press Enter to close...")

driver.quit()