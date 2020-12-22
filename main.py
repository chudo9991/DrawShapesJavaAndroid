import wikipedia
import requests
from speach import *

def S():
    h = int(input("Введи высоту: "))
    l = int(input("Введи сторону: "))
    print("Площадь треугольника: ", 0.5*h*l)
    say("Площадь треугольника:" + str(0.5*h*l))

def wiki():
    wikipedia.set_lang("ru")
    say("О чём ты хочешь узнать?")
    x = input("О чём ты хочешь узнать? ")
    print(wikipedia.summary(x))
    say(wikipedia.summary(x, sentences=1))

def weather():
    appid = "8a61dda3a2ef6afaf929cc1c4154f9ef"
    s_city = "Petrozavodsk"
    city_id = 509820

    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params= {
                           'q': s_city,
                           'id': city_id,
                           'type': 'like',
                           'units': 'metric',
                           'APPID': appid
                       })
    print(res.json()['list'][0])
    print("Температура сейчас:", res.json()['list'][0]['main']['temp'])
    print("Ощущается как:", res.json()['list'][0]['main']['feels_like'])
    print("Давление", res.json()['list'][0]['main']['pressure'])
    print("Влажность", res.json()['list'][0]['main']['humidity'])


print("Привет! Я - Джарвис, твой бот-помощник.")
say("Привет! Я - ДжАрвис, твой бот-помощник.")
print("Чтобы выбрать команду введи соотвествующую цифру.")
say("Чтобы выбрать команду введи соотвествующую цифру.")
print("Чтобы выйти введи 'exit'")
say("Чтобы выйти введи эксит")

answer = ""

while answer != "exit":
    print("1 - посчитать площадь треугольника, 2 - инфо из Википедии, 3 - текущая погода")
    answer = input("Введи команду: ")
    if answer=="1":
        S()
    elif answer=="2":
        wiki()
    elif answer=="3":
        weather()

