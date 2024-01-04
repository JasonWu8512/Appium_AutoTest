import time

import allure


@allure.feature("登录")
class TestLogin:

    def test_y_user_pwLogin(self, setup, onboarding_page, home_page):
        onboarding_page.y_user_pwLogin()
        onboarding_page.get_home_notification()
        home_page.home_swipe_down(setup)
        onboarding_page.open_level_change()
        onboarding_page.result_assert(onboarding_page.get_year_level_title_text(), "当前级别:Y1")




