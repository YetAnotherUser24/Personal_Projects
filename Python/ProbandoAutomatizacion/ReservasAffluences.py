import time
import pyautogui as py


def after_book(correo):

<<<<<<< HEAD
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
=======
    # Moverse y registrar el apartado de correo
    time.sleep(2)
>>>>>>> d5e752672bd6bca29a124d48a85738ed2aebcc09
    py.scroll(-1000)
    py.moveTo(694, 205, 0.1)
    py.leftClick()
    py.write(correo, 0.01)
    py.hotkey("altright", "q")
    py.write("utec.edu.pe", 0.01)
    time.sleep(0.1)

    # Moverse y registrar la cantidad de personas
    py.moveRel(0, 150)
    py.leftClick()
    py.write("2", 0.01)
    time.sleep(0.1)

    # Aceptar los terminos y condiciones
    py.moveRel(0, 130)
    py.leftClick()

    # Guardar
    py.moveRel(330, 130)
    py.leftClick()

    # Cerrar
    time.sleep(1)
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
    py.moveRel(0, -350)
    py.scroll(-29 * (n-1))
    py.leftClick()
    py.scroll(20)


<<<<<<< HEAD
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
=======
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
    coor = py.locateCenterOnScreen(ruta, confidence=0.8)

    # Seleccionar día
    time.sleep(0.1)
    py.moveTo(coor)
    py.leftClick()
    time.sleep(0.1)

    # Clickear boton BOOK
    time.sleep(1)
    py.scroll(-500)
    py.moveTo(1705, 730)
    py.leftClick()


def weekday(diasem, hora, correo="samir.suarez"):
    dic = {"mo": 0, "lu": 0, "tu": 1, "ma": 1, "we": 2, "mi": 2,
           "th": 3, "ju": 3, "fr": 4, "vi": 4, "sa": 5, "su": 6, "do": 6}

    w = (time.localtime().tm_wday + 1) % 7

    if (dic[diasem] == w):
        before_book()
        hour(hora)
        day()
        after_book(correo)


def main():
    correos = ["samir.suarez", "carlos.rojas", "fabiola.fuentes"]

    weekday("mo", 15)
    weekday("tu", 11)
    weekday("tu", 16, correos[2])
    weekday("we", 9)
    weekday("we", 11, correos[2])
    weekday("th", 10)
    weekday("th", 17, correos[2])
    weekday("fr", 15)
    weekday("sa", 9)
    weekday("sa", 11, correos[2])

    print("Ejecucion terminada con exito!!!")
    return 0


main()
>>>>>>> d5e752672bd6bca29a124d48a85738ed2aebcc09
