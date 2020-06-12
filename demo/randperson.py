# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3.8.3 64-bit
#     name: python38364bita14c50cabb94433e97ec307454e1294b
# ---

from numpy.random import randint

l = ['ML', 'WJ', 'FL', 'CS', 'ZF', 'YH', 'FY', 'YW']
l.sort()
l


def f(l: list):
    '''select a random person in the list,
    print it out and then pop it
    '''
    sz = len(l)
    n = randint(sz)
    print(l[n])
    l.pop(n)


f(l)
l

f(l)
l

f(l)
l

f(l)
l

f(l)
l

f(l)
l

f(l)
l

f(l)
l

f(l)
l
