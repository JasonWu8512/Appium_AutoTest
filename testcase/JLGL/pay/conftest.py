import pytest

from common.utils import setup
from pageView.onboardingPage.onboardingPage import OnboardingPage
from pageView.payPage.guestPayPage import GuestPayPage
from pageView.payPage.noPayPage import NoPayPage
from pageView.payPage.pay88Page import Pay88Page
from pageView.payPage.payYearPage import PayYearPage
from pageView.payPage.payBasePage import PayBasePage


@pytest.fixture(scope="class")
def onboarding_page(setup):
    return OnboardingPage(setup)


@pytest.fixture(scope="class")
def guest_pay_page(setup):
    return GuestPayPage(setup)


@pytest.fixture(scope="class")
def no_pay_page(setup):
    return NoPayPage(setup)


@pytest.fixture(scope="class")
def pay_88_page(setup):
    return Pay88Page(setup)


@pytest.fixture(scope="class")
def pay_year_page(setup):
    return PayYearPage(setup)


@pytest.fixture(scope="class")
def pay_base_page(setup):
    return PayBasePage(setup)
