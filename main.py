import pyautogui
import keyboard
import winsound
images = {
    "buy": "images/buy.png",
    "cantbuy1": "images/cantbuy1.png",
    "cantbuy2": "images/cantbuy2.png",
    "cantpay": "images/cantpay.png",
    "cantprison": "images/cantprison.png",
    "deny": "images/deny.png",
    "drop": "images/drop.png",
    "dropcube": "images/dropcube.png",
    "pay": "images/pay.png",
    "decline": "images/decline.png",
    "surrender": "images/surrender.png",
    "sell": "images/sell.png",
    "exit": "images/exit.png",
    "create": "images/create.png",
    "two": "images/two.png",
    "createroom": "images/createroom.png"
}

# brands = [
#     "brands/adidas.png",
#     "brands/american.png",
#     "brands/apple.png",
#     "brands/audi.png",
#     "brands/boss.png",
#     "brands/british.png",
#     "brands/chanel.png",
#     "brands/facebook.png",
#     "brands/fanta.png",
#     "brands/ford.png",
#     "brands/holidayinn.png",
#     "brands/kfc.png",
#     "brands/lacoste.png",
#     "brands/landrover.png",
#     "brands/lufthansa.png",
#     "brands/mercedes.png",
#     "brands/nokia.png",
#     "brands/novotel.png",
#     "brands/puma.png",
#     "brands/radissonblu.png",
#     "brands/rockstar.png"
# ]


def find(image):
    return pyautogui.locateOnScreen(images[image], confidence=.8)


def click(ptr):
    if ptr is not None:
        center = pyautogui.center(ptr)
        pyautogui.moveTo(center[0], center[1], duration=0)
        pyautogui.leftClick()
        pyautogui.moveTo(100,200, duration=0)


# def trytosell():
#     for brand in brands:
#         ptr = pyautogui.locateOnScreen(brand, grayscale=True, confidence=.7)
#         if ptr is not None:
#             ptr2 = pyautogui.locateOnScreen(images['sell'], confidence=.7)
#             if ptr2 is not None:
#                 click(ptr2)
#                 return True
#     return False


def find_click(image):
    ptr = find(image)
    click(ptr)



def bot():
    global images
    prisontick = False
    #find_click('exit')
    find_click('decline')
    print("ищу1")
    find_click('deny')
    print("ищу2")
    find_click('drop')
    print("ищу3")
    find_click('buy')
    print("ищу4")
    ptr = find('pay')
    if ptr is not None:
        print(0)
    click(ptr)
    find_click('surrender')
    ptr = find('cantprison')
    if ptr is not None:
        prisontick = True
        ptr = find('dropcube')
        click(ptr)
    ptr = find('cantbuy2')
    if ptr is not None:
        ptr = find('buy')
        if ptr is None:
            click(ptr)
    ptr = find('cantpay')
    if ptr is not None and not prisontick:
        winsound.Beep(3000, 1000)


def main():
    while True:
        if keyboard.is_pressed(';'):
            break
        bot()


main()
