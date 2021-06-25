from browser import Browser



class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)

    def clk_get(self):
        self.driver.find_element_by_xpath('//*[@id="operations-user-getUserByName"]/div/span[1]').click()

    def clk_try(self):
        self.driver.find_element_by_xpath(
            '//*[@id="operations-user-getUserByName"]/div[2]/div/div[1]/div[1]/div[2]/button').click()

    def preenche_nome(self, nome):
        self.driver.find_element_by_xpath(
            '//*[@id="operations-user-getUserByName"]/div[2]/div/div[1]/div[2]/div/table/'
            'tbody/tr/td[2]/input').send_keys(nome)

    def clk_execute(self):
        self.driver.find_element_by_xpath('//*[@id="operations-user-getUserByName"]/div[2]/div/div[2]/button').click()
