from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(1)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get("https://www.instagram.com/urlDaFotoDeComentario/")
        time.sleep(5)   
        self.abrir_paginafoto_comentar()

    @staticmethod

    def type_like_a_person(sentence, where_to_type):
        for letter in sentence:
            where_to_type.send_keys(letter)
            time.sleep(random.randint(1, 3) / 15)

    def abrir_paginafoto_comentar(self):
        driver = self.driver
        

        counter = 0
        try:

            while(counter <= 3):
                counter = counter + random.randint(1, 2)
                if counter <= 3:
                    comments = [
                    "Que foto massa.",
                    "Muito legal",
                    "Que click",
                    "Espetacular",
                    "Demais, parabéns"
                    ]  

                    time.sleep(random.randint(5, 10))
                    driver.find_element_by_class_name("Ypffh").click()
                    comment_input_box = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(1, 3))
                    self.type_like_a_person(random.choice(comments), comment_input_box)
                    time.sleep(random.randint(1, 3))
                    driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                    time.sleep(random.randint(5, 10))
            
                else:
                    print("+ 1 Loops")

                    new_url = random.choice([
                    "https://www.instagram.com/xxx/",
                    "https://www.instagram.com/xxx/",
                    "https://www.instagram.com/xxx/",
                    "https://www.instagram.com/xxx/",
                    "https://www.instagram.com/xxx/",
                    "https://www.instagram.com/xxx/"]
                    )

                    driver.get(new_url)  

                    time.sleep(random.randint(30, 120))                  
                    driver.get("https://www.instagram.com/urlDaFotoDeComentario/")
                    time.sleep(random.randint(900, 1500))                     
                    self.abrir_paginafoto_comentar()

        except:
            print("-----------VERIFICAR--------------")            
            time.sleep(random.randint(900, 1500))
            self.abrir_paginafoto_comentar()

                


Bot = InstagramBot("yourUser", "yourPassword")
Bot.login()
