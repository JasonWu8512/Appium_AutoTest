from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class OnboardingPageData:
    home_tab_btn = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view'
                                    '.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup['
                                    '1]/android.widget.LinearLayout/android.widget.TextView')
    agree_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/tv_agree')
    secret_login_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/to_secret_login')
    pw_login_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/secret_login')
    checkBox_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_checkBox')
    more_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/more')
    youke_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/ll_youke')
    startLearn_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/start_learn')
    limitedTime_btn1 = (MobileBy.ID, 'com.jiliguala.niuwa:id/showImage')
    limitedTime_btn2 = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_operation_float_window')
    limitedTime__close_btn3 = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_close')
    level_change_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/txt_schedule')

    # 输入框&文本定位
    mobile_input = (MobileBy.ID, 'com.jiliguala.niuwa:id/account_input')
    pw_input = (MobileBy.ID, 'com.jiliguala.niuwa:id/secret_input')
    schedule_text = (MobileBy.ID, 'com.jiliguala.niuwa:id/txt_schedule')
    year_level_title_text = (MobileBy.ID, 'com.jiliguala.niuwa:id/levelTV')
    level_title_text = (MobileBy.ID, 'com.jiliguala.niuwa:id/level_title')

    # 通知权限
    alwaysAllow_btn1 = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                        '.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]')
    alwaysAllow_btn2 = (MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')


class HomePageData:
    alwaysAllow_btn1 = (MobileBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                        '.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]')
    alwaysAllow_btn2 = (MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    limitedTime_btn1 = (MobileBy.ID, 'com.jiliguala.niuwa:id/showImage')
    limitedTime_btn2 = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_operation_float_window')


class PayPageData:
    pay_tab_btn = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                   '.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android'
                                   '.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup['
                                   '2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView')
    pay_btn = (By.ID, 'com.jiliguala.niuwa:id/btn_purchase')
    pw_login_link = (MobileBy.ID, 'com.jiliguala.niuwa:id/tv_change_to_password')
    pw_login_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/tv_passport_login')
    limitedTime_btn1 = (MobileBy.ID, 'com.jiliguala.niuwa:id/showImage')
    limitedTime_btn2 = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_operation_float_window')
    pay_back_btn1 = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_buy_back')
    pay_back_btn2 = (MobileBy.ID, 'com.jiliguala.niuwa:id/action_back')
    pay_how_use_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/ll_buy_how_use')
    banner_group_btn1 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget'
                                         '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                                         '.ViewGroup[1]')
    banner_group_btn2 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget'
                                         '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                                         '.ViewGroup[2]')
    banner_group_btn3 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget'
                                         '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                                         '.ViewGroup[3]')

    banner_group_btn4 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget'
                                         '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                                         '.ViewGroup[4]')
    banner_group_btn5 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android'
                                         '.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                         '/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget'
                                         '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view'
                                         '.ViewGroup[5]')

    parent_lock_text = (MobileBy.ID, 'com.jiliguala.niuwa:id/tv_parent_lock_title')
    pay_title_text = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                '.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    pay_price_text = (By.ID, 'com.jiliguala.niuwa:id/price')
    pay_how_use_text = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout'
                                        '/android.webkit.WebView/android.webkit.WebView')

    mobile_input = (MobileBy.ID, 'com.jiliguala.niuwa:id/et_phone_passport_input')
    pw_input = (MobileBy.ID, 'com.jiliguala.niuwa:id/et_passport_input')


class ExtendPageData:
    expend_tab_btn = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                      '.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view'
                                      '.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup['
                                      '3]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView')
    week_song_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/v_white_round_bg')
    song_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_song')
    vocabulary_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_word')
    daily_spoken_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_oral')
    story_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_cartoon')
    video_or_song_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_video_or_song')
    change_to_video_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/btn_change_to_video')
    week_song_back_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/iv_back')
    # song_back_btn = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
    #                                  '.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
    #                                  '/android.widget.RelativeLayout[1]/android.widget.ImageButton')
    song_back_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/audio_top_back_btn')
    vocabulary_close_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/action_cancel')
    daily_spoken_back_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/action_back')
    full_album_back_btn = (MobileBy.ID, 'com.jiliguala.niuwa:id/back')
    full_album_btn = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup['
                                      '2]/android.widget.RelativeLayout/android.widget.ImageView[2]')

    extend_title_text = (MobileBy.ID, 'com.jiliguala.niuwa:id/tv_extension_title')

    view_more_tip = (MobileBy.ID, 'com.jiliguala.niuwa:id/show_list_tip')
