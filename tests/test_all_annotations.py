import json

import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure import attachment_type


class TestAllAnnotations:

    @allure.link("https://github.com", name="QA GURU 7 Lesson")
    @allure.label("owner", "uraniumcore238")
    @allure.severity('Blocker')
    @allure.story('Checking visibility issue number')
    def test_all_annotations(self):
        allure.dynamic.feature("Задачи в репозитории")
        allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)
        allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
        allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)

        with allure.step('Open page eroshenkoam/allure-example'):
            browser.open('eroshenkoam/allure-example')
        with allure.step('Issue tab should be visible'):
            s("#issues-tab").should(be.visible)
        with allure.step('Click on issue tab'):
            s("#issues-tab").click()
        with allure.step('Assert that issue №76 is visible'):
            s(by.partial_text("#76")).should(be.visible)
