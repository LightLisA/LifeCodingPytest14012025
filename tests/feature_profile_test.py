import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Middle")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        assert self.data.LOGIN is not None, "LOGIN не може бути None"
        self.login_page.enter_login(self.data.LOGIN)
        assert self.data.PASSWORD is not None, "PASSWORD не може бути None"
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test_{random.randint(1, 20)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshots("Success")
