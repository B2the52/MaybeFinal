import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        user = "Sikari"
        pwd = "Jollywax3."
        driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(3)
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        try:
            # verify Book List exists on new screen after clicking "All books" button
            # note that this test requires at least one book in the database to be successful
            elem = driver.find_element(By.ID, "id_username")
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("User is authorized")


time.sleep(2)


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()