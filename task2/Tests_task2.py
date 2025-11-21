import time

from selenium.common import ElementClickInterceptedException
from PageObject import MainPage
from conftest import driver

def test_positive_create_task(driver): #1
    page = MainPage(driver)
    page.click_new_task()
    page.enter_valid_name()
    page.enter_description()
    page.select_project()
    page.select_priority()
    page.select_executor()
    assert page.click_create_task() , "Задача не создана"

def test_create_task_without_required_parameters(driver): #2
    page = MainPage(driver)
    page.click_new_task()
    page.enter_description()
    assert not page.is_create_button_clickable() , "Задача создана без необходимых параметров"

def test_create_task_with_long_name(driver): #3
    page = MainPage(driver)
    page.click_new_task()
    page.enter_long_name()
    page.enter_description()
    page.select_project()
    page.select_priority()
    page.select_executor()
    page.click_create_task()
    assert page.click_create_task() , "Задача не создана"

def test_open_task(driver): #4
    page = MainPage(driver)
    assert page.open_existing_task() , "Не удалось открыть задачу"


def test_change_description_in_existing_task(driver): #5
    page = MainPage(driver)
    page.open_existing_task()
    page.update_description()
    assert page.click_update_task() , "Описание задачи не обновлено"

def test_change_required_params_in_existing_task(driver): #6
    page = MainPage(driver)
    page.open_existing_task()
    page.update_name()
    name = page.update_name()
    page.click_update_task()
    page.search_by_name(name)

    if page.is_task_exist():
        assert name == page.first_task_from_list()
    else:
        assert page.is_task_exist(), "Параметры задачи не обновлены"


def test_search_task(driver): #7
    page = MainPage(driver)
    name = page.search()
    assert name == page.first_task_from_list() , "Существующая задача не найдена через поисковую строку"

def test_search_with_space_and_data(driver): #8
    page = MainPage(driver)
    name = page.search()
    page.search_input_clear()
    page.search_by_name(" " + name + " ")
    assert page.is_task_exist(), "Пробелы некорректно влияют на поиск задачи"


def test_search_with_front_space(driver): #19
    page = MainPage(driver)
    name = page.search()
    page.search_input_clear()
    page.search_by_name(" " + name)
    assert page.is_task_exist(), "Пробел спереди введеного имени задачи в поисковую строку некорректно влияет на поиск задачи"

def test_search_with_back_space(driver): #10
    page = MainPage(driver)
    name = page.search()
    page.search_input_clear()
    page.search_by_name(name + " ")
    assert page.is_task_exist(), "Пробел сзади введеного имени задачи в поисковую строку некорректно влияет на поиск задачи"

def test_search_with_space(driver): #11
    page = MainPage(driver)
    name = "             "
    page.search_by_name(name)
    assert page.is_task_exist(), "Строка только из пробелов неккоректно влияет на поиск задачи"

def test_clear_search_input(driver): #12
    page = MainPage(driver)
    name = page.search()
    page.search_input_clear()
    assert page.is_search_input_clear() == "", "Быстрая очистка поисковой строки не сработала"

def test_search_by_status(driver): #13
    page = MainPage(driver)
    page.search_by_status()
    status = page.search_by_status()
    assert status == page.first_status_from_list() ,"Существующая задача не найдена через фильтр по статусу"

def test_search_by_dashboard(driver): #14
    page = MainPage(driver)
    page.search_by_dashboard()
    dashboard = page.search_by_dashboard()
    assert dashboard in page.first_dashboard_from_list() ,"Существующая задача не найдена через фильтр по доске"

def test_search_with_name_status_dashboard(driver): #15
    test_search_by_status(driver)
    time.sleep(2)
    test_search_by_dashboard(driver)
    time.sleep(2)
    test_search_task(driver)


def test_transition_to_dashboard_from_task_description(driver): #16
    page = MainPage(driver)
    page.search_by_dashboard()
    dashboard = page.search_by_dashboard()
    page.open_existing_task()
    page.go_to_dashboard_from_task_description()
    assert dashboard == page.get_dashboard_tittle() ,"Не удалось перейти на доску из описания задачи"

def test_transition_to_dashboard_from_task_list(driver): #17
    page = MainPage(driver)
    page.go_to_projects()
    page.go_to_dashboard_from_project_list()
    tittle = page.get_dashboard_tittle()
    assert page.is_dashboard(tittle) ,"Не удалось перейти на доску из списка задач"







