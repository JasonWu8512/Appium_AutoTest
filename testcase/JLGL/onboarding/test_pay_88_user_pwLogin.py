import allure


@allure.feature("登录")
class TestLogin:

    def test_pay_88_user_pwLogin(self, onboarding_page):
        onboarding_page.pay_88_user_pwLogin()
        onboarding_page.get_home_notification()
        onboarding_page.result_assert(onboarding_page.get_home_text(), "首页")
