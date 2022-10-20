import time
import pyautogui as py


def monday(day, h=1):
    if (day == 0):
        return 0

    hour(h)
    day()


def tuesday(day, h=1):
    if (day == 1):
        return 0

    hour(h)
    day()


def wednesday(day, h=1):
    if (day == 2):
        return 0

    hour(h)
    day()


def thursday(day, h=1):
    if (day == 3):
        return 0

    hour(h)
    day()


def friday(day, h=1):
    if (day == 4):
        return 0

    hour(h)
    day()


def saturday(day, h=1):
    if (day == 5):
        return 0

    hour(h)
    day()


def sunday(day, h=1):
    if (day == 6):
        return 0

    hour(h)
    day()


def after_book():
    py.scroll(-1000)
    py.moveTo(694, 205, 0.5)
    py.leftClick()
    py.write("samir.suarez", 0.03)
    py.hotkey("altright", "q")
    py.write("utec.edu.pe", 0.03)
    time.sleep(0.2)

    py.moveRel(0, 150)
    py.leftClick()
    py.write("2", 0.1)
    time.sleep(0.2)

    py.moveRel(0, 130)
    py.leftClick()

    py.moveRel(330, 130)
    py.leftClick()

    time.sleep(1)
    py.hotkey("ctrl", "w")


def before_book():
    py.hotkey("win", "r")
    py.write("https://affluences.com/biblioteca-utec/reservation")
    py.press("enter")

    py.moveTo(1523, 880, 3)
    py.leftClick()
    py.scroll(-40)
    py.leftClick()
    time.sleep(0.2)

    py.moveRel(-300, 0)
    py.leftClick()
    py.scroll(-20)
    py.leftClick()
    py.scroll(20)


def hour(n):
    n = int(4*(n+1))
    time.sleep(0.2)
    py.moveRel(-300, 0)
    py.leftClick()
    py.moveRel(0, -350, 1)
    py.scroll(-29 * (n-1))
    py.leftClick()
    py.scroll(20)


def day():

    time.sleep(0.2)
    py.moveRel(-340, 360)
    py.leftClick()

    mes = time.localtime().tm_mon

    if (mes in [4, 6, 9, 11]):
        d = (time.localtime().tm_mday + 1) % 31
    else:
        d = (time.localtime().tm_mday + 1) % 32

    d = str(d)
    ruta = "D:\Personal_Projects\Python\ProbandoAutomatizacion\dias\\" + d + ".png"
    coor = py.locateCenterOnScreen(ruta, confidence=0.9)

    time.sleep(0.2)
    py.moveTo(coor)
    py.leftClick()
    time.sleep(1)
    py.scroll(-900)
    py.moveTo(1706, 636, 0.5)
    py.leftClick()


def main():

    before_book()

    day = time.localtime().tm_wday
    monday(day, 11)
    tuesday(day, 9)
    wednesday(day, 10)
    thursday(day, 15)
    friday(day, 9)
    saturday(day)
    sunday(day, 15)

    after_book()

    return 0


main()
