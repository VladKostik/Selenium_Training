from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


def test_nova_poshta():
    browser = webdriver.Chrome('drivers/chromedriver')
    browser.implicitly_wait(1)
    browser.maximize_window()
    actions = ActionChains(browser)

    office_link_locator = '//ul/li/a[@href="/office"]'
    office_list_locator = '//ul/li/a[@href="/office/list"]'
    city_filter_locator = '// div / input[ @ id = "oCityFilter"]'
    odessa_city_locator = '//div/ul[@class="list drop-down-ul map"]/li[1]'
    warehouse_filter_locator = '//div/input[@id="oWarehouseFilter"]'
    warehouse_42_locator = '//div/ul/li[' \
                                      '@data-warehouse-number="42"]'

    browser.get('https://novaposhta.ua/')

    office_link_element: WebElement = \
        browser.find_element_by_xpath(office_link_locator)
    office_link_element.click()

    office_list_element: WebElement = \
        browser.find_element_by_xpath(office_list_locator)
    office_list_element.click()

    city_filter_element: WebElement = \
        browser.find_element_by_xpath(city_filter_locator)
    city_filter_element.send_keys('одесса')

    odessa_city_element: WebElement = \
        browser.find_element_by_xpath(odessa_city_locator)
    odessa_city_element.click()

    warehouse_filter_element: WebElement = \
        browser.find_element_by_xpath(warehouse_filter_locator)
    warehouse_filter_element.click()

    warehouse_42_element: WebElement = \
        browser.find_element_by_xpath(warehouse_42_locator)
    actions.move_to_element(warehouse_42_element).perform()
    warehouse_42_element.click()
