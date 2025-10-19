import os
import time
import allure
from registration_form import RegistrationFormPage


def test_sending_form(in_browser):
    browser = in_browser

    register_page = RegistrationFormPage(in_browser)
    with allure.step("open registration page"):
        register_page.open("/automation-practice-form")
    with allure.step("filling personal information"):
        register_page.fill_name("Daniil")
        register_page.fill_surname("Zhuravlev")
        register_page.fill_email("butmanovich@yandex.ru")
        register_page.fill_number("3123131232")
        register_page.choose_gender(1)
        register_page.fill_date_of_birth('2002', 'May', '11')
    with allure.step("filling other info"):
        register_page.choose_subject("Computer Science")
        register_page.choose_hobby()
    # register_page.choose_photo('123123.png')
    with allure.step("filling address information"):
        register_page.fill_address('Moskva, street 10')
        register_page.choose_state('NCR')
        register_page.choose_city('Delhi')
    with allure.step("sending form"):
        register_page.submit_form()
    with allure.step("check if registration form is working"):
        time.sleep(2)
        register_page.should_registered_student_with(
            "Daniil Zhuravlev",
            "butmanovich@yandex.ru",
            "Male",
            "3123131232",
            "11 May,2002",
            'Computer Science',
            'Sports',
            '',
            'Moskva, street 10',
            'NCR',
            'Delhi'
        )
        time.sleep(2)
        browser.element('#closeLargeModal').click()
