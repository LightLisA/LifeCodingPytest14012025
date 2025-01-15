import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage


class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.driver = browser
        request.cls.data = Data()
        request.cls.login_page = LoginPage(browser)
        request.cls.dashboard_page = DashboardPage(browser)
        request.cls.personal_page = PersonalPage(browser)
