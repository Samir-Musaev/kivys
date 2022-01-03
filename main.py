import socket

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread

import threading
import socket

KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y":0.5}

        Label:
                font_size: "30sp"
                text: root.data_label
        TextInput:
                id: Inp
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.5)
        Button:
                text: "Поиск по названию"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "Поиск по описанию"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback2()
        Button:
                text: "Случайный"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback3()
        Button:
                text: "Отправить"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback4()
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!Что найти?")

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     SERVER = "10.8.0.6"
    #     PORT = 1488
    #
    #     self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.client.connect((SERVER, PORT))
    #     self.client.sendall(bytes("979879789",'UTF-8'))
    #
    #     threading.Thread(target=self.get_data).start()

    def callback(self):
        self.data_label = "Поиск по названию"
        # self.client.sendall(bytes("Поиск по названию",'UTF-8'))

    def callback2(self):
        self.data_label = "Поиск по описанию"

    def callback3(self):
        self.data_label = "Случайный"

    def callback4(self):
        self.data_label = "Отправить"

    # def get_data(self):
    #     while App.get_running_app().running:
    #         in_data = self.client.recv(4096)
    #         print("От сервера :", in_data.decode())
    #         kkk = in_data.decode()
    #         self.set_data_label(kkk)Введите запрос
    #
    #
    #
    #
    #
    #
    # Фото профиля

    # @mainthread
    # def set_data_label(self, data):
    #     self.data_label += str(data) + '\n'


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()