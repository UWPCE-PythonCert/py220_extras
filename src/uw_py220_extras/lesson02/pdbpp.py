#!/usr/bin/env python

def myfunc():
    import pdb; pdb.set_trace()
    a = 1
    b = 6
    c = a + b
    print(a)

def not_worried_about_this():
    xx = 99
    yy = xx * 78

if __name__ == "__main__":
    not_worried_about_this()
    myfunc()
