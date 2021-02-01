link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_element_present(browser):

    browser.implicitly_wait(10)
    browser.get(link)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, "button not found"  