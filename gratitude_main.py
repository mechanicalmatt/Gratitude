

import time


db = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/gratitude.txt"
day = ""


info = input('what are you grateful for today? -> ')

def append(text):
    with open(db, 'a') as f:
        text = print(info, file=f)

def read():
    with open(db, 'r') as f:
        for i in f.readlines():
            print(i)
        input('...')

def run():
    if info == 'READ':
        print(read())
    else:
        append(info)

# read()
run()
# read()

