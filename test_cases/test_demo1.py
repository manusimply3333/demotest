import pytest


def test1():
    print("This is Test1, it will pass")

def test2():
    print("This is Test2, This will fail")
    assert 1 == 2,"wrong assertion"

def test3():
    print("This is Test3, it will run for loop")
    for i in range(0,10):
        print(f"The value is {i}")

def test4():
    print("This is additional test added")

def test5():
    print("added one more test")