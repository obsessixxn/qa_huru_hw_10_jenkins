import os
import time

from selene import browser, have
from selene.support.shared import browser

from registration_form import RegistrationFormPage


def test_sending_form(in_browser):
    browser = in_browser

    register_page = RegistrationFormPage(in_browser)
    register_page.open("/automation-practice-form")
    register_page.fill_name("Daniil")
    register_page.fill_surname("Zhuravlev")
    register_page.fill_email("butmanovich@yandex.ru")
    register_page.choose_gender(1)
    register_page.fill_number("3123131232")
    register_page.fill_date_of_birth('2002', 'May', '11')
    register_page.choose_subject("Computer Science")
    register_page.choose_hobby()
    register_page.choose_photo('123123.png')
    register_page.fill_address('Moskva, street 10')
    register_page.choose_state('NCR')
    register_page.choose_city('Delhi')
    register_page.submit_form()
    register_page.should_registered_student_with(
        "Daniil Zhuravlev",
        "butmanovich@yandex.ru",
        "Male",
        "3123131232",
        "11 May,2002",
        'Computer Science',
        'Sports',
        '123123.png',
        'Moskva, street 10',
        'NCR',
        'Delhi'
    )

    browser.element('#closeLargeModal').click()
    time.sleep(2)