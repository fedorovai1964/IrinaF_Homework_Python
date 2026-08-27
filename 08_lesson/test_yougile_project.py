from config import url
from project_api import ProjectApi


def test_post_positive():
    project = ProjectApi(url)
    result = project.post_create_project("Мой второй проект")
    assert result.status_code == 201
    id = result.json()["id"]
    title = project.get_project(id)
    assert title.json()['title'] == "Мой второй проект"
    # очистка данных
    project.delete_project(id)


def test_post_negative():   # Пустое название проекта
    project = ProjectApi(url)
    result = project.post_create_project("")
    assert result.status_code == 400


def test_put_positive():
    project = ProjectApi(url)
    result = project.post_create_project("Создание проекта")
    id = result.json()["id"]

    title_change = project.put_сhange_project(id, "Изменение проекта")
    assert title_change.status_code == 200

    title = project.get_project(id)
    assert title.json()['title'] == "Изменение проекта"
    # очистка данных
    project.delete_project(id)


def test_put_negative():    # Пустое название проекта
    project = ProjectApi(url)
    result = project.post_create_project("Создание проекта")
    id = result.json()["id"]

    title_change = project.put_сhange_project(id, "")
    assert title_change.status_code == 400

    title = project.get_project(id)
    assert title.json()['title'] == "Создание проекта"
    # очистка данных
    project.delete_project(id)


def test_get_positive():
    project = ProjectApi(url)
    result = project.post_create_project("Мой второй проект")
    id = result.json()["id"]

    title = project.get_project(id)
    assert title.status_code == 200
    assert title.json()['title'] == "Мой второй проект"
    # очистка данных
    project.delete_project(id)


def test_get_negative():     # id = 0
    project = ProjectApi(url)
    result = project.post_create_project("Мой второй проект")
    id = result.json()["id"]

    title = project.get_project(id=0)
    assert title.status_code == 404

    # очистка данных
    project.delete_project(id)
