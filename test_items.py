from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    # Открываем страницу указанного товара
    browser.get(link)

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), "Button 'Add to Basket' is not found or invisible"