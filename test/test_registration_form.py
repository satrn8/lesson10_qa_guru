from demoqa_tests import manager
import allure
from utils.attach import add_html, add_screenshot, add_logs, add_video


@allure.description('Test sign up form')
@allure.title("Successful fill form")
@allure.tag('UI')
def test_registration_form(setup_browser):
    browser = setup_browser

    with allure.step("Open page"):
        manager.open_form_page("/automation-practice-form")

    with allure.step("Form"):
        (manager.form
         .set_first_name("Alyona")
         .set_last_name("Tch")
         .set_email("verypyc@gmail.com")
         .set_gender("Female")
         .set_number("9998889988")
         .set_date_birth(1992, 7, 27)
         .set_subjects("Maths")
         .set_hobbies("Reading")
         .set_picture("pepe.png")
         .set_address("Moscow")
         .set_states("NCR")
         .set_cities("Gurgaon")
         .set_submit())

    with allure.step("Result"):
        manager.result.name.should_have("Alyona Tch")
        manager.result.email.should_have("verypyc@gmail.com")
        manager.result.gender.should_have("Female")
        manager.result.number.should_have("9998889988")
        manager.result.date_of_birth.should_have("27 July,1992")
        manager.result.subjects.should_have("Maths")
        manager.result.hobbies.should_have("Reading")
        manager.result.picture.should_have("pepe.png")
        manager.result.address.should_have("Moscow")
        manager.result.cities.should_have("NCR Gurgaon")

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
    add_video(browser)
