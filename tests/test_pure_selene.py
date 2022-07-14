from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class TestPureSelene:

    def test_pure_selene(self):

        browser.open('eroshenkoam/allure-example')
        s("#issues-tab").should(be.visible)
        s("#issues-tab").click()
        s(by.partial_text("#76")).should(be.visible)
