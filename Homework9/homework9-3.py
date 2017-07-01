# -*- coding: utf-8 -*-
# Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить
# все ссылки со страницы на другие. Ответить себе на вопрос
# удобно ли так делать?
import re
import requests


def links_from_web(url):
    site = requests.get(url)
    cont = site.content.decode("utf-8")
    links = re.findall(r'href=[\'"]?([^\'" >]+)', cont)
    for i in links:
        print(i)


if __name__ == '__main__':
    links_from_web('https://habrahabr.ru')
