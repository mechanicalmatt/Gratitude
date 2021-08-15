from datetime import date
import random

db = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/gratitude.txt"
day = ""
today = date.today()

random_entry = ""
all_entries = []


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

info = [str(today) + ': ' + input('what are you grateful for today? -> ')]

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