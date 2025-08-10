from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import random
import sys

# Инициализация браузера (выберите нужный вам браузер)
browser = webdriver.Firefox()  # Для Firefox
#browser = webdriver.Chrome()  # Для Chrome


def search_wikipedia(query):
    # Переходим на страницу Википедии
    browser.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(2)  # Ждем загрузки страницы

    # Проверяем, что страница загружена правильно
    expected_title = query.replace('_', ' ')
    if expected_title not in browser.title:
        print(f"Ошибка: Ожидаемый заголовок '{expected_title}' не найден в фактическом заголовке '{browser.title}'.")
        browser.quit()
        sys.exit(1)


def list_paragraphs():
    # Находим все параграфы на странице
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        user_input = input("Нажмите Enter для продолжения или введите 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            return


def choose_random_link():
    # Находим все элементы в разделе "См. также" или "Ссылки"
    try:
        see_also_section = browser.find_element(By.ID, "see-also")
    except:
        try:
            see_also_section = browser.find_element(By.ID, "links")
        except:
            print("Раздел 'См. также' или 'Ссылки' не найден.")
            return

    links = see_also_section.find_elements(By.TAG_NAME, "a")
    see_also_links = [link for link in links if link.get_attribute("href")]

    if not see_also_links:
        print("Нет связанных статей.")
        return

    # Выбираем случайную связную статью
    random_link = random.choice(see_also_links)
    link_text = random_link.text
    link_href = random_link.get_attribute("href")

    # Переходим на выбранную статью
    browser.get(link_href)
    time.sleep(2)  # Ждем загрузки страницы

    # Получаем название статьи из URL
    new_query = link_href.split('/')[-1]
    search_wikipedia(new_query)


def main():
    # Спрашиваем у пользователя первоначальный запрос
    initial_query = input("Введите ваш запрос для поиска в Википедии: ").replace(' ', '_')
    search_wikipedia(initial_query)

    while True:
        # Предлагаем пользователю выбрать действие
        action = input(
            "Выберите действие:\n1. Листать параграфы текущей статьи\n2. Перейти на одну из связанных страниц\n3. Выйти из программы\n")

        if action == '1':
            list_paragraphs()
        elif action == '2':
            choose_random_link()
        elif action == '3':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

    # Закрываем браузер
    browser.quit()


if __name__ == "__main__":
    main()