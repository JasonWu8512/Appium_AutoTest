import allure


@allure.feature("登录")
class TestLogin:

    def test_guest_login(self, onboarding_page):
        onboarding_page.guestLogin()
        # onboarding_page.result_assert(onboarding_page.home_popup_close(), True, "首页弹窗")
