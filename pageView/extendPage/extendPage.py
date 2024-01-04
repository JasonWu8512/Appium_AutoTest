import time

import allure

from appium.webdriver.common.mobileby import MobileBy
from pageView.basePage import BasePage
from data.testData import ExtendPageData


class ExtendPage(BasePage):
    expend_tab_btn = ExtendPageData.expend_tab_btn
    week_song_btn = ExtendPageData.week_song_btn
    song_btn = ExtendPageData.song_btn
    vocabulary_btn = ExtendPageData.vocabulary_btn
    daily_spoken_btn = ExtendPageData.daily_spoken_btn
    story_btn = ExtendPageData.story_btn
    video_or_song_btn = ExtendPageData.video_or_song_btn
    change_to_video_btn = ExtendPageData.change_to_video_btn
    week_song_back_btn = ExtendPageData.week_song_back_btn
    # song_back_btn = ExtendPageData.song_back_btn
    song_back_btn = ExtendPageData.song_back_btn
    vocabulary_close_btn = ExtendPageData.vocabulary_close_btn
    daily_spoken_back_btn = ExtendPageData.daily_spoken_back_btn
    full_album_back_btn = ExtendPageData.full_album_back_btn
    full_album_btn = ExtendPageData.full_album_btn

    extend_title_text = ExtendPageData.extend_title_text

    view_more_tip = ExtendPageData.view_more_tip

    def extendTab(self):
        with allure.step("首页，点击拓展Tab"):
            self.click_element(*self.expend_tab_btn, doc="点击拓展Tab")

    def extend_week_song(self):
        with allure.step("拓展Tab，点击每周儿歌"):
            self.click_element(*self.week_song_btn, doc="点击每周儿歌")
        with allure.step("每周儿歌，音视频切换按钮"):
            self.click_element(*self.video_or_song_btn, doc="音视频切换按钮")
        with allure.step("每周儿歌，切换到视频"):
            self.click_element(*self.change_to_video_btn, doc="切换到视频")
        with allure.step("每周儿歌，点击返回"):
            self.click_element(*self.week_song_back_btn, doc="点击返回")

    def extend_songs(self):
        with allure.step("拓展Tab，点击儿歌"):
            self.click_element(*self.song_btn, doc="点击儿歌")
        time.sleep(2)
        with allure.step("儿歌，点击返回"):
            self.click_element(*self.song_back_btn, doc="点击返回")

    def extend_vocabulary(self):
        with allure.step("拓展Tab，点击词汇"):
            self.click_element(*self.vocabulary_btn, doc="点击词汇")
        with allure.step("词汇，关闭列表"):
            try:
                self.click_element(*self.vocabulary_close_btn, doc="关闭列表")
            finally:
                pass
        with allure.step("词汇，点击返回"):
            self.click_element(*self.song_back_btn, doc="点击返回")

    def extend_daily_spoken(self):
        with allure.step("拓展Tab，点击每日口语"):
            self.click_element(*self.daily_spoken_btn, doc="点击每日口语")
        with allure.step("每日口语，点击返回"):
            self.click_element(*self.daily_spoken_back_btn, doc="点击返回")

    def extend_story(self):
        with allure.step("拓展Tab，点击故事汇"):
            self.click_element(*self.story_btn, doc="点击故事汇")
        time.sleep(2)
        with allure.step("故事汇，点击返回"):
            self.click_element(*self.song_back_btn, doc="点击返回")

    def extend_full_album(self):
        with allure.step("拓展Tab，点击全部专辑"):
            self.click_element(*self.full_album_btn, doc="点击全部专辑")
        with allure.step("专辑，点击返回"):
            self.click_element(*self.full_album_back_btn, doc="点击返回")

    def get_extend_title_text(self):
        with allure.step("获取拓展Tab标题"):
            return self.get_text(*self.extend_title_text, doc="获取标题")
