from re import search

from BasePage import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import testcase_data
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_task(self):
        self.driver.find_element(*Locators.new_task_button).click()

    def enter_valid_name(self):
        name = testcase_data.unique_valid_task_name()
        self.driver.find_element(*Locators.name).send_keys(name)

    def enter_long_name(self):
        name = testcase_data.not_valid_task_name()
        self.driver.find_element(*Locators.name).send_keys(name)

    def enter_description(self):
        description = testcase_data.unique_description()
        self.driver.find_element(*Locators.description).send_keys(description)

    def select_project(self):
        dropdown = self.driver.find_element(*Locators.projects_dropdown).click()
        option = self.driver.find_element(*Locators.projects_name).click()
    def select_priority(self):
        dropdown = self.driver.find_element(*Locators.priority_dropdown).click()
        option = self.driver.find_element(*Locators.priority_name).click()

    def select_executor(self):
        dropdown = self.driver.find_element(*Locators.executor_dropdown).click()
        option = self.driver.find_element(*Locators.executor_name).click()

    def click_create_task(self):
        self.driver.find_element(*Locators.create_task_button).click()

    def create_task(self):
        create_button = self.driver.find_element(*Locators.create_task_button)
        return create_button

    def open_existing_task(self):
        self.driver.find_element(*Locators.task_in_the_task_list).click()
        self.driver.find_element(*Locators.open_task_window)

    def click_update_task(self):
        self.driver.find_element(*Locators.update_task_button).click()

    def update_description(self):
        description = testcase_data.unique_description()
        self.driver.find_element(*Locators.description).clear()
        self.driver.find_element(*Locators.description).send_keys(description)

    def search(self):
        names = self.driver.find_element(*Locators.names_of_task_from_task_list)
        name = names.text
        required_task = self.driver.find_element(*Locators.search_input).send_keys(name)
        return name
    def first_task_from_list(self):
        names = self.driver.find_element(*Locators.names_of_task_from_task_list)
        name = names.text
        return name

    def search_by_status(self):
        self.driver.find_element(*Locators.search_by_status_dropdown).click()
        status = self.driver.find_element(*Locators.status_name)
        status.click()
        status = status.text
        return status
    def first_status_from_list(self):
        status = self.driver.find_element(*Locators.status_name_from_task_list).text
        return status

    def search_by_dashboard(self):
        self.driver.find_element(*Locators.search_by_dashboard_dropdown).click()
        dashboard = self.driver.find_element(*Locators.dashboard_name)
        dashboard.click()
        dashboard = dashboard.text
        return dashboard

    def first_dashboard_from_list(self):
        dashboard = self.driver.find_element(*Locators.dashboard_name_from_task_list).text
        return dashboard

    def get_dashboard_tittle(self):
        dashboard_tittle = self.driver.find_element(*Locators.dashboard_tittle).text
        return dashboard_tittle

    def go_to_dashboard_from_task_description(self):
        self.driver.find_element(*Locators.go_to_dashboard_button).click()

    def go_to_projects(self):
        self.driver.find_element(*Locators.go_to_projects).click()

    def go_to_dashboard_from_project_list(self):
        self.driver.find_element(*Locators.to_dashboard_from_projects_list).click()

    def is_dashboard(self,tittle):
        list = ["Редизайн карточки товара", "Все",
                "Оптимизация производительности",
                "Рефакторинг API", "Миграция на новую БД",
                "Автоматизация тестирования", "Переход на Kubernetes"]
        if tittle in list:
            return True
        else:
            return False