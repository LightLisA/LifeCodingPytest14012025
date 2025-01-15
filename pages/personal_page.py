import time
import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@placeholder='First Name']")
    LICENSE_EXPIRY_DATE_FIELD = ("xpath", "//input[@placeholder='yyyy-dd-mm']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    SUCCESSFUL_POPUP = ("xpath", "//div[contains(@class, 'oxd-toast-content--success')]")
    SUCCESSFUL_TITLE = ("xpath", "//p[contains(@class, 'oxd-text--toast-title')]")
    SUCCESSFUL_MESSAGE = ("xpath", "//p[contains(@class, 'oxd-text--toast-message')]")

    def change_name(self, new_name: str):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "a")  # Виділяє весь текст
            first_name_field.send_keys(Keys.BACKSPACE)  # Видаляє виділений текст
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes gas been saved successfully")
    def is_changes_saved(self):

        successful_popup = self.wait.until(EC.visibility_of_element_located(self.SUCCESSFUL_POPUP))
        successful_title_text = self.wait.until(EC.visibility_of_element_located(self.SUCCESSFUL_TITLE)).text
        successful_message_text = self.wait.until(EC.visibility_of_element_located(self.SUCCESSFUL_MESSAGE)).text
        assert successful_popup, "Pop-up is not visible"
        if successful_popup:
            assert successful_title_text == "Success", \
                f"Expected title 'Success', but got '{successful_title_text}'"
            assert successful_message_text == "Successfully Updated", \
                f"Expected message 'Successfully Updated', but got '{successful_message_text}'"

        self.wait.until(EC.invisibility_of_element(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))


