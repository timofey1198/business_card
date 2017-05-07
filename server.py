# -*- coding: utf-8 -*-
from flask import Flask
from content import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    menu = '\
            <div class="menu_box">\
                <a href="index"><div class="Menu-opened">Главная</div></a>\
                <a href="about"><div class="Menu">Обо мне</div></a>\
                <a href="science"><div class="Menu">Наука</div></a>\
                <a href="contacts"><div class="Menu">Контакты</div></a>\
            </div>'    
    content = '\
        <div class="content">\
            <div class="news">\
                <h3>Это я</h3><br>\
                <img src="img/me_1" height="200px">\
            </div>\
            <div class="news">\
                <h3>Новость2</h3><br>\
                <p>Текст</p>\
            </div>\
        </div>'
    return html_all(menu, content)


@app.route("/about")
def about():
    menu = '\
            <div class="menu_box">\
                <a href="index"><div class="Menu">Главная</div></a>\
                <a href="about"><div class="Menu-opened">Обо мне</div></a>\
                <a href="science"><div class="Menu">Наука</div></a>\
                <a href="contacts"><div class="Menu">Контакты</div></a>\
            </div>'     
    about_1 = open('pages/about_1.txt', 'r')
    about_2 = open('pages/about_2.txt', 'r')
    content = ('\
        <div class="content">\
            <div class="news">\
                <h1>Обо мне</h1><br>'
                + about_1.read() +
            '</div>\
            <div class="news">'
                + about_2.read() +
            '</div>\
        </div>')
    return html_all(menu, content)


@app.route("/contacts")
def contacts():
    menu = '\
            <div class="menu_box">\
                <a href="index"><div class="Menu">Главная</div></a>\
                <a href="about"><div class="Menu">Обо мне</div></a>\
                <a href="science"><div class="Menu">Наука</div></a>\
                <a href="contacts"><div class="Menu-opened">Контакты</div></a>\
            </div>'     
    content = '\
        <div class="content">\
            <div class="news">\
                <h1>Контакты</h1><br>\
            </div>\
        </div>'
    return html_all(menu, content)


@app.route("/science")
def science():
    menu = '\
            <div class="menu_box">\
                <a href="index"><div class="Menu">Главная</div></a>\
                <a href="about"><div class="Menu">Обо мне</div></a>\
                <a href="science"><div class="Menu-opened">Наука</div></a>\
                <a href="contacts"><div class="Menu">Контакты</div></a>\
            </div>'     
    science = open('pages/science.txt', 'r')
    content = ('\
        <div class="content">\
            <div class="news">\
                <h1>Наука</h1><br>'
                + science.read() +
            '</div>\
        </div>')
    return html_all(menu, content)


#---------------------------------RESOURCES------------------------------------

@app.route("/style")
@app.route("/style.css")
def style():
    st = open('resources/style.css', 'r', encoding='utf-8')
    style = st.read()
    return style


@app.route("/img/top")
def top():
    img = open('resources/img/top.png', 'rb')
    return img.read()


@app.route("/img/me_1")
def me_1():
    img = open('resources/img/me_1.jpg', 'rb')
    return img.read()


if __name__ == "__main__":
    app.run()