import pytest

from common.utils import setup
from pageView.extendPage.extendPage import ExtendPage
from pageView.homePage.honePage import HomePage
from pageView.onboardingPage.onboardingPage import OnboardingPage


@pytest.fixture(scope="class")
def onboarding_page(setup):
    return OnboardingPage(setup)


@pytest.fixture(scope="class")
def home_page(setup):
    return HomePage(setup)


@pytest.fixture(scope="class")
def extend_page(setup):
    return ExtendPage(setup)
