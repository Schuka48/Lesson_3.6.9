import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)

    assert is_elemnt_present(browser), "Кнопка добавить в корзину отсутствует"

def is_elemnt_present(browser):
    try:
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector("div.product_main button[type='submit']")
        return True
    except:
        return False