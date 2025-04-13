from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier
import time

# --- Setup ---
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 10)
toaster = ToastNotifier()

time.sleep(2)

# --- Login ---
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
time.sleep(3)

# --- Navigate to PIM ---
pim_menu = driver.find_element(By.XPATH, "//span[text()='PIM']")
ActionChains(driver).move_to_element(pim_menu).click().perform()
time.sleep(3)

# --- Add Employees ---
employees = [("John", "Doe"), ("Alice", "Smith"), ("Bob", "Williams")]

for first, last in employees:
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first)
    driver.find_element(By.NAME, "lastName").send_keys(last)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
    time.sleep(3)

# --- Go to Employee List ---
pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
pim_menu.click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List"))).click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-body")))
time.sleep(3)

# --- Scroll and Verify Employees in the Table (with retries and toast) ---
for first, last in employees:
    full_name = f"{first} {last}"
    print(f"\n🔍 Searching for: {full_name}")
    found = False

    for attempt in range(3):  # Retry loop
        print(f"Attempt {attempt + 1}...")
        time.sleep(3)

        rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[contains(@class, 'oxd-table-row')]")

        for row in rows:
            row_text = row.text.lower()
            if first.lower() in row_text and last.lower() in row_text:
                print(f"✅ Name Verified: {full_name}")
                toaster.show_toast("Employee Verified", f"{full_name} was found.", duration=5, threaded=True)
                found = True
                break

        if found:
            break
        else:
            print("🔄 Refreshing the page to retry...")
            driver.refresh()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-body")))
            time.sleep(3)

    if not found:
        print(f"❌ Name Not Found After Retry: {full_name}")

# --- Logout ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
time.sleep(2)
driver.quit()
