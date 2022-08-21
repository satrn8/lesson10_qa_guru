import time
from selene import command
from selene.support.conditions import have
from selene.support.shared import browser
from demoqa_tests.student_registration_form import StudentRegistrationForm, Registration
from demoqa_tests.controls.table import Table
from utils import attach


form = StudentRegistrationForm()
result = Registration()


def open_form_page(url: str):
    browser.open(url)
    time.sleep(1)
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]') \
        .with_(timeout=10).should(have.size_greater_than_or_equal(3)) \
        .perform(command.js.remove)
