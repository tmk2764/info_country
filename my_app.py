from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QTextEdit
import json
app = QApplication([])
window = QWidget()

#countries = {
#    'Казахстан': ''
#}
#with open('countries.json','w',encoding='utf-8') as file:
#json.dump(countries,file)
main_layout = QHBoxLayout()
row_left = QVBoxLayout()
row_right = QVBoxLayout()
window.setWindowTitle('Информация о странах')
list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
add_country_but = QPushButton('Добавить страну')
del_country_but = QPushButton('Удалить страну')
edit_country_but = QPushButton('Изменить страну')
line_countries = QHBoxLayout()
line_countries.addWidget(add_country_but)
line_countries.addWidget(del_country_but)
line_countries.addWidget(edit_country_but)
name_countries.setPlaceholderText('Введите страну...')

row_right.addWidget(list_countries)
row_left.addWidget(text_countries)
row_left.addWidget(name_countries)
row_left.addLayout(line_countries)
main_layout.addLayout(row_left,7)
main_layout.addLayout(row_right,3)

window.setStyleSheet('background-color: white;color: red')
list_countries.setStyleSheet('border: 2px solid blue; font-size: 20px')
text_countries.setStyleSheet('border: 2px solid blue; font-size: 20px')
name_countries.setStyleSheet('border: 2px solid blue; font-size: 18px')
add_country_but.setStyleSheet('border: 2px solid blue; font-size: 18px')
del_country_but.setStyleSheet('border: 2px solid blue; font-size: 18px')
edit_country_but.setStyleSheet('border: 2px solid blue; font-size: 18px')

with open('countries.json','r',encoding='utf-8') as file:
    countries = json.load(file)
    for country in countries:
        list_countries.addItem(country)


def add_country():
    country = name_countries.text()
    with open('countries.json', 'r',encoding='utf-8') as file:
        countries = json.load(file)
    countries[country] = ''
    with open('countries.json', 'w',encoding='utf-8') as file:
        json.dump(countries,file)
    list_countries.clear()
    with open('countries.json', 'r',encoding='utf-8') as file:
        countries = json.load(file)
        for country in countries:
            list_countries.addItem(country)

def del_country():
    country = list_countries.selectedItems()[0].text()
    if country:
        with open('countries.json', 'r',encoding='utf-8') as file:
            countries = json.load(file)
        del countries[country]
        with open('countries.json', 'w',encoding='utf-8') as file:
            json.dump(countries,file)
        list_countries.clear()
        with open('countries.json', 'r',encoding='utf-8') as file:
            countries = json.load(file)
            for country in countries:
                list_countries.addItem(country)
    else:
        pass

def edit_country():
    country = list_countries.selectedItems()[0].text()
    if country:
        with open('countries.json', 'r',encoding='utf-8') as file:
            countries = json.load(file)
        text = text_countries.toPlainText()
        countries[country] = text
        with open('countries.json', 'w',encoding='utf-8') as file:
            json.dump(countries,file)
    else:
        pass

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r',encoding='utf-8') as file:
        countries = json.load(file)
    text_countries.setText(countries[country])

add_country_but.clicked.connect(add_country)
del_country_but.clicked.connect(del_country)
edit_country_but.clicked.connect(edit_country)
list_countries.itemClicked.connect(info_country)
window.setLayout(main_layout)
window.show()
app.exec()