from selenium import webdriver


class BaseClass:
    driver=""
    @staticmethod
    def open_browser():
        BaseClass.driver = webdriver.Chrome(executable_path="C:\\Users\\JANU\\PycharmProjects\\pythonProject\\chromedriver\\chromedriver.exe")
        BaseClass.driver.maximize_window()
