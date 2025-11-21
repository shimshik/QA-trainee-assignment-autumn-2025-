
from selenium.common import ElementClickInterceptedException
from PageObject import MainPage
from conftest import driver

def test_positive_create_task(driver):
    page = MainPage(driver)
    page.click_new_task()
    page.enter_valid_name()
    page.enter_description()
    page.select_project()
    page.select_priority()
    page.select_executor()
    page.click_create_task()

def test_create_task_without_required_parameters(driver):
    page = MainPage(driver)
    page.click_new_task()
    page.enter_description()
    try:
        page.click_create_task()
    except ElementClickInterceptedException:
        assert True

def test_create_task_with_long_name(driver):
    page = MainPage(driver)
    page.click_new_task()
    page.enter_long_name()
    page.enter_description()
    page.select_project()
    page.select_priority()
    page.select_executor()
    page.click_create_task()

def test_open_task(driver):
    page = MainPage(driver)
    page.open_existing_task()


def test_change_params_in_existing_task(driver):
    page = MainPage(driver)
    page.open_existing_task()
    page.update_description()
    page.click_update_task()

def test_search_task(driver):
    page = MainPage(driver)
    name = page.search()
    assert name == page.first_task_from_list()

def test_search_by_status(driver):
    page = MainPage(driver)
    page.search_by_status()
    status = page.search_by_status()
    assert status == page.first_status_from_list()

def test_search_by_dashboard(driver):
    page = MainPage(driver)
    page.search_by_dashboard()
    dashboard = page.search_by_dashboard()
    assert dashboard in page.first_dashboard_from_list()


def test_transition_to_dashboard_from_task_description(driver):
    page = MainPage(driver)
    page.search_by_dashboard()
    dashboard = page.search_by_dashboard()
    page.open_existing_task()
    page.go_to_dashboard_from_task_description()
    assert dashboard == page.get_dashboard_tittle()

def test_transition_to_dashboard_from_task_list(driver):
    page = MainPage(driver)
    page.go_to_projects()
    page.go_to_dashboard_from_project_list()
    tittle = page.get_dashboard_tittle()
    assert page.is_dashboard(tittle)







