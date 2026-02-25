from selenium import webdriver
from selenium.webdriver.common.by import By
# מנגנון המתנה
from selenium.webdriver.support.ui import WebDriverWait # מאפשר לסלניום לחכות עד שדף יטען כדי להמנע משגיאות
#תנאי המתנה
from selenium.webdriver.support import expected_conditions as EC # רשימת תנאים מוכנים מראש של לחכות עד שדברים יעבדו ולא יקפצו שגיאות
def test_login_success():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        # fill username + password
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # click login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # verify success message
        flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "You logged into a secure area!" in flash.text

        print("✅ Login success test passed")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_success()

