from selene import browser, have, be
from demo_qa_tests.pages import registration_form
from demo_qa_tests.pages.registration_form import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    # Открываем форму регистрации
    registration_page.open()

    # Заполнение полей FirstName и LastName
    registration_page.fill_first_name('Boris')
    registration_page.fill_last_name('Shark')

    # Заполнение поля Email
    registration_page.fill_email('examplemail@mail.com')

    # Выбор радио-кнопки для поля Gender
    registration_page.pick_gender()

    # Заполнение поля Mobile
    registration_page.fill_mobile_phone('2911011214')

    # Заполнение поля Date of Birth
    registration_page.fill_birthday('1998', '2', '24')

    # Заполнение поля Subjects
    registration_page.pick_subject('Ma', 'Ph')

    # Выбор чек-боксов для поля Hobbies
    registration_page.pick_hobbies()

    # Выбор файла для поля Picture
    registration_page.set_picture('photo.jpeg')

    # Заполнение поля Current Address
    registration_page.fill_address('Republic of Belarus, Minsk')

    # Выбор значений в выпадающих списках State и City
    registration_page.pick_state_and_city()

    # Submit
    registration_page.click_submit()

    # Проверки
    registration_page.assert_submit_user_info(
        'Boris Shark',
        'examplemail@mail.com',
        'Male',
        '2911011214',
        '24 March,1998',
        'Maths, Physics',
        'Sports, Reading',
        'photo.jpeg',
        'Republic of Belarus, Minsk',
        'Rajasthan Jaipur')
