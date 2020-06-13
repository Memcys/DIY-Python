# -*- coding: utf-8 -*-
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
#     language: python
#     name: python38364bita14c50cabb94433e97ec307454e1294b
# ---

from numpy.random import randint

import logging
logging.getLogger().setLevel(logging.INFO)

l = ['ML', 'WJ', 'FL', 'CS', 'ZF', 'YH', 'FY', 'YW']
l.sort()
l


# New feature in Python 3.8:
# - [assignment (“the walrus operator”) `:=`](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)
# - [f-strings support = for self-documenting expressions and debugging](https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging)

def f(l: list):
    '''select a random person in the list,
    print it out and then pop it
    '''
    if (sz := len(l)) > 0:
        n = randint(sz)
        print(f'{n=}; {l[n]=}')
        l.pop(n)
    else:
        # or print if you prefer
        logging.info('omitting blank list')


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
