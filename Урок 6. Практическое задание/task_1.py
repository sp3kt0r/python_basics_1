"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep #указываем то что импртируем функцию time с модуля sleep. Делается это для того чтобы программа поняла что программа будет иметь задержку.


class TrafficLight: # создаём класс
    color = ['Красный', 'Желтый', 'Зеленый'] # задаём атрибут цвета

    def running(self): #вызываем инструкцией def будущую функцию running
        i = 0 # задаём переменную i которой будет присвоен 0
        while i != 3: # задаём цикл пока i не будет равен 3
          
            print(TrafficLight.color[i]) # выводим класс с атрибутом цвета
            if i == 0: # если i равен 0 то следующее действие будет в задержке на 7 секунд
                sleep(7)
            elif i == 1: # указываем на i если оно будет равно 1, уходит в задержку на 2 секунды
                sleep(2)
            elif i == 2: # если i равно 2, тто оно уйдёт в задержку на 10 секунд
                sleep(10)
            i += 1 # оператор для выявления истины, если всё верно, то запуск пройдёт т.к все три значения будут верны, без него будет выводить только первое значение

t = TrafficLight() # задали переменную t и указали на класс 
t.running()  #запустили метод running в классе
