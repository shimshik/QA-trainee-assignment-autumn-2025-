import random

from selenium.webdriver.common.by import By
import testcase_data


class Locators:
    new_task_button = (By.XPATH, '//button[text() = "Создать задачу"]')
    name = (By.XPATH, "//input[@class = 'MuiInputBase-input MuiOutlinedInput-input css-1pk1fka']")
    description = (By.XPATH,"//textarea[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputMultiline css-s63k3s']")
    projects_dropdown = (By.XPATH, '//div[label[text() = "Проект"]]')
    projects_name = (By.XPATH, f"//li[@data-value = {testcase_data.unique_project_name_id()}]")
    priority_dropdown = (By.XPATH, '//div[label[text() = "Приоритет"]]')
    priority_name = (By.XPATH, f"//li[@data-value = '{testcase_data.unique_priority_name()}' ]")
    executor_dropdown = (By.XPATH, '//div[label[text() = "Исполнитель"]]')
    executor_name = (By.XPATH, f"//li[@data-value = {testcase_data.unique_executor_name_id()}]")
    create_task_button = (By.XPATH, "//button[text() = 'Создать']")
    task_in_the_task_list = (By.XPATH, "//div[@class = 'MuiBox-root css-69i1ev']")
    names_of_task_from_task_list = (By.XPATH,"//div[@class = 'MuiBox-root css-69i1ev']//h6")
    open_task_window = (By.XPATH,"//div[@class = 'MuiBox-root css-1epuubg']")
    update_task_button = (By.XPATH, "//button[text() = 'Обновить']")
    search_input = (By.XPATH, "//input[@id=':r3:']")
    search_input_cross = (By.XPATH,"//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-xz9haa']")
    search_by_status_dropdown = (By.XPATH,"//div[label[text() = 'Статус']]")
    search_by_dashboard_dropdown = (By.XPATH, "//div[label[text() = 'Доска']]")
    status_name = (By.XPATH, f"//li[@data-value = '{testcase_data.unique_status_name()}' ]")
    dashboard_name = (By.XPATH, f"//li[@data-value = '{testcase_data.unique_dashboard_name()}' ]")
    status_name_from_task_list = (By.XPATH, "//span[@class = 'MuiChip-label MuiChip-labelSmall css-b9zgoq']")
    dashboard_name_from_task_list = (By.XPATH, "//p[@class = 'MuiTypography-root MuiTypography-body2 css-1xinhls']")
    go_to_dashboard_button = (By.XPATH,"//a[text() = 'Перейти на доску']")
    dashboard_tittle = (By.XPATH,"//div[@class = 'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-1e90fby']//h4")
    go_to_projects = (By.XPATH, "//a[text()='Проекты']")
    to_dashboard_from_projects_list = (By.XPATH,"//a[@href = '/board/1']")