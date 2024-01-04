import time
import allure


@allure.feature("购买tab")
class TestPayTab:

    def test_how_use_banner(self, onboarding_page, pay_base_page):
        onboarding_page.guestLogin()
        pay_base_page.payTab()
        pay_base_page.pay_how_use()
        pay_base_page.result_assert(pay_base_page.get_pay_how_use_text(), True, "如何使用")
        pay_base_page.payActionBack()

    def test_guest_pay_0_banner(self, setup, guest_pay_page, pay_base_page):
        pay_base_page.pay_swipe_up(setup)
        guest_pay_page.result_assert(guest_pay_page.guestPayBanner(), "0元英语启蒙体验营")
        guest_pay_page.result_assert(guest_pay_page.guestPayBanner(), "0")
        # guest_pay_page.payBack()
