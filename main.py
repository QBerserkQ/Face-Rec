import cv2
import numpy
import face_recognition_models
import face_recognition
import telebot
import config
from telebot import types
from simple_facerec import SimpleFacerec

names = []
sfr = SimpleFacerec()
sfr.load_encoding_images("D:\Games2\OPENCV\img/")

cam = cv2.VideoCapture(2)

bot = telebot.TeleBot(config.TOKEN)

while True:
    boolean, window = cam.read()

    face_location, face_name = sfr.detect_known_faces(window)
    for faceloc, facename in zip(face_location, face_name):
        y1, x2, y2, x1 = faceloc[0], faceloc[1], faceloc[2], faceloc[3]

        cv2.putText(window, facename, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.rectangle(window, (x1, y1), (x2, y2), (25, 240, 30), 3)
        if facename not in names:
            if facename != 'Unknown':
                names.append(facename)

    cv2.imshow("Face", window)

    key = cv2.waitKey(1)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


stroka = ', '.join(names)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Посещаемость')
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=kb)

@bot.message_handler(content_types=['text'])
def start1(message):
    if message.chat.type == 'private':
        if message.text == 'Посещаемость':
            bot.send_message(message.chat.id, stroka)
        else:
            bot.send_message(message.chat.id, 'Я вас не понимаю')

bot.polling()









