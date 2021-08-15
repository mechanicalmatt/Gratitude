

from datetime import date
import random

db = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/gratitude.txt"
day = ""
today = date.today()

random_entry = ""
all_entries = []

print()
# print entry from random date
def rand_selection():
    with open(db, 'r') as f:
        count = 0
        for entry in f.readlines():
            count += 1
            all_entries.append(entry)
        selection = random.randrange(count)
    all_entries_strip = [i.strip('\n') for i in all_entries]
    return all_entries_strip[selection]
print(rand_selection())
print()

stuff = input('what are you grateful for today? -> ')
info = [str(today) + ': ' + stuff]

def append(text):
    with open(db, 'a') as f:
        text = print(info, file=f)

def read():
    with open(db, 'r') as f:
        count = 1
        for i in f.readlines():
            print(str(count) + ' ' + i)
            count += 1
        input('...')

def run():
    if stuff == 'READ':
        print()
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print(read())
    else:
        append(info)

# read()
run()
# read()

