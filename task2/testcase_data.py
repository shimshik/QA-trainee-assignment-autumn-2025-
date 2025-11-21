import random, string
from datetime import datetime

def unique_valid_task_name():
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    task_name = f"Test Task {random_str}_{datetime.now().strftime('%H%M%S')}"
    return task_name
def unique_project_name_id():
    return random.randint(1, 6)
def unique_priority_name():
    list = ["Low","Medium","High"]
    return list[random.randint(0,2)]
def unique_executor_name_id():
    return random.randint(1, 7)
def unique_description(word_count=10):
    description = []
    for _ in range(word_count):
        word_length = random.randint(1, 8)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        description.append(word)
    return ' '.join(description)

def not_valid_task_name():
    random_str = ''.join(random.choices(string.ascii_letters + string.digits+string.punctuation, k = random.randint(256,300)))
    task_name = f"Test Task {random_str}_{datetime.now().strftime('%H%M%S')}"
    return task_name

def unique_status_name():
    list = ["Backlog","InProgress","Done"]
    return list[random.randint(0,2)]

def unique_dashboard_name():
    list = ["Редизайн карточки товара","Все","Оптимизация производительности","Рефакторинг API","Миграция на новую БД","Автоматизация тестирования","Переход на Kubernetes"]
    return list[random.randint(0,6)]

def unique_dashboard_id():
    return random.randint(1,6)


