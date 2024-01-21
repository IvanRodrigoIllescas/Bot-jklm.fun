from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

import pyperclip



import random, pyautogui

mouse=Controller()

global txtbomb

archivo_nombre='palabras.txt'
archivo = open(archivo_nombre,mode='r',encoding='UTF8')
global listaPalabras
listaPalabras = archivo.read().split()
archivo.close()

#print(listaPalabras)

global bombX
global bombY

global cajaX
global cajaY

global usadas

usadas=[]

bombX=0
bombY=0

cajaX=0
cajaY=0


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        
    # las teclas Fx son especiales y dan error    
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

        #localizar bomba f8
        if key==key.f8:

            global bombX
            global bombY

            print('f8, localizar bomba')
            bombX, bombY=pyautogui.position()
            print('bomba x', bombX, 'bomba y ', bombY)

        #localizar caja f7
        if key==key.f7:

            global cajaX
            global cajaY

            print('f7, localizar caja')
            cajaX, cajaY=pyautogui.position()
            print('caja x', cajaX, 'caja y ', cajaY)

        if key==key.f9:
            print('f9, resolver')

            pyautogui.moveTo(bombX, bombY)
            pyautogui.doubleClick()

            pyautogui.hotkey('ctrl', 'c')

            global txtbomb
            
            txtbomb = pyperclip.paste()

            global palabra

            try:
                palabra= enc_palabra(txtbomb)
            except:
                print('error')
                palabra='ERROR NT FOUND'
            
            pyautogui.moveTo(cajaX, cajaY)
            pyautogui.click()

            try:
                pyautogui.typewrite(palabra, interval=0.001)
                pyautogui.press('enter')
            except:
                print('error2')

        
        if key==key.f2:
            print (posibles)
            fail = open ('fail.txt','a')
            fail.write(posibles+'\n')
            fail.close()
            

def enc_palabra(letras):
    print(letras)

    global posibles
    for i in listaPalabras:
        x = i.find(letras)
        if x!=-1:
            posibles=i
            usadas.append(i)
            listaPalabras.remove(i)
            break;
    print(posibles)
    return posibles
    

    

def on_release(key):
    print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Listener
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

