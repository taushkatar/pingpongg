#создай приложение для запоминания информации
#подключение библиоте
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

#создание элементов интерфейса
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People') 
button = QPushButton('ssd')

question = QLabel('В каком году канал получил «золотую кнопку» от YouTube?')
RadioGroupBox = QGroupBox('название группы')

btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')

answers = []
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

RG_h1 = QHBoxLayout()
RG_V1 = QVBoxLayout()
RG_V2 = QVBoxLayout()

RG_V1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
RG_V1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
RG_V2.addWidget(btn_answer3, alignment = Qt.AlignCenter)
RG_V2.addWidget(btn_answer4, alignment = Qt.AlignCenter)

RG_h1.addLayout(RG_V1)
RG_h1.addLayout(RG_V2)

RadioGroupBox.setLayout(RG_h1)

layout_main = QVBoxLayout()


RadioGroupResult = QGroupBox('Результат ответа')
REsult_Layout = QVBoxLayout()
trueOrFalse =QLabel('Правильн/неправильно')
rightAnswer = QLabel('222')
REsult_Layout.addWidget(trueOrFalse)
REsult_Layout.addWidget(rightAnswer)
RadioGroupResult.setLayout(REsult_Layout)

layout_main.addWidget(question, alignment=Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox, alignment= Qt.AlignCenter)
layout_main.addWidget(RadioGroupResult, alignment=Qt.AlignCenter)
layout_main.addWidget(button, alignment=Qt.AlignCenter)


def viewResult():
    check_answer()
    RadioGroupBox.hide()#скрыть
    RadioGroupResult.show()  
    button.setText('Следующий вопрос') #поменять надписm

def viewAnswer():
    ask('Вопрос', '0', '1', '2', '3')
    chekedFalse()
    RadioGroupResult.hide()#скрыть
    RadioGroupBox.show()
    button.setText('Ответ') #поменять надпись

def viewWin():
    if button.text() == 'Ответ':
        viewResult()
    else:
        viewAnswer()

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


def chekedFalse():
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(questions, right_as, wrong1, wrong2, wrong3):
    shuffle(answers)
    question.setText(questions)
    answers[0].setText(right_as)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)

def check_answer():
    if answers[0].isChecked():
        trueOrFalse.setText('Правильно')
    else:
        trueOrFalse.setText('Неправильно')
    rightAnswer.setText('Правильный ответ' + answers[0].text())
button.clicked.connect(viewWin)
main_win.setLayout(layout_main)
main_win.show()
viewAnswer()
app.exec_()
