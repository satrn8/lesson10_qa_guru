from selene.support.shared import browser
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.resource import resource
from selene import command, have
from selene.support.shared.jquery_style import s

from demoqa_tests.controls.table import Table


class StudentRegistrationForm:
    def set_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def set_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def set_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def set_gender(self, value):
        browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text(value)).click()
        return self

    def set_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def set_date_birth(self, year: str, month: int, day: 'str'):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').s(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').s(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()
        return self

    def set_subjects(self, *values):
        for value in values:
            s('#subjectsInput').set_value(value).press_enter()
        return self

    def set_hobbies(self, *values):
        for value in values:
            s('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def set_picture(self, value):
        browser.element("#uploadPicture").send_keys(resource(value))
        return self

    def set_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def set_states(self, value):
        state = Dropdown(browser.element("#state"))
        state.select(option="NCR")
        return self

    def set_cities(self, value):
        city = Dropdown(browser.element("#city"))
        city.select(option="Gurgaon")
        return self

    def set_submit(self):
        s('#submit').perform(command.js.click)


class Registration:
    def __init__(self):
        self.name = Table(0)
        self.email = Table(1)
        self.gender = Table(2)
        self.number = Table(3)
        self.date_of_birth = Table(4)
        self.subjects = Table(5)
        self.hobbies = Table(6)
        self.picture = Table(7)
        self.address = Table(8)
        self.cities = Table(9)