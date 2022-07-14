import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class TestLambdaSteps:

    def test_lambda_steps(self):

        with allure.step('Open page eroshenkoam/allure-example'):
            browser.open('eroshenkoam/allure-example')
        with allure.step('Issue tab should be visible'):
            s("#issues-tab").should(be.visible)
        with allure.step('Click on issue tab'):
            s("#issues-tab").click()
        with allure.step('Assert that issue №76 is visible'):
            s(by.partial_text("#76")).should(be.visible)
