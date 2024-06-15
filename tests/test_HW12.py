from demo_qa_tests.pages.registration_page import RegistrationPage
import allure


def test_student_registration_form():
    with allure.step('Открываем главную страницу'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('Заполняем поля First name и Last name'):
        registration_page.fill_first_name('Boris')
        registration_page.fill_last_name('Shark')

    with allure.step('Заполняем поле Email'):
        registration_page.fill_email('examplemail@mail.com')

    with allure.step('Нажимаем радиокнопку Gender'):
        registration_page.pick_gender()

    with allure.step('Заполяем поле Mobile'):
        registration_page.fill_mobile_phone('2911011214')

    with allure.step('Заполняем поле Date of Birth'):
        registration_page.fill_birthday('1998', '2', '24')

    with allure.step('Заполняем поле Subjects'):
        registration_page.pick_subject('Ma', 'Ph')

    with allure.step('Выбираем чек-боксы Hobbies'):
        registration_page.pick_hobbies()

    with allure.step('Вставляем картинку в поле Picture'):
        registration_page.set_picture('photo.jpeg')

    with allure.step('Заполняем поле Current Address'):
        registration_page.fill_address('Republic of Belarus, Minsk')

    with allure.step('Выбираем State и City в выпадающих списках'):
        registration_page.pick_state_and_city()

    with allure.step('Нажимаем кнопку Submit'):
        registration_page.click_submit()

    with allure.step('Проверяем заполнение формы'):
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
