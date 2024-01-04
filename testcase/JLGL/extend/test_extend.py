import time
import allure


@allure.feature("拓展tab")
class TestExpendTab:

    def test_extend(self, extend_page, onboarding_page):
        onboarding_page.no_pay_user_pwLogin()
        onboarding_page.get_home_notification()
        extend_page.extendTab()
        extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    def test_week_song(self, extend_page):
        extend_page.extend_week_song()
        time.sleep(2)
        extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    # def test_songs(self, extend_page):
    #     extend_page.extend_songs()
    #     time.sleep(2)
    #     extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    def test_vocabulary(self, extend_page):
        extend_page.extend_vocabulary()
        time.sleep(2)
        extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    def test_daily_spoken(self, extend_page):
        extend_page.extend_daily_spoken()
        time.sleep(2)
        extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    # def test_story(self, extend_page):
    #     extend_page.extend_story()
    #     time.sleep(2)
    #     extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")

    def test_full_album(self, extend_page):
        extend_page.extend_full_album()
        time.sleep(2)
        extend_page.result_assert(extend_page.get_extend_title_text(), "拓展资源")
