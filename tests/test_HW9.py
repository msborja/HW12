from demo_qa_tests.pages.registration_page import RegistrationPage

def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Boris')
    registration_page.fill_last_name('Shark')

    registration_page.fill_email('examplemail@mail.com')

    registration_page.pick_gender()

    registration_page.fill_mobile_phone('2911011214')

    registration_page.fill_birthday('1998', '2', '24')

    registration_page.pick_subject('Ma', 'Ph')

    registration_page.pick_hobbies()

    registration_page.set_picture('photo.jpeg')

    registration_page.fill_address('Republic of Belarus, Minsk')

    registration_page.pick_state_and_city()

    registration_page.click_submit()

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
