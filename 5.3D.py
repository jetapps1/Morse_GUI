import tkinter as tk
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)

frame = tk.Tk()
frame.title("Morse Code 5.3D")
frame.geometry('400x200')

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def printInput():
        morsecode = encrypt(inputtxt.get(1.0, "end-1c").upper())
        for letter in morsecode:
                if(letter == "."):
                        GPIO.output(17, GPIO.HIGH)
                        time.sleep(0.3)
                        GPIO.output(17, GPIO.LOW)
                        time.sleep(0.3)
                if(letter == "-"):
                        GPIO.output(17, GPIO.HIGH)
                        time.sleep(0.9)
                        GPIO.output(17, GPIO.LOW)
                        time.sleep(0.3)
                if(letter == " "):
                        time.sleep(0.6)


inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)

inputtxt.pack()

printButton = tk.Button(frame,
                        text = "Show Morse Code",
                        command = printInput)
printButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()

frame.mainloop()
