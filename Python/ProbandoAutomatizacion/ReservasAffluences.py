import time
import pyautogui as py


def monday(d, h=1, correo="samir.suarez"):
    if (d == 0):
        hour(h)
        day()
        after_book(correo)

    return 0


def tuesday(d, h=1, correo="samir.suarez"):
    if (d == 1):
        hour(h)
        day()
        after_book(correo)

    return 0


def wednesday(d, h=1, correo="samir.suarez"):
    if (d == 2):
        hour(h)
        day()
        after_book(correo)

    return 0


def thursday(d, h=1, correo="samir.suarez"):
    if (d == 3):
        hour(h)
        day()
        after_book(correo)

    return 0


def friday(d, h=1, correo="samir.suarez"):
    if (d == 4):
        hour(h)
        day()
        after_book(correo)

    return 0


def saturday(d, h=1, correo="samir.suarez"):
    if (d == 5):
        hour(h)
        day()
        after_book(correo)

    return 0


def sunday(d, h=1, correo="samir.suarez"):
    if (d == 6):
        hour(h)
        day()
        after_book(correo)

    return 0


def after_book(correo):

    # Moverse y registrar el apartado de correo
    time.sleep(2)
    py.scroll(-1000)
    py.moveTo(694, 205, 0.1)
    py.leftClick()
    py.write(correo, 0.02)
    py.hotkey("altright", "q")
    py.write("utec.edu.pe", 0.02)
    time.sleep(0.1)

    # Moverse y registrar la cantidad de personas
    py.moveRel(0, 150)
    py.leftClick()
    py.write("2", 0.02)
    time.sleep(0.1)

    # Aceptar los terminos y condiciones
    py.moveRel(0, 130)
    py.leftClick()

    # Guardar
    py.moveRel(330, 130)
    py.leftClick()

    # Cerrar
    time.sleep(5)
    py.hotkey("ctrl", "w")


def before_book():

    # Entra a la página de reservas
    py.hotkey("win", "r")
    py.write("https://affluences.com/biblioteca-utec/reservation")
    py.press("enter")

    # Selección del cubículo E805
    py.moveTo(1523, 880, 3)
    py.leftClick()

    n = 5
    n = int(2*(n+1))
    time.sleep(0.2)
    py.moveRel(0, -350, 0.2)
    py.scroll(-29 * (n-1))
    py.leftClick()
    py.scroll(20)

    # py.scroll(-40)
    # py.leftClick()
    # time.sleep(0.2)
    py.leftClick()
    time.sleep(0.2)

    # Selección de duración 2h
    py.moveRel(-300, 350, 0)
    py.leftClick()
    py.scroll(-20)
    py.leftClick()
    py.scroll(20)


def hour(n):

    n = int(4*(n+1))
    time.sleep(0.2)
    py.moveRel(-300, 0)
    py.leftClick()
    py.moveRel(0, -350, 0.2)
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

    # Seleccionar día
    time.sleep(0.2)
    py.moveTo(coor)
    py.leftClick()
    time.sleep(0.2)

    # Clickear boton BOOK
    py.scroll(-500)
    py.moveTo(1705, 730, 0.5)
    py.leftClick()


def main():

    correos = ["samir.suarez", "carlos.rojas", "fabiola.fuentes"]
    before_book()

    #day = time.localtime().tm_wday
    day = 4
    monday(day, 11)
    monday(day, 3, correos[2])
    tuesday(day, 9)
    wednesday(day, 10)
    thursday(day, 15)
    friday(day, 9)
    saturday(day)
    sunday(day, 15)

    return 0


time.sleep(5)
main()
# time.sleep(4)
#
# py.scroll(-500)
#
# time.sleep(4)
# print(py.position())
