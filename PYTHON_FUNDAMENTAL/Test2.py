from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set Chrome options to specify the download folder
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/sanjaybiswas/Downloads",  # Change this path as needed
    "download.prompt_for_download": False,
    "directory_upgrade": True
})

# Set up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open NSE website
driver.get("https://www.nseindia.com/market-data/live-equity-market")
time.sleep(5)  # Wait for the page to load

# Locate and click the CSV download button (Update the XPath if needed)
try:
    download_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Download')]")
    download_button.click()
    print("Download started...")
except Exception as e:
    print("Download button not found:", e)

# Wait for a few seconds to ensure download completion
time.sleep(10)

# Close the browser
driver.quit()
print("Download completed!")