import time
import pyautogui as py


def main():

    before_book()

    #day = time.localtime().tm_wday
    day = 0
    if (day == 0):
        monday()
    elif (day == 1):
        tuesday()
    elif (day == 2):
        wednesday()
    elif (day == 3):
        thursday()
    elif (day == 4):
        friday()
    elif (day == 5):
        saturday()

    after_book()

    return 0


def monday():

    # Hora
    hour(11.5)

    # Dia
    d = time.localtime().tm_mday
    d = str(d)
    coor = py.locateCenterOnScreen(
        "D:\Personal_Projects\Python\ProbandoAutomatizacion\dias\\"+d+".png")

    time.sleep(0.2)
    py.moveRel(-340, 0)
    py.leftClick()

    time.sleep(0.2)
    py.moveTo(coor, 0.5)
    py.leftClick()
    time.sleep(1)
    py.scroll(-900)
    py.moveTo(1706, 636, 0.5)
    py.leftClick()


def tuesday():
    return 0


def wednesday():
    return 0


def thursday():
    return 0


def friday():
    return 0


def saturday():
    return 0


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

    py.moveTo(1523, 880, 2.5)
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


def dia():

    d = time.localtime().tm_mday
    d = str(d)
    coor = py.locateCenterOnScreen(
        "D:\Personal_Projects\Python\ProbandoAutomatizacion\dias\\"+d+".png")

    time.sleep(0.2)
    py.moveRel(-340, 0)
    py.leftClick()
    time.sleep(0.2)
    py.moveTo(coor, 0.5)
    py.leftClick()


# main()
# time.sleep(4)
# print(py.position())
# main()
# time.sleep(4)
# monday()
time.sleep(4)
re = py.locateCenterOnScreen(
    "D:\Personal Projects\Personal_Projects\Python\ProbandoAutomatizacion\\edit.png", confidence=0.7)
print(re)
