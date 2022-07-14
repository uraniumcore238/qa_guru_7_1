import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class TestDecorators:

    @allure.step('Open page eroshenkoam/allure-example')
    def open_page(self):
        browser.open('eroshenkoam/allure-example')

    @allure.step('Issue tab should be visible')
    def check_visibility(self):
        s("#issues-tab").should(be.visible)

    @allure.step('Click on issue tab')
    def click_on_issue(self):
        s("#issues-tab").click()

    @allure.step('Assert that issue №76 is visible')
    def assert_text(self):
        s(by.partial_text("#76")).should(be.visible)

    def test_decorators(self):
        self.open_page()
        self.check_visibility()
        self.click_on_issue()
        self.assert_text()
