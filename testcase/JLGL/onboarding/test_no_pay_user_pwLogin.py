import allure


@allure.feature("登录")
class TestLogin:

    def test_no_pay_user_pwLogin(self, onboarding_page):
        onboarding_page.no_pay_user_pwLogin()
        onboarding_page.get_home_notification()
        onboarding_page.close_home_banner()
        onboarding_page.result_assert(onboarding_page.get_level_title_text(), "当前级别：K1")
