from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # #Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1.
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "YzE0ZjIyNTktYjc4OS00ZWE2LThhMDktYWRkN2RjYmFiNDIx",
            "domain": "gitflic.ru",
        })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/student_skypro")

    # Сохраните текущий URL.
    url1 = driver.current_url
    assert url1 == "https://gitflic.ru/user/student_skypro", "URL неверный"

    # Разлогиньтесь (очистите куки).
    driver.delete_cookie("SESSION")

    # Установите cookie пользователя 2.
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "M2RjOGNiNTYtZDIxMC00Nzg4LWE3YmItMDhlODBkNzNlMTMz",
            "domain": "gitflic.ru",
        })

    # Обновите страницу.
    driver.refresh()

    # Перейдите на страницу пользователя https://gitflic.ru/user/test_skaypro
    driver.get("https://gitflic.ru/user/test_skaypro")

    # Сохраните текущий URL.
    url2 = driver.current_url
    assert url2 == "https://gitflic.ru/user/test_skaypro", "URL не сохранился"

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    if url2 == url1:
        print(f"Ошибка, url не должны быть равны: {url1} = {url2}")
    else:
        print(f"Все верно, url разные: {url1} != {url2}")

    driver.quit()
