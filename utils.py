
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)

    def clk_get(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="operations-user-getUserByName"]/div/span[1]')))
        element.click()

    def clk_try(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="operations-user-getUserByName"]/div[2]/div/div[1]/div[1]/div[2]/button')))
        element.click()

    def preenche_nome(self, nome):
        self.driver.find_element_by_xpath(
            '//*[@id="operations-user-getUserByName"]/div[2]/div/div[1]/div[2]/div/table/'
            'tbody/tr/td[2]/input').send_keys(nome)

    def clk_execute(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="operations-user-getUserByName"]/div[2]/div/div[2]/button')))
        element.click()

    def resposta(self):
        element = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="operations-user-getUserByName"]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/pre'))).text
        return element
