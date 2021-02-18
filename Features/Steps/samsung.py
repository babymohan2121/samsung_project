from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.Steps.Initilizer.initilizer import BaseClass


@Given ('open browser as "{BROWSER}"')
def openbrowser(context,BROWSER):
    print("browser is opened successfully",BROWSER)
    BaseClass.open_browser()

@When ('enter URl as "{URL}"')
def enter_google_page_URL(context,URL):
    print("URL is entered successfully",URL)
    BaseClass.driver.get(URL)


@When ('type amazon in input box')
def input(context):
    BaseClass.driver.find_element(By.NAME,'q').send_keys("amazon")

@When ('click submit button')
def click_submit(context):
    BaseClass.driver.find_element(By.NAME,'q').submit()

@When ('click amazon Link')
def click_amazon_link(context):
    sample=BaseClass.driver.find_element(By.PARTIAL_LINK_TEXT,'Amazon.in')
    sample.click()

@When ('type Samsung mobile')
def input(context):
    BaseClass.driver.find_element(By.ID,'twotabsearchtextbox').send_keys("Samsung Mobile")

@When('click search button')
def click_search(context):
        BaseClass.driver.find_element(By.ID,'twotabsearchtextbox').submit()

@Then ('verify the samsung mobile page is successsfully opened')
def verify(context):
    print("verified successfully")

@When ('click first link of samsung product')
def click_first_link_of_samsung_product(context):
    BaseClass.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[1]/div/span/div/div/div[1]/div[1]/div/div[2]/div/a/span/span[2]').click()

@When ('click AddtoCart')
def AddtoCart(context):
    #BaseClass.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #BaseClass.driver.execute_script('arguments[0].scrollIntoView():')
    #BaseClass.driver.execute_script('window.scrollBy(o,100)')

    #cart=BaseClass.driver.find_element(By.PARTIAL_LINK_TEXT,'add-to-cart-button')
   # BaseClass.driver.execute_script('arguments[0].scrollIntoView();',cart)
    cart=BaseClass.driver.find_element(By.TAG_NAME,'button').click()
    BaseClass.driver.execute_script('arguments[0].scrollIntoView();',cart)
