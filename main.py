from typing import Final
from tkinter import *

constvar: Final = 5

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

myset: set = {
    'a': 'Anil',
    'b': 'buppy',
    'c': 'chloe',
    'k': 'kapil',
    'c': 'chandan'
}

mytuple = (1, 2, 3, 'abc', 'hello')

listOfDictionary = [
    {
        'name': 'manish',
        'age': 24,
    },
    {
        'name': 'kapil',
        'age': 14
    },
    {
        'name': 'saching',
        'age': 45
    }
]

myDictionar = {
    'samsung': '9000',
    'nokia': '10000',
    'lava': '11000',
    'micromax': '15000',
    'xioni': '9000'
}








def add(a, b):
    return a + b


def myloop(arr: list):
    arr.append(45)
    for val in arr:
        print(val)


def dictionaryprint(dic: dict):
    for key, value in dic.items():
        print("key-->", key, 'value-->', value)
        print(f"key-->{key} value--> {value}")


def printingtuple(ctuple: tuple):
    for a in ctuple:
        print(a)



mul = lambda a,b: a*b

print(mul(4,5))


class Vehicle:
    name: str
    color: str
    _window = 6
    __wiper = 78



    def __init__(self,name,color):
        print('initialization')
        self.name=name
        self.color=color


    def running (self):
        print('running')

    def horn(self):
        print('horn')

    def printing(self):
        print(f'name-->{self.name}  color--->{self.color}')

    def __del__(self):
        print('distruction')



if __name__ == "__main__":
    print('inside main')
    print(add(4, 5))
    myloop(mylist)
    dictionaryprint(myDictionar)
    car1 = Vehicle('lemborgini', 'yellow')

    print(car1)
    car1.running()
    car1.horn()
    car1.printing()
    print(car1._window)
    root = Tk()
    root.configure(background='light green')
    root.geometry("300x200")
    root.title("Flames Game")
    root.mainloop()